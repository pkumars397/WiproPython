'''Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336'''

def mul(a):
    prod=1
    for i in range(len(a)):
        prod*=a[i]
    return prod
l=[]
n=int(input("How many elements in list :"))
print("Enter elements:")
for i in range(n):
    element=int(input())
    l.append(element)
print("Product of elements of list is : ",mul(l))
