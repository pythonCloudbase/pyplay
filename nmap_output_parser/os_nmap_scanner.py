import os

input_file = open('site_list.txt', 'r+').readlines()

import subprocess as sp

outputs = []
for idx, i in enumerate(input_file):
    i = i.strip()
    print(f"\n#{idx+ 1}. running for :{i}\n")
    output = sp.getoutput(f'nmap -F {i}')

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
        