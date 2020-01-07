class Tower():
    def __init__(self):
        self.container = []

    def push(self,element):
        self.container.append(element)

    def pop(self):
        self.container.pop()

    def move_peg(self,t):
        t.push(self.container.pop())

    def __repr__(self):
        return repr(self.container)

# psuedocode 
# if n = 1 move from start to end
# move n -1 peg to to rest of the towers with temp as the in between


def hanoi(start, end, temp, n):
    if (n == 1):
        start.move_peg(end)
    
    else:
        hanoi(start, temp, end, n-1)
        hanoi(start, end, temp, 1)
        hanoi(temp, end, start, n-1)
        

if __name__ == "__main__":
    A = Tower()
    B = Tower()
    C = Tower()
    N = 3

    for i in range(0, N):
        A.push(i + 1)

    # print(A, B , C)
    # A.move_peg(B)
    print(A, B, C)

    hanoi(A, C, B, N)
    print(A, B, C)


    