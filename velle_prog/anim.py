import time
import sys

# sample input
# python anim.py 20 "|/-\\" 100

animation = "|/-\\"
animation1 = "MW"
animation2 = "(O|O)"
animation3 = str(sys.argv[2])


for i in range(int(sys.argv[3])):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation3[i % len(animation3)] * int(sys.argv[1]))

    sys.stdout.flush()

print("End !")