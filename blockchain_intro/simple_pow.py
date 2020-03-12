from hashlib import sha256
x = 5
y = 0
while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y +=1

print(f'The solution is y = {y}')

print(hash(5*21))

# in blockchain the proof of work is called hashcash
