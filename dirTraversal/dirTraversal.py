import os

rootdir = "."

for dirName, subdirList, fileList in os.walk(rootdir):
    print('Found directory: %s' % dirName)
    for dname in subdirList :
        print('\t %s' % dname)
    
    for fname in fileList :
        print('\t %s' % fname)
    
        