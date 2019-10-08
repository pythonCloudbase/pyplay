import math
iter = []
for i in range (1000,30001):
    c = i
    flag = True
    while(c>1):
        if((c%10)%2 != 0):
            flag = False
        c = math.floor(c/10)
        

    if(flag):
        iter.append(str(i))

print(",".join(iter))
