from collections import Counter

def countRepeatedMarks(l):
    rl=Counter(l)
    return rl

marks=[]
for i in range(10):
    m=int(input("Enter Mark: "))
    marks.append(m)
print(countRepeatedMarks(marks))