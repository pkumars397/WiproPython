'''Faulty Calculator In Python With Code
After running this program you will see that it asks you to enter two numbers and the operation
you want to perform then it will check if the entered numbers match the faulty conditions or
not if not then it will print the real result if matches it prints the faulty result you entered below is an example output.

Enter a number: 2
Enter another number: 9
 
What operation do you want to do (+,-,/,*): *
18'''

def faulty_Calculator():
    n1=int(input("Enter a number: "))
    n2=int(input("Enter another number: "))

    op=input("What operation do you want to do (+,-,/,*): ")
    if op=="+":
      print(n1+n2)
    elif op=="-":
      print(n1-n2)
    elif op=="/":
      print(n1/n2)
    elif op=="*":
      print(n1*n2)
    else: 
      print("Enter a valid Operation")