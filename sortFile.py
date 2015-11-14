from subprocess import Popen, PIPE

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


