# read amt from console ,shop give discount of 10% if amnt greater than 1000
# print amt,discount and net amount

amount=float(input("enter the value for amount: "))

discount=0

if amount>1000:
   discount=0.1*amount

netAmount=amount-discount

netAmount=amount+discount
print("Amount: ",amount)
print("Discount: ",discount)
print("netAmount: ",netAmount)