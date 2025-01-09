# read amt from console ,shop give discount of 10% if amnt greater than 1000
# if amount is less than 1000 ,5 % dicount
# if amount is between 1000 and 5000,7% discount
# if amount is greater than 5000,10% discount
# print amt,discount and net amount
# logical operator : and or not
# relational operator : >,>=,<,<=

amount=float(input("enter the value for amount: "))


if amount<1000:
   discount=0.05*amount

elif amount>=1000 and amount<=5000:
   discount=0.07*amount
else:
   discount=0.1*amount

netAmount=amount-discount
print("Amount: ",amount)
print("Discount: ",discount)
print("netAmount: ",netAmount)