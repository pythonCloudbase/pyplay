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

while( gameOn):
    if(turn%2 ==0):
        player = 2
        sign = 'O'
    else:
        player = 1
        sign = 'X'

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
        

