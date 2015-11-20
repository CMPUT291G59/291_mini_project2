import sys 
import os
import csv
import datetime
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
            elif c==9:
                print(title[c]+e+"\n")
            else:
                print(title[c]+e)
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
    return alist


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
    return alist

def searchAllCamera():
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
    return alist

def searchIniralCam():
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
    return blist

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
    return alist


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
    return blist 


def priceChecker(alist):
    blist=[]
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
    reviewDB.close()
    return blist
def dateChecker(alist):
    blist=[]
    filename1 = 'rw.idx'
    reviewDB = db.DB()
    reviewDB.open(filename1, None, db.DB_HASH, db.DB_CREATE)
    for i in alist:
        result=reviewDB.get(i)
        result=result.decode("utf-8")
        for a in csv.reader([result],skipinitialspace=True):
            st = datetime.datetime.fromtimestamp(int(a[7])).strftime('%Y/%m/%d')
            if datetime.datetime.strptime(st,'%Y/%m/%d')>datetime.datetime.strptime("2007/06/20",'%Y/%m/%d'):
                a[7]=a[7]+"    "+st
                blist.append(a)
    reviewDB.close()
    return blist


def dateCheckerWithPrice(alist):
    blist=[]
    filename1 = 'rw.idx'
    reviewDB = db.DB()
    reviewDB.open(filename1, None, db.DB_HASH, db.DB_CREATE)
    for i in alist:
        result=reviewDB.get(i)
        result=result.decode("utf-8")
        for a in csv.reader([result],skipinitialspace=True):
            st = datetime.datetime.fromtimestamp(int(a[7])).strftime('%Y/%m/%d')
            if datetime.datetime.strptime(st,'%Y/%m/%d')>datetime.datetime.strptime("2007/06/20",'%Y/%m/%d'):
                if "unknow" not in a[2]:
                    if 20.0<float(a[2])<60.0:               
                        a[7]=a[7]+"    "+st
                        blist.append(a)
    reviewDB.close()
    return blist


a = input("please enter your query>>>")
a = a.split()
print(a)
if len(a)==1:
    if ":" in a[0]:
        c = a[0].split(":")
        print(c)