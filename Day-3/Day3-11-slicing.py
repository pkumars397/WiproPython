#Syntax list[start:end:step] 

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get all elements in the list
print(a[::])
print(a[:])

#Start to someIndex
print(a[:3])
#from some index to end
print(a[1:])

#from some index to some index-1
print(a[1:4])

#using step
print(a[1: :2])

#out of bound but will not throw an error
print(a[2:100])

#Using negative index for slicing from end of the list
print(a[-2:])

print(a[:-3]) #will exclude -3 index

print(a[-4:-2])
