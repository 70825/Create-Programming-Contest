import os
import glob

files = glob.glob("./tests/*")
for name in files:
    if not os.path.isdir(name):
        src = os.path.splitext(name)
        if src[1] == '':
            os.rename(name, src[0]+'.in')
        else:
            os.rename(name, src[0]+'.out')