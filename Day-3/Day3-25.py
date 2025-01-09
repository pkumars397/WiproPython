'''Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
'''
l=[1,2,3,4,5,6,7,8,9]
ansList=[]
for item in l:
  if item%2==0:
     ansList.append(item)
print(ansList)