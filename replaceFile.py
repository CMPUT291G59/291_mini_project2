
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
