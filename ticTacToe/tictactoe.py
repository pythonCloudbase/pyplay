from random import randint

arr = ['1','2','3','4','5','6','7','8','9']
def board():
    for i in range(8,-1,-1):
        print(arr[i], end=" ")
        if((i)%3 == 0):
            print("\n")
        else:
            print("|",end=" ")

def checkWin(sign):
    if arr[0] == sign :
        if arr[1] == sign :
            if arr[2] == sign :
                return True
        elif arr[3] == sign :
            if arr[6] == sign :
                return True
        elif arr[4] == sign :
            if arr[8] == sign :
                return True
    elif arr[8] == sign :
        if arr[7] == sign :
            if arr[6] == sign :
                return True
        elif arr[5] == sign :
            if arr[2] == sign :
                return True

    elif arr[7] == sign :
        if arr[4] == sign :
            if arr[1] == sign :
                return True
    
    elif arr[5] == sign :
        if arr[4] == sign :
            if arr[3] == sign :
                return True  

    else:
        return False        

board()

gameOn = True
turn = 1
player = 0
sign = None
win = False

signs = ['X', 'O']
index = randint(0,1)
sign1 = signs[index]
if index == 0:
    sign2 =  signs[1]
else:
    sign2 = signs[0]

print("Player 1 has been assigned " + sign1 )
print("Player 2 has been assigned " + sign2 + "\n")

while( gameOn):
    if(turn%2 ==0):
        player = 2
        sign = sign2
    else:
        player = 1
        sign = sign1

    get = int(input("player " + str(player) + " : "))
    
    arr.insert(get,sign)
    arr.remove(str(get))

    print("turn " + str(turn) +" : ")
    board()
    print(arr)
    win = checkWin(sign)
    if (win):
        print( "player " + str(player)  + " wins !")
        gameOn = False
        break

    if(turn == 9):
        print ("Its a dull draw !")
        gameOn = False
    
    turn += 1
        

