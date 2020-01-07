n_dict = {}
n_dict[1] = 1
n_dict[0] = 0

def fibo(n):
    if(n not in n_dict):
        n_dict[n] = fibo(n-1) + fibo(n-2)
    
    return n_dict[n]

if __name__ == "__main__":
    get = int(input('Enter n: '))
    print(fibo(get))