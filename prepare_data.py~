import sys 
import os
import fileinput
import re
def replaceFile(fileToSearch):
    textToSearch = "\"" 
    textToReplace ="&quot;"
    textToSearch2 = "\\" 
    textToReplace2 ="\\\\"
    tempFile = open( fileToSearch, 'r+' )
    for line in fileinput.input( fileToSearch ):
        tempFile.write( line.replace( textToSearch, textToReplace ) )
        #tempFile.write( line.replace( textToSearch2, textToReplace2 ) )
    tempFile.close()
    tempFile = open( fileToSearch, 'r+' )
    for line in fileinput.input(fileToSearch):
        tempFile.write( line.replace( textToSearch2, textToReplace2 ) )
    tempFile.close()
    
def makeList(fileName):

    alist = ["product/productId:","product/title:","product/price:","review/userId:","review/profileName:",
             "review/helpfulness:","review/score:","review/time:","review/summary:","review/text:"]
    tempFile = open( fileName, 'r+' )
    i = 0
    blist = []
    clist = []
    
    for line in fileinput.input( fileName ):
        if line.strip() != '':
            for k in alist:
                if k in line:
                    if k == "product/title:" or k == "review/profileName:" or k == "review/summary:" or k == "review/text:":
                        line = "".join(line.rsplit(k))
                        line = line[1:-1] 
                        line  = "\"" + line +"\""
                        blist.append(line)
                    else:               
                        line = "".join(line.rsplit(k))
                        line = line[1:-1]
                        
                        blist.append(line)
                        
        else:
            clist.append(blist)
            blist = []
    
    tempFile.close()
    return clist

def makeReview(fileName):
    tempFile=open('reviews.txt','w+')
    
    alist=makeList(fileName)
    for i,a in enumerate(alist):
        if i==0:
            tempFile.write(str(i+1))
        else:
            tempFile.write("\n"+str(i+1))
        for b in a:
            tempFile.write(","+b)
            i=i+1
    tempFile.close()






def makePterm(fileName):
    tempFile=open('pterms.txt','w+')
    blist=[]
    clist=[]
    alist=makeList(fileName)
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
    for b in blist:
        b=" ".join(b)
        b=re.sub('\W+',' ',b)
        clist.append(b)
    
    for i,c in enumerate(clist):
        c=c.split()
        for c1 in c:
            if len(c1)>=3:
                tempFile.write(c1.lower()+","+str(i+1)+"\n")
    tempFile.close() 
    


    
    
    
def makeRterm(fileName):
    tempFile=open('rterms.txt','w+')
    blist=[]
    clist=[]
    alist=makeList(fileName)
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
    for i,c in enumerate(clist):
        c=c.split()
        for c1 in c:
            if len(c1)>=3:
                tempFile.write(c1.lower()+","+str(i+1)+"\n")
    tempFile.close()












def makeScore(fileName):
    tempFile=open('scores.txt','w+')
    alist=makeList(fileName)
    for k,i in enumerate(alist):
        tempFile.write(str(i[6])+", "+str(k+1)+"\n")
    tempFile.close()



fileName = input("please enter your file name ")    
replaceFile(fileName)
makeReview(fileName)
makePterm(fileName)
makeRterm(fileName)
makeScore(fileName)
print("Your files are created!")
