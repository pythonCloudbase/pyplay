get = input( "Enter thre phrase: " )

upper = 0
lower = 0

for i in get :
    if(i.isupper()):
        upper += 1
    elif(i.islower()):
        lower += 1

print("UPPER ", upper)
print("LOWER ", lower)



