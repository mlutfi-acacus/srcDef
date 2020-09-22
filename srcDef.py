#!/usr/bin/python3
import shutil
import sys
import os
import hashlib


def hashFile(fileName):
    data = open(fileName).read()
    return hashlib.md5(data.encode()).hexdigest()



fileName = sys.argv[1]

shutil.copy(fileName, "{}.{}".format(fileName, hashFile(fileName)))

if os.path.isfile(fileName+"e"):
    os.system("rm {}e".format(fileName))

os.system("sourcedefender encrypt {}".format(fileName))






f = open(fileName,"w")
f.write("import sourcedefender\n")
f.write("import {}".format(fileName.rstrip(".py")))
f.close()
