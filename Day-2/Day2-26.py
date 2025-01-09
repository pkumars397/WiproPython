marks=[23,45,67,78,90,48]

#new list is formed by adding 2 to each element of the list marks

#newlist=[25,47,68,80,92,50]

#your task is create newlist based on the requirement above

def add2(l):
    for i in range(len(l)):
         l[i]+=2
    return l;

print(add2(marks))
        