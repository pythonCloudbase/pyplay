import sys

get= sys.stdin.readlines()

sortScoreList = []

for line in get :
    totalscore = 0
    
    name,age,score = line.strip().split(',')
    #print(name,age,score)

    d = 1
    for char in name:
        totalscore += ord(char) * 100000/d
        d = d * 10

    totalscore += int(age) + int(score)
    sortScoreList.append(totalscore)


#print(sortScoreList)


sortIndex = []
for i in range(len(sortScoreList)):
    min = 0

    for j in range(len(sortScoreList)):
        print(min,j)
        if (sortScoreList[min] > sortScoreList[j]):
            
            min = j
    sortIndex.append(min)
    sortScoreList[min] = 1000000000000000000
    #print(sortScoreList, sortIndex)

#print(sortIndex)


for i in sortIndex:
    print((get[i].strip()))

