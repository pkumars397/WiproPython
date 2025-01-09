'''Write a  Python function that checks whether a passed string is a palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.'''

def isPal(s):
    revStr=s[::-1]
    if s==revStr:
       return True
    return False

userIn=input("Enter your word: ")
print("Enter word ",userIn,"is palindrome YES/NO: ",isPal(userIn))