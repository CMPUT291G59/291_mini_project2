import sys 
import os
import fileinput
import replaceFile
import re
fileName = input("please enter your file name ")
replaceFile.replaceFile(fileName)
tempFile=open('pterms.txt','w+')
blist=[]
clist=[]
alist=replaceFile.makeList(fileName)
for i, a in enumerate(alist):
    c = a[1].split()
    if c[0][0]=="\"" or c[-1][-1]=="\"":
        #line = "".join(line.rsplit(k))
        tep = c[0]
        tep = tep[1:]
        c[0] = tep
        tep1 = c[-1]
        tep1 = tep1[:-1]
        c[-1] = tep1
    blist.append(c)
for i,b in enumerate(blist):
    b=" ".join(b)
    b=re.sub('\W+',' ',b)
    clist.append(b)
print(clist)

for i,c in enumerate(clist):
    c=c.split()
    for c1 in c:
        if len(c1)>=3:
            tempFile.write(c1.lower()+","+str(i+1)+"\n")
tempFile.close()