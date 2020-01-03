memo = {}

memo[0] = 1
memo[1] = 1

print(memo)

def fib(n):

    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    
    return memo[n]

    # if(n < 2):
    #     return 1
    # else :
    #     return fib(n-1) + fib(n-2)


get = int(input('Enter fibonacci sequence number: '))

print(fib(get))