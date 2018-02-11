#!/usr/bin/env python3

import os
from hashlib import md5
import collections

dirs = ["/media/system/Data/",
        "/data/.move/",
        "/data/.folder/"]

x,y,z = [],[],[]

for i in range(len(dirs)):
    for root,dir,fname in os.walk(dirs[i]):
        for file in fname:
            fullpath = os.path.join(root, file)
            size = os.path.getsize(fullpath)
            if size > 2097152:
                afile = open(fullpath, 'rb')
                hasher = md5()
                buf = afile.read(65536)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = afile.read(65536)
                afile.close()
                hash = hasher.hexdigest()
                x.append(fullpath)
                y.append(hash)

a = 1
b = [item for item, count in collections.Counter(y).items() if count > 1]

for i in range(len(b)):
    print("Duplicate Set: "+ str(a))
    a += 1
    c = 0
    for j in range(len(y)):
        if b[i] == y[j]:
            if c == 0:
                print("Original File: "+ x[j])
                c += 1
            else:
                #os.remove(x[j])
                print("Duplicate file: "+ x[j])
