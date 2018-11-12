#!/usr/bin/env python3
import os
from hashlib import md5

dir1 = ["/Users/amandeep/python/test/test1"]
dir2 = ["/Users/amandeep/python/test/test2",
        "/Users/amandeep/python/test/test3"]

set1 = []
set2 = []

#MAX_SIZE = 2097152
MAX_SIZE = 0.1 * 1024 * 1024

print("List of Dir in Set1: ")
for i in range(len(dir1)):
    if os.path.isdir(dir1[i]):
        print(" - ", dir1[i])
    else:
        print("Invalid Dir: ", dir1[i])

        
print("List of Dir in Set2: ")
for i in range(len(dir2)):
    if os.path.isdir(dir2[i]):
        print(" - ", dir2[i])
    else:
        print("Invalid Dir: ", dir2[i])

for i in range(len(dir1)):
    for root,dir,fname in os.walk(dir1[i]):
        for file in fname:
            fullpath = os.path.join(root, file)
            size = os.path.getsize(fullpath)
            if size > MAX_SIZE:
                afile = open(fullpath, 'rb')
                hasher = md5()
                buf = afile.read(65536)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = afile.read(65536)
                afile.close()
                hash = hasher.hexdigest()
                set1.append((hash,fullpath))

for i in range(len(dir2)):
    for root,dir,fname in os.walk(dir2[i]):
        for file in fname:
            fullpath = os.path.join(root, file)
            size = os.path.getsize(fullpath)
            if size > MAX_SIZE:
                afile = open(fullpath, 'rb')
                hasher = md5()
                buf = afile.read(65536)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = afile.read(65536)
                afile.close()
                hash = hasher.hexdigest()
                set2.append((hash,fullpath))


print("No of Files in Set1: ",len(set1),'\n')
print("No of Files in Set2: ",len(set2),'\n')

uniq = []

for i in range(len(set1)):
    uniq.append(set1[i][0])

uniq =set(uniq)

a = 1
c = 0

for i in uniq:
    print("Set: "+ str(a))
    for j in range(len(set1)):
        if i == set1[j][0]:
            print("Orig File: ", set1[j][0], set1[j][1])
    for k in range(len(set2)):
        if i == set2[k][0]:
            #os.remove(set2[k][1])
            c += 1
            print("Removed: ", set2[k][0], set2[k][1])
    print('\n')
    a += 1

print("No of Files Deleted: ", c)
