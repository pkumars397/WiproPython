#Takes two lists and returns True if they have at least one common member ,otherwise False


def cmmnMembers(x,y):
    for i in x:
        if i in y:
           return True
    else : return False
print(cmmnMembers([1,2,3],[4,45]))
print(cmmnMembers([1,2,3],[3,4,5]))