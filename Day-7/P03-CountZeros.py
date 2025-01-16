# Find the number of zero in a number

def countZero(n):
    counter=0
    n=str(n)
    for item in n:
        if item=="0":
            counter+=1
    return counter

n=int(input("enter a num: "))
print(f'number of zero is {countZero(n)}')