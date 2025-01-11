# import copy
# x=[1,2,4,55]
# sc=copy.copy(x)
# dc=copy.deepcopy(x)

# print("shallowcpy" ,sc)
# print("deepcopy",dc)

# x[0]="changed"
# print(x)
# print("shallowcpy" ,sc)
# print("deepcopy",dc)

import copy

x= [[1, 2, 3], [4, 5, 6]]

shallow_copy = copy.copy(x)
deep_copy = copy.deepcopy(x)
print(shallow_copy)
print(deep_copy)


x[0][0] = 'Changed'

print(shallow_copy) 

print(deep_copy)