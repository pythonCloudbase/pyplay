input_file = open('site_list.txt', 'r+').readlines()

# print(input_file)

import nmap

results_array = []
site_names = []

nm = nmap.PortScanner()

for i in input_file:
    print('----------------------------------------------------')
    print(f'Scanning for {i}')
    nm.scan(i)
    print(f'Host : {nm[i].hostname()}')
    print(f'State : {nm[i].state()}')
    for proto in nm[i].all_protocols():
        print('----------')
        print(f'Protocol : {proto}')
        
        lport = nm[i][proto].keys()
        lport.sort()
        for port in lport:
            print ('port : %s\tstate : %s' % (port, nm[i][proto][port]['state']))
    