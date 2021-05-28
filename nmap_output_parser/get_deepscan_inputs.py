input_file = open('os_new_output.txt', 'r+').readlines()

services = []
current_host = ""

import subprocess as sp

for i in input_file:
    i = i.strip()
    
    try:
        if(i[0] =="#"):
            current_host = i.split(":")[1]

        if(i[0].isnumeric()):
            port = i.split("/")[0]

        run_command = f"nmap -A -sV -p {port} {current_host}"
        print("\n" + run_command)

        output = sp.getoutput(run_command)

        split_out = output.split("\n")
        write=False
        for s in split_out:
            fulls = s.split(" ")
            if(len(fulls)<2):
                write=False
            for f in fulls:
                if (f == "PORT"):
                    write= True
        
            if (write):
                print(s)


    except:
        pass 
