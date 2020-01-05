class Stack():
    def __init__(self):
        self.container = []
    
    def push(self, item):
        self.container.append(item)
    
    def pop(self):
        self.container.pop()
    
    def __repr__(self):
        return repr(self.container)

num_discs = 3

tower_a = Stack()
tower_b = Stack()
tower_c = Stack()

for i in range(1, num_discs + 1):
    tower_a.push(i)
    tower_b.push(i)
    tower_c.push(i)

print(tower_a.__repr__())
print(tower_b.__repr__())
print(tower_c.__repr__())