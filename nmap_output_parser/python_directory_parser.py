mypath = "./INA"

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)

for file_name in onlyfiles:

    input_file = join(mypath,file_name)
    print("parsing now: ", input_file)

    f = open(input_file)

    fulltext = f.readlines()

    # print(fulltext)

    scan_at = []
    port_data = []

    ip_found = 0
    port_filter = False

    port_filter_stop_words = ["MAC Address", "Warning", "Device type", "Running", "OS CPE", "cpe", "OS details", "Network Distance", "Service Info" ]

    interesting_info = {}


    for i,text in enumerate(fulltext):
        if (len(text.split('Nmap scan report for '))>1):
            ip_found += 1
            scan_at.append(text.split('Nmap scan report for ')[1])
            port_data.append("\nSCAN AT: " + scan_at[ip_found-1])
            
        if (len(text.split('PORT'))>1):
            port_filter = True
        
        if (text.split(":")[0] in port_filter_stop_words):
            port_filter = False
            interesting_info[text.split(":")[0]] = "".join(text.split(":")[1:])

        if (port_filter):
            if(text[0].isdigit()):
                port_data.append(text)
        
    # print("SCAN AT: ", scan_at)

    # print("PORT INFORMATION: ")
    # print("\n".join(port_data))

    # print("OTHER INFORMATION: ")

    # for k, v in interesting_info.items():
    #     print ("{:<8} {:<15}".format(k, v))

    f.close()

    w = open("output/output_"+file_name, 'w+')

    w.write("\n")
    w.write("PARSED INFORMATION FROM FILE : " + file_name + "\n")
    w.write("".join(port_data))
    w.write("\n")
    # w.write("OTHER INFORMATION: ")
    # w.write("\n")
    # for k, v in interesting_info.items():
    #     w.write ("{:<8} {:<15}".format(k, v))