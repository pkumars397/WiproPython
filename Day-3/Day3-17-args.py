import sys

print("Total arguments passed: ",len(sys.argv))

print("Name of Program is : ",sys.argv[0])

print("Arguments passed:")

for i in range(1,len(sys.argv)):
    print(sys.argv[i])

sum=0
for i in range(1,len(sys.argv)):
    sum+=int(sys.argv[i])
print("SUm is:",sum)

