# my solution
number= input('Enter a number : ')
ans=1
for i in range(1,int(number)+1):
    ans=ans*i
print(ans)

""" proposed solution

def fact(x):
    if(x==0):
        return x
    else:
        return x * fact(x -1)
x = input("enter a number: ")
print(fact(x))

"""
