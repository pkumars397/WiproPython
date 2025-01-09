# Tuples -- Similar to list but its items are not modifiable,imutable
# enclosed in small braces.

marks=(12,34,56,78,90,19)
print(type(marks))
print("\n")

print(marks)


for I in marks:
   print(I)
#Aggregate functions

print("Length: ",len(marks))
print("Sum is: ",sum(marks))
print("Maximum element in tuple is :",max(marks))
print("minmum element in tuple is : ",min(marks))

