import re
def text_match(text):
        patterns = 'ab{2,3}$' #Minimum 2 maximum 3 b.
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
 
print(text_match("abb"))
print(text_match("abbb"))
print(text_match("abc"))