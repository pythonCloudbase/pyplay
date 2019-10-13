get = input("Enter the number list: ").split(',')

out = [str(int(x)*int(x)) for x in get if (int(x)%2 != 0)]

print(",".join(out))

