# Python 3 program to find
# factorial of given number
def factorial(n):
    #Iterative way of doing factorial
    '''
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
    '''
    #Recursive Way of doing factorial:
     
    if n == 0:
        return 1
 
    return n * factorial(n - 1)
 
 
# Driver Code
num = 5
print("Factorial of", num, "is", factorial(num))