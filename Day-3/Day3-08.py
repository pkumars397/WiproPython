f=open("studMarks.txt","w")
for i in range(3):
    name=input("enter the name:")
    mark1=input("enter mark1")
    mark2=input("enter the mark2:")
    f.write(name+" "+mark1+" "+mark2)
    f.write("\n")
f.close()
