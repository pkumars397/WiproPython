#Write a  Python program to handle a ZeroDivisionError exception when dividing a number by zero.

# Define a function named divide_numbers that takes two parameters: x and y.

def divide_numbers(x, y):
    try:
       
        result = x / y
        
        print("Result:", result)

    except ZeroDivisionError:
       
        print("The division by zero operation is not allowed.")

numerator = 100
denominator = 0
divide_numbers(numerator, denominator)