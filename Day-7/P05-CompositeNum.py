'''composite number is a positive integer which has more than two factors.
 
For example, 10 has factors 1, 2, 5, 10, hence it is a composite number.'''

number = int(input("Enter a number : "))
 
is_composite = False
 
for i in range(2, number):
    if number % i == 0:
        is_composite = True
 
if is_composite == True:
    print(number, "is a composite number")
else:
    print(number, "is not a composite number but a prime number")
 