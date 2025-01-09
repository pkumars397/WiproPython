#1.print sum of even  nos from 1 to n using for loop

n=int(input("Enter the n: "))

evenSum=0
for i in range(1,n+1):
  if i%2==0:
     evenSum+=i

print(evenSum)
