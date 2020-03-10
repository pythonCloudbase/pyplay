class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if (self.data):
            if (data < self.data):
                if(self.left is None):
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif(data > self.data):
                if(self.right is None):
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else :
            self.data = data

    def returnData(self):
        return self.data
    
    def printTree(self):
        if(self.left):
            self.left.printTree()
        print(self.data, end = " ")
        if(self.right):
            self.right.printTree()
    
    # inorder traversal
    def inOrderTraversal(self,root):
        res =[]
        if root:
            res = self.inOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.inOrderTraversal(root.right)
        return res
    
    # search
    def search(self, target):
        if (self.data == target):
            return True
        elif (self.data < target):
            if(self.right):
                return self.right.search(target)
        elif(self.data > target):
            if(self.left):
                return self.left.search(target)
        
        return False

root = Node(12)
root.insert(6)
root.insert(100)
root.insert(7)
root.insert(8)
root.insert(9)
root.insert(2)
    
#root.printTree()

print(root.inOrderTraversal(root))

print(root.search(5))
print(root.search(6))