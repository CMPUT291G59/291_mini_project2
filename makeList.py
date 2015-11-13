import os
import sys
import fileinput


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
                        line = line[0:-1]
                        
                        blist.append(line)
                        
        else:
            clist.append(blist)
            blist = []
    
    tempFile.close()
    return clist

#c = makeList("10.txt")
#for i in c:
    #print(i)    

