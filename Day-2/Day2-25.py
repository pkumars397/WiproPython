def biggest(a,b,c):
   
    if a>b:
        largest=a
    else:
        largest=b
    if b<c and b>a:
        largest=c
    return largest
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))

print("largest of three is:",biggest(a,b,c))