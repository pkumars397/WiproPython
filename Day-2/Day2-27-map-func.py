#we have list x=[1,2,3,4,5,6,7,8]

#and create new list y , contains squares of each element in x ]

#y =[1,4,9,16,25,36,49,64]
        
x=[1,2,3,4,5,6,7,8]
newList=map(lambda x:x**2,x)
print(list(newList))
