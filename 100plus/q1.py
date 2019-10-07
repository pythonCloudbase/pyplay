get = input("Enter  number sequence: ").split(',')

out = []
for i in get:
    if(int(i)%5 == 0):
        out.append(i)

print(",".join(out))
