# readLine() reads one line at a time
# read(x)    reads x bytes from the file
#===============================================================================================
    
f=open("doss2.txt")
print(f.readline())  # reads one line at time
print(f.readline()) 
f.close()

#================================================================================================
f=open("doss2.txt")
print(f.read(7))  # reads 5 bytes  from the file 
f.close()
