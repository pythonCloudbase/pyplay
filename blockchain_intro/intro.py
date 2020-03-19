import hashlib
import json
from time import time
from textwrap import dedent
from uuid import uuid4
from urllib.parse import urlparse
import requests

from flask import Flask, jsonify, request

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        self.nodes = set()

        # new genesis block
        self.new_block(previous_hash=1, proof=100)

    def register_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def new_block(self, proof, previous_hash=None):

        # create a new block
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        # reset the list of current transaction
        self.current_transaction = []

        # add it to the chain
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):

        # create new transaction to go into next mined block
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # hashes a block
        block_string =  json.dumps(block, sort_keys=True).encode()
        
        # returns the hash
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):

        # returns last block
        return self.chain[-1]
    
    def proof_of_work(self, last_block):
        # find a number p such that hash(pp') constains 4 leading zeros, where p is the previous p'
        # p is the previous proof and p' is the new proof

        # this function is wrapper over valid proof

        last_proof = last_block['proof']
        last_hash = self.hash(last_block)

        proof = 0
        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1
        
        return proof
    
    @staticmethod
    def valid_proof(last_proof, proof, last_hash):
        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
    
    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1

        while (curent_index < len(chain)):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n---------\n")

            #check that the hash of the block is correct
            if block['previous_hash'] != self.hash(last_block):
                return False
            
            #check that the proof of work is correct
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False
            
            last_block = block
            current_index += 1
        
        return True
    
    def resolve_conflicts(self):
        # this resolves conflicts by replacing our chain with the longest one in the network

        neighbhors = self.nodes
        new_chain = None

        # we are looking at chain longer than ours
        max_length = len(self.chain)

        # grab and verify the chains from all the nodes in our network
        for node in neighbhors:
            response = requests.get(f'http://{node}//chain')

            if response.status_code ==200:
                length = response.json()['length']
                chain = response.json()['chain']

                # check if the length is longer and the chain is valid
                if (length > max_length and self.valid_chain(chain)):
                    max_length = length
                    new_chain = chain
            
            if new_chain:
                self.chain = new_chain
                return True
            
            return False 

###################################################   blockchain class end

app = Flask(__name__)

# generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '') 

# instantiate the blockchain
blockchain = Blockchain()



@app.route('/mine', methods=['GET'])
def mine():
    # We run the proof of work algorithm to get the next proof
    last_block = blockchain.last_block
    
    proof = blockchain.proof_of_work(last_block)

    # now we need to give reward for mining
    blockchain.new_transaction(
        sender = "0",
        recipient = node_identifier,
        amount =1
    )

    #forge new block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }

    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    print(values)

    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return "missing values", 400
    
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to BLock {index}'}

    return jsonify(response), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@ app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400
    
    for node in nodes:
        blockchain.register_node(node)
    
    response ={
        'message': 'new nodes have been added',
        'total_nodes': list(blockchain.nodes)
    }
    return jsonify(response), 201

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was authoritative',
            'chain': blockchain.chain
        }
    
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



