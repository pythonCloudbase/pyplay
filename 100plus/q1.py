get = input("Enter the sentence : ").split(" ")
unique = list(set(get))
unique.sort()

diction = {}

for i in unique :
    diction[i] = 0

for j in get:
    diction[j] += 1

for z in diction.keys():
    print(z, ':', diction[z])
