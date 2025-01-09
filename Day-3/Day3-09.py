line="---------------------------------"
print(line)
d=open("studMarks.txt")
for detail in d:
    name,mark1,mark2=detail.split(" ")
    total=int(mark1)+int(mark2)
    print("Name :",name)
    print("mark1: ",mark1)
    print("mark2: ",mark2)
    print("Total: ",total)
    print(line)
d.close()