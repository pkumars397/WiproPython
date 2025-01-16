l=[12,3,1,5,7,4]

for i in range(len(l)):
    minElemetIndex=i
    for j in range(i,len(l)):
        if l[j]<l[minElemetIndex]:
            minElemetIndex=j
            
    if minElemetIndex!=i:
        l[i],l[minElemetIndex]=l[minElemetIndex],l[i]
print(l)
