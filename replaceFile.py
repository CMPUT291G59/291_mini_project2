
import os
import sys
import fileinput

def replaceFile(fileToSearch):
    textToSearch = "\"" 
    textToReplace ="&quot;"
    
    
    textToSearch2 = "\\" 
    textToReplace2 ="\\\\"
    
    
    
    tempFile = open( fileToSearch, 'r+' )
    
    for line in fileinput.input( fileToSearch ):
        tempFile.write( line.replace( textToSearch, textToReplace ) )
        #tempFile.write( line.replace( textToSearch2, textToReplace2 ) )
    tempFile.close()
    tempFile = open( fileToSearch, 'r+' )
    for line in fileinput.input(fileToSearch):
        tempFile.write( line.replace( textToSearch2, textToReplace2 ) )
    tempFile.close()
    
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
