import time
from subprocess import Popen, PIPE
#using linux command and run under python program
#this fuction is able to sort the file and git rid of duplications.
start_time = time.time()
p = Popen('sort -u -o pterms.txt pterms.txt', shell=True,
          stdout=PIPE, stderr=PIPE)
out, err = p.communicate()
p1 = Popen('sort -u -o rterms.txt rterms.txt', shell=True,
          stdout=PIPE, stderr=PIPE)
out, err = p1.communicate()
p2 = Popen('sort -n -o scores.txt scores.txt', shell=True,
          stdout=PIPE, stderr=PIPE)
out, err = p2.communicate()
print("Your file is sorted!")
print("It cost %s seconds" % (time.time() - start_time))

