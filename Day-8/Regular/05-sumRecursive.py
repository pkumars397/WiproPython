#Python program to calculate the sum of a list of numbers using recursion.

def sum(l):
   if len(l)==1:
       return l[0]
   return l[0]+ sum(l[1:])

l=[1,2,3,4,5]
print(sum(l))