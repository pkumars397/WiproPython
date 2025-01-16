#Write a Python program that matches a string that has an a followed by one or more b's.
 
import re

def text_match(text):

     pattern ="^a(b+)" #One or more occurance
     if re.search(pattern,text):
         return "found a match"
     else:
         return "not found a match"
 
print(text_match("ab"))

print(text_match("abc"))