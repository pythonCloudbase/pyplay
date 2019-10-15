import sys

get = sys.stdin.readlines()

money = 0

for i in range(len(get)):
    tokens = get[i].split()
    if (tokens[0] == 'd'):
        money += int(tokens[1])
    elif (tokens[0] == 'w'):
        money -= int(tokens[1])
    else :
        print("improper format given", " ".join(get[i]))

print(money)