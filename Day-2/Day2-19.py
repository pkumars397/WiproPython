#Remove duplicates from the list
#Remove duplicates from the list

a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

finallist=[]
for i in a:
    if not (i in finallist):
        finallist.append(i)
print(finallist)


# a=list(set(a)) ,list of unique elements

