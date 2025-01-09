'''Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"'''

userInput=input("Enter your string: ")
revStr=''
for char in userInput:
    revStr=char+revStr
print("Reverse Of the entered String: ",userInput,"is ",revStr)
