marks=[12,34,45,50,60]
# create two lists pmarks and fmarks. pmarks contains element of marks >=50 
# fmarks contains elements of marks < 50
# print marks, pmarks and fmarks
marks=[12,34,45,50,60]
pmarks=[]
fmarks=[]
for element in marks:
    if element>=50:
       pmarks.append(element)
    else:
       fmarks.append(element)
print(pmarks,fmarks)
    