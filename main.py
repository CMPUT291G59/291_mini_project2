import sys 
import os
import csv
from bsddb3 import db
def printScreen():
    print("1. p:camera")
    print("2. r:great")
    print("3. camera")
    print("4. cam%")
    print("5. r:great cam%")
    print("6. rscore > 4")
    print("7. camera rscore < 3")
    print("8. pprice < 60 camera")
    print("9. camera rdate > 2007/06/20")
    print("10. camera rdate > 2007/06/20 pprice > 20 pprice < 60")
    print("Press <q> to quit the system!")
    
def printResult(alist):
    blist=[]
    title = ["product/productId:","product/title:","product/price:","review/userId:","review/profileName:",
             "review/helpfulness:","review/score:","review/time:","review/summary:","review/text:"]
    filename1 = 'rw.idx'
    reviewDB = db.DB()
    reviewDB.open(filename1, None, db.DB_HASH, db.DB_CREATE)
    for i in alist:
        result=reviewDB.get(i)
        result=result.decode("utf-8")
        for a in csv.reader([result],skipinitialspace=True):
            blist.append(a)
    for b,i in enumerate(blist):
        for c,e in enumerate(i):
            if c==0:
                print(str(b+1)+"\n"+title[c]+e)
            elif c==9:
                print(title[c]+e+"\n")
            else:
                print(title[c]+e)
    reviewDB.close()
    print("You find",len(alist),"matches in the result")
def searchCamera():
    alist=[]
    filename = 'pt.idx'
    ptermDB = db.DB()
    ptermDB.open(filename, None, db.DB_BTREE, db.DB_CREATE)
    cursor = ptermDB.cursor()
    rec = cursor.first()
    while rec:
        key, value =rec
        key1=key.decode("utf-8")
        if "camera" in key1:
            alist.append(value)
        rec = cursor.next()
    ptermDB.close()
    printResult(alist)
def searchGreat():
    alist=[]
    filename = 'rt.idx'
    rtermDB = db.DB()
    rtermDB.open(filename, None, db.DB_BTREE, db.DB_CREATE)
    cursor = rtermDB.cursor()
    rec = cursor.first()
    while rec:
        key, value =rec
        key1=key.decode("utf-8")
        if "great" in key1:
            alist.append(value)
        rec = cursor.next()
    rtermDB.close()
    printResult(alist)
def searchAllCamera(a):
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
        if "camera" in key1:
            alist.append(value)
        rec = cursor.next()
    ptermDB.close()
    #print("sssss",len(alist))
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
        if "camera" in key1:
            alist.append(value)
        rec1 = cursor.next()
    rtermDB.close()
    #print(alist)
    #print(len(alist))
    alist=list(set(alist))
    if a=="3":
        printResult(alist)
    else:
        return alist
def searchIniralCam(a):
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
        if "cam" == key1[0:3]:
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
        if "cam" == key1[0:3]:
            alist.append(value)
        rec1 = cursor.next()
    rtermDB.close()
    alist=list(set(alist))
    if a=="4":
        printResult(alist)  
    else:
        return alist
def findGreatCam(alist):
    blist=[]
    filename = 'rt.idx'
    rtermDB = db.DB()
    rtermDB.open(filename, None, db.DB_BTREE, db.DB_CREATE) 
    cursor = rtermDB.cursor()
    rec = cursor.first()
    #print(len(rtermDB))
    while rec:
        key, value =rec
        key1=key.decode("utf-8")
        if "great" in key1 and value in alist:
            blist.append(value)
        rec = cursor.next()
    rtermDB.close()
    printResult(blist)
def findScore():
    alist=[]
    filename = 'sc.idx'
    scoreDB = db.DB()
    scoreDB.open(filename, None, db.DB_BTREE, db.DB_CREATE)
    cursor = scoreDB.cursor()
    rec = cursor.first()
    print(len(scoreDB))
    while rec:
        key, value =rec
        key1=key.decode("utf-8")
        key1=float(key1)
        if key1>4.0:
            alist.append(value)
        rec = cursor.next()
    scoreDB.close()
    printResult(alist)
def findLess3(alist):
    blist=[]
    filename = 'sc.idx'
    scoreDB = db.DB()
    scoreDB.open(filename, None, db.DB_BTREE, db.DB_CREATE) 
    cursor = scoreDB.cursor()
    rec = cursor.first()
    #print(len(scoreDB))
    while rec:
        key, value =rec
        key1=key.decode("utf-8")
        key1=float(key1)
        if key1<3.0 and value in alist:
            blist.append(value)
        rec = cursor.next()
    scoreDB.close()
    printResult(blist) 
def priceChecker(alist):
    blist=[]
    title = ["product/productId:","product/title:","product/price:","review/userId:","review/profileName:",
                 "review/helpfulness:","review/score:","review/time:","review/summary:","review/text:"]
    filename1 = 'rw.idx'
    reviewDB = db.DB()
    reviewDB.open(filename1, None, db.DB_HASH, db.DB_CREATE)
    for i in alist:
        result=reviewDB.get(i)
        result=result.decode("utf-8")
        for a in csv.reader([result],skipinitialspace=True):
            if "unknow" not in a[2]:
                if float(a[2])<60.0:
                    blist.append(a)
    for b,i in enumerate(blist):
        for c,e in enumerate(i):
            if c==0:
                print(str(b+1)+"\n"+title[c]+e)
            elif c==9:
                print(title[c]+e+"\n")
            else:
                print(title[c]+e)
    reviewDB.close()    
    print("You find",len(blist),"matches in the result")
a=["1","2","3","4","5","6","7","8","9","10","Q","q"]
print("Welcome to W&M database management system!")
printScreen()
b=input("Enter a number to choose above operation> ")    
while b not in a:
    b=input("Invalid enter!> ")
while(b !="q" or b!="Q"):
    if b=="1":
        searchCamera()
    elif b=="2":
        searchGreat()
    elif b=="3":
        searchAllCamera(b)
    elif b=="4":
        searchIniralCam(b)
    elif b=="5":
        alist=searchIniralCam(b)
        findGreatCam(alist)
    elif b=="6":
        findScore()
    elif b=="7":
        alist=searchAllCamera(b)
        findLess3(alist)
    elif b=="8":
        alist=searchAllCamera(b)
        priceChecker(alist)
    #elif b=="9":
        
    #elif b=="10":
    b=input("Press <anykey> to back main menu OR <q> to quit the system!")
    if b=="q" or b=="Q":
        break
    else:
        printScreen()
        b=input("Enter a number to choose above operation> ")
    while b not in a:
        b=input("Invalid enter!> ")    
print("Thank you for using our system!")