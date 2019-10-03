import sys
print("Enter lines : ")
userInput = sys.stdin.readlines()

#print(userInput)

oline = ""

for word in userInput:
    oword = ""
    for char in word:
        #print("char: ", char)

        if(ord(char) in range(97,123) ):
            char  = chr(ord(char)-32)
            #print("char changes: ", chr(ord(char) -32))
            
        oword += char
    oline += oword 

print(oline)


#print(ord('a') - ord('A')) --32
