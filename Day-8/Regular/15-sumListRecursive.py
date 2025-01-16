def sumRec(l:list[int])->int:
    total=0
    for item in (l):
        if type(item)==type([]):
            total=total+sumRec(item)
        else:
            total+=item
    return total

list=[12,32,[1,2,3],22]
print(sumRec(list))