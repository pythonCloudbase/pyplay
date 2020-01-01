def fib(n):
    if(n == 1 or n == 0):
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    get = input("Enter: ")
    print(fib(int(get)))
