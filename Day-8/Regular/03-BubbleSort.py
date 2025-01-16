l=[12,3,3,4,0,1,50]

for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
print(l)