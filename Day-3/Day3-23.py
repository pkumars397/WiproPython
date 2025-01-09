'''Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12'''

def countUpperLower(s):
    countUp=0
    countLow=0
    for i in s:
       if i.isupper():
          countUp+=1
       else:countLow+=1
    return (countUp,countLow)

userInput=input("Enter string: ")
totalUp,totalLow=countUpperLower(userInput)
print("No. of Upper case characters :",totalUp)
print("No. of Lower case Characters :",totalLow)
