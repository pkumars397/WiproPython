#Write a Python program that matches a string that has an a followed by zero or more b's.[Logic Building]

import re

def text_match(text):
    import re
def text_match(text):
      patterns = '^a(b*)$' #Zero or more occurance
      if re.search(patterns,  text):
                return 'Found a match!'
      else:
                return('Not matched!')
       
print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))