def inputList():
    a = input("please enter your query>>>")
    a = a.lower()
    a = a.split()
    print(a)
    i = a.index("<")
    
    while "<" in a :
        i = a.index("<")
        a[(i-1):(i+2)] = ["".join(a[(i-1):(i+2)])]
        
    
    while ">" in a :
        i = a.index(">")
        a[(i-1):(i+2)] = ["".join(a[(i-1):(i+2)])]
    return a

#a = inputList()
#print(a)

