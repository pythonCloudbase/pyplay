get = input("Enter the phrase :")
#print(get)

letters = 0
numbers = 0

for i in get:

    # if (i in (range(ord('a'), ord('z')) or range(ord('A'), ord():
    #     letter += 1
    # elif(i in range(0,10)):
    #     numbers += 1

    #print(i)
    if(i.isalpha()):
        letters += 1
    elif(i.isnumeric()):
        numbers += 1

print("LETTERS ", letters)
#("NUMBERS ", numbers)