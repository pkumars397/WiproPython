#Write a Python program that matches a string that has an a followed by zero or one 'b'.
 
import re
def text_match(text):
    pattern="^a?(b)" #Zero OR one
    if re.search(pattern,text):
        return "Match found"
    else :
        return "Match not found"
 
print(text_match("ab"))
print(text_match("abc"))
print(text_match("abbc"))
print(text_match("aabbc"))