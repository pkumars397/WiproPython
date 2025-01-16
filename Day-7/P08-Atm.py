'''Welcome to the Pythondex ATM
Please enter your four digit pin: 1234
what do you want to do
Enter 1 to Widthdraw Cash
Enter 2 for Balance Enquiry
Enter 3 to Quit
Enter the number corresponding to the activity you want to do: 2
 
Total balance 1000 Dollars
 
what do you want to do
Enter 1 to Widthdraw Cash
Enter 2 for Balance Enquiry
Enter 3 to Quit
Enter the number corresponding to the activity you want to do: 1000
Please enter a correct value shown
what do you want to do
Enter 1 to Widthdraw Cash
Enter 2 for Balance Enquiry
Enter 3 to Quit
Enter the number corresponding to the activity you want to do: 2
Total balance 1000 Dollars
 
what do you want to do
Enter 1 to Widthdraw Cash
Enter 2 for Balance Enquiry
Enter 3 to Quit
Enter the number corresponding to the activity you want to do: 1
Enter the amount of money you want to widthdraw: 1000
1000 Dollars successfully widthdrawn your remaining balance is 0 Dollars
 
what do you want to do
Enter 1 to Widthdraw Cash
Enter 2 for Balance Enquiry
Enter 3 to Quit
Enter the number corresponding to the activity you want to do: 2
Total balance 0 Dollars
 
what do you want to do
Enter 1 to Widthdraw Cash
Enter 2 for Balance Enquiry
Enter 3 to Quit
Enter the number corresponding to the activity you want to do: 1
Enter the amount of money you want to widthdraw: 1
You don't have sufficient balance to make this widthdrawal
Enter the amount of money you want to widthdraw: 0
0 Dollars successfully widthdrawn your remaining balance is 0 Dollars'''

def atmWorkflow():
    balance=1000
    print(f"Welcome to the Pythondex ATM")
    while True:
        print(f"what do you want to do\nEnter 1 to Widthdraw Cash\nEnter 2 for Balance Enquiry\nEnter 3 to Quit")
        userInput=int(input(f'Enter the number corresponding to the activity you want to do: '))
        if userInput==1:
            try:
              withdrawalAmnt=int(input("Enter the amount of money you want to widthdraw: "))
              if balance>withdrawalAmnt:
                balance-=withdrawalAmnt
                print(f"{withdrawalAmnt} Dollars successfully widthdrawn your remaining balance is {balance} Dollars")
            except ValueError:print("Enter a valid value: ")
            else: print("You have insufficient funds\n")
        elif userInput==2:
            print(f'\nTotal balance {balance} Dollars\n')
        elif userInput==3:
            print("Thank you for using Parathyxon atm ")
            break
        else:print("Please enter a correct value shown\n")
    
atmWorkflow()