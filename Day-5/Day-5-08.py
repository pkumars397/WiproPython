#String formating

price = 59
txt = f"The price is {price} dollars"
print(txt)
 
 
#Display the value 95 with 2 decimals:
 
txt = f"The price is {95:.2f} dollars"
print(txt)
 
 
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)
 
 
#Use the string method upper()to convert a value into upper case letters:
 
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)