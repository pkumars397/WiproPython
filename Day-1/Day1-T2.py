#1.print sum of even  nos from 1 to n using while loop

n=int(input("Enter the n: "))

i=1
evenSum=0
while i<=n:
  if i%2==0:
     evenSum+=i
  i+=1

print(evenSum)
