# written by Di Meng 
# this python makes the scores.txt form original txt file
import sys 
import os
import fileinput
import replaceFile
import re
fileName = input("please enter your file name ")
replaceFile.replaceFile(fileName)
tempFile=open('scores.txt','w+')
scoreList = []
alist=replaceFile.makeList(fileName)
for k,i in enumerate(alist):
    print(i[6])
    tempFile.write(str(i[6])+","+str(k+1)+"\n")
tempFile.close()
