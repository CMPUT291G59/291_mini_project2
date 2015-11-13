import sys
import os 
import fileinput
import replaceFile
fileName = input("please enter your file name ")
replaceFile.replaceFile(fileName)
tempFile=open( fileName, 'r+' )
#tempFile1=open('reviews.txt','w+')
i=1
alist=[]
for line in fileinput.input( fileName):
    alist.append(line.replace( "product/productId: ",""))
    if line.strip()=="":
        i=i+1
for line in alist:
    print(line)
print(len(alist))
        
tempFile.close()    
#tempFile1.close()