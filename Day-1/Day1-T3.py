#1.print sum of odd  nos from 1 to n using for loop

n=int(input("Enter the n: "))

oddSum=0
for i in range(1,n+1):
  if i%2!=0:
     oddSum+=i

print(oddSum)
