# It will search for a target element by iterating through entire list
def lin_Search( list, n):
    for index,item in enumerate(list):  # Number of Checking in worst case: n,Best case is 1
        if item==n:                     # Space it is taking is 1 ,O(1)
            return index
    return -1
target=89
i=lin_Search([23,45,67,89,19,24] , 89)
# print(i)
if i!=-1:
    print(f'Target {target} found at index {i} ')
else: 
    print(f'{target} not found in the list')