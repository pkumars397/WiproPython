#Strong Numbers are the numbers whose sum of factorial of digits is equal to the original number.

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

def strongNum(num):
    total=0
    num=str(num)
    for n in num:
        total+=fact(int(n))
    print(total)
    return total==int(num)

num=int(input("enter the number: "))
print(f'Entered number is strong Number: {strongNum(num)}')