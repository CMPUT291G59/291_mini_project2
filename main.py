import sys 
import os
import csv
import datetime
import time
from bsddb3 import db
#this fuction is to found the intersect in two list
def inter(a,b):
    c = [set(a)&set(b)]
    return c
#this fuction is able to find intersect in mutiple list
def MultiInter(a):
   
    if len(a)==0:
        return "there is no matching data"
    elif len(a)==1:
        return list(a[0])
    while len(a)>1:
        r = inter(a[0],a[1])
        a[0:2] = r
    return list(a[0])

#this fucttion is able to check input and identify the input 
def checkInput(b):
    start_time=time.time()
    a=b.split()
    clist=[]
    #check input if there ">" or "<" in a list it will join the term
    while "<" in a :
        i = a.index("<")
        a[(i-1):(i+2)] = ["".join(a[(i-1):(i+2)])]
    while ">" in a :
        i = a.index(">")
        a[(i-1):(i+2)] = ["".join(a[(i-1):(i+2)])]
    for i,c in enumerate(a):
        if len(a)!= 1:
            if c[-1] == "<" or c[-1] == ">":
                a[i:i+2]=["".join(a[i:i+2])]   
            elif c[0] == "<" or c[0] == ">":
                a[i-1:i+1]=["".join(a[i-1:i+1])]   
    #go through every element in the list and find special cheracter to identify them
    for i in a:
        #when there is ":" in a string 
        if ":" in i:
            c=i.split(":")
            if c[0]=="p":
                if "%" in c[1]:
                    x=True
                    c[1]=c[1][0:-1]
                    result=searchInitial(x,c[1])
                    clist.append(result)
                else:
                    x=True
                    result=searchterm(x,c[1])
                    clist.append(result)
            elif c[0]=="r":
                if "%" in c[1]:
                    x=False
                    c[1]=c[1][0:-1]
                    result=searchInitial(x,c[1])
                    clist.append(result) 
                else:
                    x=False
                    result=searchterm(x,c[1])
                    clist.append(result)
            else:
                b=input("Your enter is invalid! Please try enter again! ")
                checkInput(b)
        #this is check that if srting is only contain characters
        elif i.isalpha()==True:
            result=searchAllTerm(i)
            clist.append(result)
        #check if the string contain "%"
        elif '%' in i:
            i=i[0:-1]
            result=searchInitialAll(i)
            clist.append(result)
        #if string contain "rscore" it will identify them.
        elif "rscore" in i:
            #check if ">" or "<" in the string and perform different operation 
            if ">" in i:
                c=i.split(">")
                c[1]=float(c[1])
                a=True
                result=findScore(a,c[1])
                clist.append(result)
            elif "<" in i:
                c=i.split("<")
                c[1]=float(c[1])
                a=False                
                result=findScore(a,c[1])
                clist.append(result)
            else:
                b=input("Your enter is invalid! Please try enter again! ")
                checkInput(b)
        #if string contain "pprice" it will identify them and go to the price function.        
        elif "pprice" in i:
            if ">" in i:
                c=i.split(">")
                c[1]=float(c[1])
                a=True
                result=priceChecker(a,c[1])
                clist.append(result)
            elif "<" in i:
                c=i.split("<")
                c[1]=float(c[1])
                a=False                
                result=priceChecker(a,c[1]) 
                clist.append(result)
            else:
                b=input("Your enter is invalid! Please try enter again! ")
                checkInput(b)
        #if string contain "rdate" it will identify them and go to the date function.  
        elif "rdate" in i:
            if ">" in i:
                c=i.split(">")
                a=True
                result=dateChecker(a,c[1])
                clist.append(result)
            elif "<" in i:
                c=i.split("<")
                a=False
                result=dateChecker(a,c[1])
                clist.append(result)
            else:
                b=input("Your enter is invalid! Please try enter again! ")
                checkInput(b)
    #append all result into a list and go to MultiInter fuction will return the result satisify all condition that user inputed            
    a = MultiInter(clist)
    #the list contain index of the result and use fullReviewChecker to convert index into actual output
    alist=fullReviewChecker(a)
    #after this step it will be the processing time
    proce_time=time.time() - start_time
    #now the index is already convert to actual data into a list and printResult will match infor stored in the list with proper title 
    printResult(alist)
    #print(len(a))
    print("it cost %s seconds to process," %(proce_time), "total cost %s seconds "% (time.time()-start_time))
    #b=[]
    #for i in a:
        #i=int(i.decode("utf-8"))
        #b.append(i)
    
    #print(sorted(b))
        
            
def fullReviewChecker(alist):
    blist=[]
    filename1 = 'rw.idx'
    reviewDB = db.DB()
    reviewDB.open(filename1, None, db.DB_HASH, db.DB_CREATE)
    for i in alist:
        result=reviewDB.get(i)
        result=result.decode("utf-8")
        for a in csv.reader([result],skipinitialspace=True):
            blist.append(a) 
    reviewDB.close()
    return blist

def printResult(alist):
    title = ["product/productId:","product/title:","product/price:","review/userId:","review/profileName:",
             "review/helpfulness:","review/score:","review/time:","review/summary:","review/text:"]
    for b,i in enumerate(alist):
        for c,e in enumerate(i):
            if c==0:
                print(str(b+1)+"\n"+title[c]+e)
            elif c==7:
                st=datetime.datetime.fromtimestamp(int(e)).strftime('%Y/%m/%d')
                print(title[c]+e+"    "+st)
            elif c==9:
                print(title[c]+e+"\n")
            else:
                print(title[c]+e)
    print("You find",len(alist),"matches in the result")
    
    
