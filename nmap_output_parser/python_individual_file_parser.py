input_file = "input.txt"

f = open(input_file)

fulltext = f.readlines()

# print(fulltext)

scan_at = ""
port_data = []

port_filter = False

port_filter_stop_words = ["MAC Address", "Warning", "Device type", "Running", "OS CPE", "cpe", "OS details", "Network Distance", "Service Info" ]

interesting_info = {}


for i,text in enumerate(fulltext):
    if (len(text.split('Nmap scan report for '))>1):
        scan_at = text.split('Nmap scan report for ')[1]
    if (len(text.split('PORT'))>1):
        port_filter = True
    
    if (text.split(":")[0] in port_filter_stop_words):
        port_filter = False
        interesting_info[text.split(":")[0]] = "".join(text.split(":")[1:])

    if (port_filter):
        port_data.append(text)
    
print("SCAN AT: ", scan_at)

print("PORT INFORMATION: ")
print("\n".join(port_data))

print("OTHER INFORMATION: ")

for k, v in interesting_info.items():
    print ("{:<8} {:<15}".format(k, v))

f.close()

w = open("output/output_"+input_file, 'w+')

w.write("SCAN AT: ")

w.write(scan_at)
w.write("\n")
w.write("PORT INFORMATION: ")
w.write("".join(port_data))
w.write("\n")
w.write("OTHER INFORMATION: ")
w.write("\n")
for k, v in interesting_info.items():
    w.write ("{:<8} {:<15}".format(k, v))