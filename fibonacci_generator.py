from typing import Generator

def fib6(n):
    yield 0
    if n > 0: yield 1
    last = 0
    nex = 1
    for _ in range(1,n):
        last, nex = nex, last + nex
        yield nex
    

if __name__ == "__main__":
    for i in fib()
