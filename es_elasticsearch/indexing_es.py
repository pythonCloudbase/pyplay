import requests

# checking if elastic search is on
res = requests.get('http://localhost:9200')
#print(res.content)

# getting elasticsearch working
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port' : 9200}])

# putting files onto the database
import json
r = requests.get('http://localhost:9200')
i = 1
while i != 200:
    r = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(i))
    print(i, r)
    try:
        es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
    except Exception as e:
        print(e)
    i = i+1

print(i, " entries put into the database.")

