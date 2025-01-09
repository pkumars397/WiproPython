# read gender (m for male , f for female) and age.
# they can vote if gender is m and age is 21 and above.
# they can vote if gender is f and age is 18 and above.
# other case they are not eligible to vote

gender=str(input("Enter gender: "))
age=int(input("Enter age: "))

if gender=="m" and age>=21:
   print("You can vote")
elif gender=="f" and age>=18:
   print("You can vote")
else:
   print("Sorry you are not eligible to vote")
