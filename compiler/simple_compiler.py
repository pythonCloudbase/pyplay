# * 5 3

stack  = input(':>').split(' ')
stack = stack[::-1]

print(stack)

i = 0
while(len(stack)>2):

    if (stack[i] in ["*", "+", "-", "/"]):
        # remove stack[i], stack[i+1], stack[i+2]
        # add compute(stack[i + 1] stack[i] stack[i+2]) in stack

        first = int(stack[i-1])
        second = int(stack[i-2])

        print(stack[i-2], stack[i-1])
        

        if (stack[i] == '*'):
            temp = first * second
            
        elif (stack[i] == '+'):
            temp = first + second
            
        elif (stack[i] == '-'):
            temp = first - second
            
        elif (stack[i] == '/'):
            temp = first / second

        n = len(stack)

        print(stack[i])
        stack.remove(stack[i])
        print(stack)
        stack.remove(stack[i-1])
        print(stack)
        stack.remove(stack[i-2])
        print(stack)
        stack.insert(0,str(temp) )
        print(stack)  
        i = -1 

    i+= 1

print("final :", stack[0])
