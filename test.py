from bsddb3 import db
filename = 'rw.idx'
reviewDB = db.DB()
reviewDB.open(filename, None, db.DB_HASH, db.DB_CREATE)
cursor = reviewDB.cursor()
rec = cursor.first()
print(len(reviewDB))
#while rec:
        #print (rec)
        #rec = cursor.next()
reviewDB.close()