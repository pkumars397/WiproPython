f=open("pk2.txt","w") #writing mode
#read name,age of 3 people

for i in range(3):
  name=input("Enter the name:")
  age=input("enter the age:")
  f.write(name + " "+age)
  f.write("\n")
f.close()