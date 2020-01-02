def fiboloop(n):
    first = 0
    second = 1
        
    for _ in range(1,n):
        temp = second
        second = first + second
        first = temp

    return second + first


if __name__ == "__main__":
    print(fiboloop(5))    


