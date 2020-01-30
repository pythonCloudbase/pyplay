get  =  "The dog ate the car"

sentence = []
for i in get.split(" "):

    tail = i[0]

    new_str  = i.replace(i[0], '')
    new_str += tail + 'ay'
    sentence.append(new_str)

print(" ".join(sentence))
