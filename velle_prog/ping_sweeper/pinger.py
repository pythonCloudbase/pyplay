import subprocess
pingable =[]

for ping in range(1,100):
    address = "10.10.10." + str(ping)
    res = subprocess.call(['ping', '-c', '3', address])
    if(res == 0):
        #print("ping to ", address, " OK.")
        pingable.append(address)

print("\n".join(pingable))