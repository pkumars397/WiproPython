# Print maximum of three numbers

a=int(input('enter the a:'))
b=int(input('enter the b:'))
c=int(input('enter the c:'))
if a>b :
   biggest=a
else:
   biggest=b
if b<=c:
   biggest=c
print("biggest is: ",biggest)

# second method
#i=0
#nums=[]
#while i<3:
#  element=int(input("enter the element:"))
#  nums.append(element)
#  i+=1
#print(max(nums))
  