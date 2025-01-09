# read n nos from the console. you can enter positive or negative values.
# print how many of them +ive and -ive

n=int(input("Enter how many number u want to enter: "))

countPos=0
countNeg=0
for i in range(1,n+1):
   num=int(input("enter number:"))
   if num>0:
     countPos+=1
   else: 
     countNeg+=1
print("Number of Positives: ",countPos)
print("Number of Negetives : ",countNeg)