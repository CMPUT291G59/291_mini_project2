import os
from subprocess import Popen, PIPE

p = Popen('db_load -T -t hash -f reviewIdx.txt rw.idx ', shell=True,
          stdout=PIPE, stderr=PIPE)
out, err = p.communicate()

p1 = Popen('db_load -T -t btree -f ptermIdx.txt pt.idx ', shell=True,
          stdout=PIPE, stderr=PIPE)
out, err = p1.communicate()

p2 = Popen('db_load -T -t btree -f rtermIdx.txt rt.idx ', shell=True,
          stdout=PIPE, stderr=PIPE)
out, err = p2.communicate()

p3 = Popen('db_load -T -t btree -f scoreIdx.txt sc.idx ', shell=True,
          stdout=PIPE, stderr=PIPE)
out, err = p3.communicate()
print("Your index files are created!")
a=input("press 'd' to delete temp txt index file! ")
if a=="d":
    os.remove("reviewIdx.txt")
    os.remove("ptermIdx.txt")
    os.remove("rtermIdx.txt")
    os.remove("scoreIdx.txt")