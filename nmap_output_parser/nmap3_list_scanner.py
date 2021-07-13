input_file = open('site_list.txt', 'r+').readlines()

# print(input_file)

import nmap3

nmap = nmap3.Nmap()

results_array = []
site_names = []
for i in input_file:
    i = i.strip()
    site_names.append(i)
    print(f"Processing for {i}")
    results = nmap.scan_top_ports(i.strip())
    results_array.append(results)
    break

for results in results_array:
    print(results)
