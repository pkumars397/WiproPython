# list accessing elements from left to right ,from 0 to n-1 index
# from right to left ,-1,-2...
# its contains of hetrogeneous elemnts

marks=[]                      # empty list
print(type(marks))
print(len(marks))             # len() returns length of the list
staff=["Lalitha" , 23 , 8.9 , False ]
print("Name   " ,staff[0])
print("Age    " ,staff[1])
print("Score  " ,staff[2])  # access from L to R
print("Score  " ,staff[-2]) # access from R to L
print("length of staff",len(staff))