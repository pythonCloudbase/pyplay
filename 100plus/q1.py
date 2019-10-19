import sys
import math

get = sys.stdin.readlines()

x = 0
y = 0

for action in get:
    direction = action.strip('\n').split(' ')[0].lower()
    steps = action.strip('\n').split(' ')[1]

    if (direction == 'up'):
        y -= int(steps)
    elif (direction == 'down'):
        y += int(steps)
    elif (direction == 'left'):
        x -= int(steps)
    elif(direction == 'right'):
        x += int(steps)
    else:
        pass


print(math.floor(math.sqrt(x**2 + y**2)))


