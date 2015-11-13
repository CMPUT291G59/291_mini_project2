import sys
import os 
import fileinput
import replaceFile
fileName = input("please enter your file name ")
replaceFile.replaceFile(fileName)
tempFile=open('reviews.txt','w+')

alist=replaceFile.makeList(fileName)
for i,a in enumerate(alist):
    if i==0:
        tempFile.write(str(i+1))
    else:
        tempFile.write("\n"+str(i+1))
    for b in a:
        tempFile.write(","+b)
        i=i+1
tempFile.close()