'''Write a Python function that takes a list and returns a new list with distinct elements from the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]'''

def distinct(l):
    '''
    newList=list(set(l))
    return newList
    '''
    newList=[]
    for item in l:
      if item not in newList:
         newList.append(item)
    return newList
print(distinct([1,2,3,3,3,3,4,5]))
