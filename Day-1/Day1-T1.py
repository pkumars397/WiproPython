#1.print sum of odd  nos from 1 to n using while loop

n=int(input("Enter the n: "))

i=1
oddSum=0
while i<=n:
  if i%2!=0:
     oddSum+=i
  i+=1

print(oddSum)

