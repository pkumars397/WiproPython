# read n nos from the console. you can enter positive or negative values.
# use the same logic above. find sum of positive and negative nos.
n=int(input("Enter how many number u want to enter: "))

sumPos=0
sumNeg=0
for i in range(1,n+1):
   num=int(input("enter number:"))
   if num>0:
     sumPos+=num
   else: 
     sumNeg+=num
print("sum of Positives: ",sumPos)
print("sum of Negetives : ",sumNeg)