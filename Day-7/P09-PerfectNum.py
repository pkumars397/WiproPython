'''A number is a perfect number if is equal to sum of its proper divisors, that is,
sum of its positive divisors excluding the number itself.
Input: n = 6
 
Output: true
 
Divisors of 6 are 1, 2 and 3. Sum of divisors is 6'''

def perfectOrNot(n):
    sumOfDiv=0
    for i in range(1,n-1):
        if n%i==0:
            sumOfDiv+=i
    if sumOfDiv==n:
        return "YEs"
    return "No"
n=int(input("enter number"))
print(f"Entered number {n} is Perfect Number or not: {perfectOrNot(n)}")