
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
        tempFile.write( line.replace( textToSearch, textToReplace ) )
        #tempFile.write( line.replace( textToSearch2, textToReplace2 ) )
    
    
    for line in fileinput.input(fileToSearch):
        tempFile.write( line.replace( textToSearch2, textToReplace2 ) )
    tempFile.close()
    input( '\n\n Press Enter to exit...' )
    
fileName = input("please enter your file name")
reaplaceFile(fileName)