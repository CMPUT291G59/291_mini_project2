
import os
import sys
import fileinput

def reaplaceFile(fileToSearch):
    textToSearch = "\"" 
    textToReplace ="&quot;"
    
    
    textToSearch2 = "\\" 
    textToReplace2 ="\\\\"
    
    
    
    tempFile = open( fileToSearch, 'r+' )
    
    
    
    for line in fileinput.input( fileToSearch ):
        line.replace( textToSearch, textToReplace )
        #tempFile.write()
        #tempFile.write( line.replace( textToSearch2, textToReplace2 ) )

    for line in fileinput.input(fileToSearch):
        tempFile.write( line.replace( textToSearch2, textToReplace2 ) )
    tempFile.close()
    input( '\n\n Press Enter to exit...' )
    
fileName = input("please enter your file name")
reaplaceFile(fileName)


alist = ["product/productId:","product/title:","product/price:","review/userId:","review/profileName:",
         "review/helpfulness:","review/score:","review/time:","review/summary:","review/text:"]
