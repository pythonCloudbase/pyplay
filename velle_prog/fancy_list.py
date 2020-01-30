get = input('Enter the content of the list : ')
#get = "She knows she'll find love"

array  = get.split(" ")

max_length = 1
for i in array:
    if(len(i) > max_length):
        max_length = len(i)

print(max_length)

print('*' * (max_length + 4))

for i in array:
    print('* ' + i + ' ' * (max_length - len(i) +1 ) + '*')

print('*' * (max_length + 4))