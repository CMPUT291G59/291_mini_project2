import sys 
import os
import fileinput
import re
import time
#this program is replace the break.pl file that instructor provide. And same fuctaion which is convert the format for DB_load
def makeReviewIndex(fileName,fileName1):
    tempFile=open(fileName1,'w+')
    file=open(fileName,'r') 
    for line in fileinput.input(fileName):
            c=line.split(',')
            tempFile.write(str(c[0])+"\n")
            stringList = c[1:]
            stringList = ",".join(stringList)
            tempFile.write(str(stringList))
    tempFile.write("\n")
    tempFile.close()
    file.close()    

def makeIndex(fileName,fileName1):
    tempFile=open(fileName1,'w+')
    file=open(fileName,'r')
    for line in fileinput.input(fileName):
        c=line.split(',')
        for i in c:
            if '\n' in i:
                tempFile.write(str(i))
            else:
                tempFile.write(str(i)+'\n')
    tempFile.close()
    file.close()
    
start_time = time.time()    
makeReviewIndex("reviews.txt","reviewIdx.txt")
makeIndex("pterms.txt","ptermIdx.txt")
makeIndex("rterms.txt","rtermIdx.txt")
makeIndex("scores.txt","scoreIdx.txt")
print("Your file is formated for db_load!")
print("It cost %s seconds" % (time.time() - start_time))