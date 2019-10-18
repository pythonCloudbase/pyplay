get = input("Input range : ").split(',')

for i in range(int(get[0]), int(get[1])):
    if(i%7 == 0):
        print(i)

