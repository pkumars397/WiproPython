#Write a Python program to check that a string contains only a certain 
#set of characters (in this case a-z, A-Z and 0-9).
import re
def is_allowed_specific_char(string):
    string = re.search('[^a-z A-Z 0-9]',string) # it will look for a-z or A-Z or 0-9 or space
    return not bool(string)
 
print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))