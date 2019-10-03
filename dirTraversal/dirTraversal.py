import os

rootdir = "Z:\codeplay\machine_mash\machine_mash\pyImagenet\\testing"

#print(dir(os))
#print(rootdir)

for dirName, subdirList, fileList in os.walk(rootdir):
    for fname in fileList :
        print('\t %s' % fname)
    
        