def searchterm(x,a):
    alist=[]
    if x==True:
        filename= 'pt.idx'
    elif x==False:
        filename = 'rt.idx'    
    termDB = db.DB()
    termDB.open(filename, None, db.DB_BTREE, db.DB_CREATE)
    cursor =termDB.cursor()
    rec = cursor.first()
    while rec:
        key, value =rec
        key1=key.decode("utf-8")
        if a == key1:
            alist.append(value)
        rec = cursor.next()
    termDB.close()
    return alist

def searchAllTerm(a):
    alist=[]
    filename = 'pt.idx'
    ptermDB = db.DB()
    ptermDB.open(filename, None, db.DB_BTREE, db.DB_CREATE)
    cursor = ptermDB.cursor()
    rec = cursor.first()
    #print(len(ptermDB))
    while rec:
        key, value =rec
        key1=key.decode("utf-8")
        if a == key1:
            alist.append(value)
        rec = cursor.next()
    ptermDB.close()
    filename1 = 'rt.idx'
    rtermDB = db.DB()
    rtermDB.open(filename1, None, db.DB_BTREE, db.DB_CREATE)
    cursor = rtermDB.cursor()
    rec1 = cursor.first()
    while rec1:
        key, value =rec1
        key1=key.decode("utf-8")
        if a == key1:
            alist.append(value)
        rec1 = cursor.next()
    rtermDB.close()
    alist=list(set(alist))
    return alist

def searchInitial(x,a):
    alist=[]
    if x==True:
        filename= 'pt.idx'
    elif x==False:
        filename = 'rt.idx'
    ptermDB = db.DB()
    ptermDB.open(filename, None, db.DB_BTREE, db.DB_CREATE)
    cursor = ptermDB.cursor()
    rec = cursor.first()
    #print(len(ptermDB))
    while rec:
        key, value =rec
        key1=key.decode("utf-8")
        if a== key1[0:len(a)]:
            alist.append(value)
        rec = cursor.next()
    ptermDB.close()  
    alist=list(set(alist))
    return alist    
def searchInitialAll(a):
    alist=[]
    filename = 'pt.idx'
    ptermDB = db.DB()
    ptermDB.open(filename, None, db.DB_BTREE, db.DB_CREATE)
    cursor = ptermDB.cursor()
    rec = cursor.first()
    #print(len(ptermDB))
    while rec:
        key, value =rec
        key1=key.decode("utf-8")
        if a== key1[0:len(a)]:
            alist.append(value)
        rec = cursor.next()
    ptermDB.close()
    #check camera in rterm
    filename1 = 'rt.idx'
    rtermDB = db.DB()
    rtermDB.open(filename1, None, db.DB_BTREE, db.DB_CREATE)
    cursor = rtermDB.cursor()
    rec1 = cursor.first()
    #print(len(rtermDB))
    while rec1:
        key, value =rec1
        key1=key.decode("utf-8")
        #print(key1[0:])
        if a == key1[0:len(a)]:
            alist.append(value)
        rec1 = cursor.next()
    rtermDB.close()
    alist=list(set(alist))
    return alist

def findScore(a,b):
    alist=[]
    filename = 'sc.idx'
    scoreDB = db.DB()
    scoreDB.open(filename, None, db.DB_BTREE, db.DB_CREATE)
    cursor = scoreDB.cursor()
    rec = cursor.first()
    while rec:
        key, value =rec
        key1=key.decode("utf-8")
        key1=float(key1)
        if key1>b and a==True:
            alist.append(value)
        elif key1<b and a==False:
            alist.append(value)
        rec = cursor.next()
    scoreDB.close()
    return alist
def priceChecker(x,b):
    blist=[]
    filename1 = 'rw.idx'
    reviewDB = db.DB()
    reviewDB.open(filename1, None, db.DB_HASH, db.DB_CREATE)
    cursor = reviewDB.cursor()
    rec = cursor.first() 
    while rec:
        key, value =rec
        value=value.decode("utf-8")
        for a in csv.reader([value],skipinitialspace=True):
            if "unknow" not in a[2]:
                if float(a[2])>b and x==True:
                    blist.append(key)
                elif float(a[2])<b and x==False:
                    blist.append(key)
            rec = cursor.next()
    reviewDB.close()
    return blist
def dateChecker(x,b):
    blist=[]
    filename1 = 'rw.idx'
    reviewDB = db.DB()
    reviewDB.open(filename1, None, db.DB_HASH, db.DB_CREATE)
    cursor = reviewDB.cursor()
    rec = cursor.first() 
    while rec:
        key, value =rec
        value=value.decode("utf-8")
        for a in csv.reader([value],skipinitialspace=True):
            st = datetime.datetime.fromtimestamp(int(a[7])).strftime('%Y/%m/%d')
            if datetime.datetime.strptime(st,'%Y/%m/%d')>datetime.datetime.strptime(b,'%Y/%m/%d')and x==True:
                a[7]=a[7]+"    "+st
                blist.append(key)
            if datetime.datetime.strptime(st,'%Y/%m/%d')<datetime.datetime.strptime(b,'%Y/%m/%d')and x==False:
                a[7]=a[7]+"    "+st
                blist.append(key)
            rec = cursor.next()
    reviewDB.close()
    return blist    

print("Welcome to W&M database management system!")
input1=input("Enter your input or press 'q' to quite\n")
input1=input1.lower()
while input1!="q":
    try:
        checkInput(input1)
        input1=input("Enter your input or press 'q' to quite\n")
        input1=input1.lower()
        if input1=="q":
            break
    except TypeError: 
        input1=input("Your enter is invalid! Please try enter again! ")
print("Thank you for using our system!")
