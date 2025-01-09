# read a number and sum of its digit
n=input("enter the num:")

sumOfDigits=0
for i in n:
    sumOfDigits+=int(i)
print(sumOfDigits)