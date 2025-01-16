#Write a Python program that matches a string that has an 'a' followed by anything ending in 'b'.
import re
def matchStr(s):
    pattern='^a.*(b)$' #. specify any character ,and * ,zero or more times
    if re.search(pattern,s):
        return "matched"
    return "unmatched"

str="akfksjb"
str2="asfjc"
print(matchStr(str),matchStr(str2))