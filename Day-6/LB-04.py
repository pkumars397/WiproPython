#Write a Python program that matches a string that has an a followed by three 'b'.
import re

def text_match(text):

        patterns = 'ab{3}$' # Specified number of times,use quantifier bracket after the charactor.

        if re.search(patterns,  text):

                return 'Found a match!'

        else:

                return('Not matched!')
 
print(text_match("abbb"))

print(text_match("aabbbbbc"))