#Write a Python program to find sequences of lowercase letters joined by an underscore.
 
# [a-z] will check if char is smaller alphabet

import re
def text_match(text):
    pattern=r"^[a-z]+_[a-z]+$" #match one or more lowercase and then one underscore and followed by [a-z]>=1 and it should at the end.
    # usring r is not necessary ,but without it python understands it as normal string.but we need raw string. useful when using \.
    if re.search(pattern,text):
        return "matched"
    return 'not matched'
print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aab_abbbc"))