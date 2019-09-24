get = input("Enter input: ").split(',')

X = int(get[0])
Y = int(get[1])

# multiList = [[0 for j in range(Y)] for i in range(X)]

print(multiList)

for i in range(X):
    for j in range(Y):
        multiList[i][j] = i*j

print(multiList)