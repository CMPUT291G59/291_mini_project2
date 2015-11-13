import sys 
import os
import fileinput
import replaceFile
import re
fileName = input("please enter your file name ")
replaceFile.replaceFile(fileName)
tempFile=open('rterms.txt','w+')
blist=[]
clist=[]
alist=replaceFile.makeList(fileName)
for i, a in enumerate(alist):
    c = a[8].split()
    c1=a[9].split()
    if c[0][0]=="\"" or c[-1][-1]=="\"":
        #line = "".join(line.rsplit(k))
        tep = c[0]
        tep = tep[1:]
        c[0] = tep
        tep1 = c[-1]
        tep1 = tep1[:-1]
        c[-1] = tep1
    if c1[0][0]=="\"" or c1[-1][-1]=="\"":
        #line = "".join(line.rsplit(k))
        tep = c1[0]
        tep = tep[1:]
        c1[0] = tep
        tep1 = c1[-1]
        tep1 = tep1[:-1]
        c1[-1] = tep1
    blist.append(c+c1)
for b in blist:
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