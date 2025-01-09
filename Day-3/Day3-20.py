'''Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20'''

def sumOfEl(a):
    total=0
    for i in range(len(a)):
        total+=a[i]
    return total

exList=[]
print("How many elements in list:")
n=int(input())
for i in range(n):
  e=int(input("enther element:"))
  exList.append(e)

print(sumOfEl(exList))
