import sys 
import os
import fileinput
import re
import time
def replace_word(infile,old_word,new_word):
    if not os.path.isfile(infile):
        print ("Error on replace_word, not a regular file: "+infile)
        sys.exit(1)

    f1=open(infile,'r').read()
    f2=open(infile,'w')
    m=f1.replace(old_word,new_word)
    f2.write(m)
    
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

def makeReview(alist):
    tempFile=open('reviews.txt','w+')
    for i,a in enumerate(alist):
        if i==0:
            tempFile.write(str(i+1))
        else:
            tempFile.write("\n"+str(i+1))
        for b in a:
            tempFile.write(","+b)
            i=i+1
    tempFile.close()

def makePterm(alist):
    tempFile=open('pterms.txt','w+')
    blist=[]
    clist=[]
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
           
def makeRterm(alist):
    tempFile=open('rterms.txt','w+')
    blist=[]
    clist=[]
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

def makeScore(alist):
    tempFile=open('scores.txt','w+')
    for k,i in enumerate(alist):
        tempFile.write(str(i[6])+","+str(k+1)+"\n")
    tempFile.close()
#ask user for input
fileName = input("please enter your file name ") 
#starting the time 
start_time = time.time()
#replace the character
replace_word(fileName,"\"" ,"&quot;")
replace_word(fileName,"\\","\\\\")
#go through file and store them into a list
alist=makeList(fileName)
#convert list in file again with proper formate
makeReview(alist)
#convert list in file again with pterm infor proper formate
makePterm(alist)
#convert list in file again with rterm infor proper formate
makeRterm(alist)
#convert list in file again with score infor proper formate
makeScore(alist)
print("Your files are created!")
#caculate the time
print("It cost %s seconds" % (time.time() - start_time))