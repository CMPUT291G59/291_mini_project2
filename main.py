import sys 
import os
from bsddb3 import db
def searchCamera():
    alist=[]
    filename = 'pt.idx'
    ptermDB = db.DB()
    ptermDB.open(filename, None, db.DB_BTREE, db.DB_CREATE)
    cursor = ptermDB.cursor()
    rec = cursor.first()
    print(len(ptermDB))
    while rec:
        key, value =rec
        key1=key.decode("utf-8")
        if "camera" in key1:
            alist.append(value)
        rec = cursor.next()
    ptermDB.close()
    filename1 = 'rw.idx'
    reviewDB = db.DB()
    reviewDB.open(filename1, None, db.DB_HASH, db.DB_CREATE)
    for i in alist:
        result=reviewDB.get(i)
        result=result.decode("utf-8")
        print(result)
def searchGreat():
    alist=[]
    filename = 'rt.idx'
    ptermDB = db.DB()
    ptermDB.open(filename, None, db.DB_BTREE, db.DB_CREATE)
    cursor = ptermDB.cursor()
    rec = cursor.first()
    print(len(ptermDB))
    while rec:
        key, value =rec
        key1=key.decode("utf-8")
        if "great" in key1:
            alist.append(value)
        rec = cursor.next()
    ptermDB.close()
    filename1 = 'rw.idx'
    reviewDB = db.DB()
    reviewDB.open(filename1, None, db.DB_HASH, db.DB_CREATE)
    u=0
    print(len(alist))
    for i in alist:
        result=reviewDB.get(i)
        result=result.decode("utf-8")
        u=u+1
        print(result)
    print(u)
a=["1","2","3","4","5","6","7","8","9","10","Q","q"]
print("Welcome to W&M database management system!")
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
print("Press <Q>or <q> to quit the system!")
b=input("Enter a number to choose above operation> ")
while b not in a:
    b=input("Invalid enter!> ")
print(b)
if b=="q" or b=="Q":
    print("Thank you for using our system!")
elif b=="1":
    searchCamera()
elif b=="2":
    searchGreat()
#elif b=="3":
    
#elif b=="4":
    
#elif b=="5":
    
#elif b=="6":
    
#elif b=="7":
    
#elif b=="8":
    
#elif b=="9":
    
#elif b=="10":   