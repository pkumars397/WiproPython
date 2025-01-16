''' Adam Number Program In Python [ LB-1]
An Adam number is a number for which the square of the number, when its digits are reversed and
is equal to the square of the number obtained by reversing the digits. For example the number 22 is an adam number because,
the square of 22 is 484 and the reverse of 484 is also 484, So the reversed square and the square of the reversed number
are equal thus making it an adam number.
'''
def is_adam_number(number):
    # Calculate the square of the number
    squared_number = number ** 2

    # Reverse the squared number
    reversed_squared_number = int(str(squared_number)[::-1])

    # Calculate the square of the reversed number
    square_of_reversed_number = int(str(number)[::-1]) ** 2

    # Check if the reversed square and square of the reversed number are equal
    return reversed_squared_number == square_of_reversed_number

# Example usage
number = int(input("Enter a number: "))
if is_adam_number(number):
    print(number, "is an Adam number.")
else:
    print(number, "is not an Adam number.")