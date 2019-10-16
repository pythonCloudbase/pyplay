get = input("Enter the passwords: ").split(',')

goodpass = []
for i in get :
    passed = 0
    if (len(i) > 5 & len(i) < 13):
        for j in i:
            if(j.isupper()):
                passed += 1
            if(j.islower()):
                passed += 1
            if(j.isnumeric()):
                passed += 1
            if(j in ['$','#','@']):
                passed += 1
    if(passed > 3):
        goodpass.append(i)

print(",".join(goodpass))
