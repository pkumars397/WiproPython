line="-------------------------------------------------------"

print(line)

f=open("pk2.txt","r")

for i in f:
   name,age=i.split(" ")
   print("Name: ",name)
   print("Age: ",age)
   print(line)
f.close()