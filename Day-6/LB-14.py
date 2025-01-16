'''Replace first char occurrences with $.
 
Write a Python program to get a string from a given string where all occurrences of its first char 
have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'''

def changeStr(s):
    newStr=s[0]
    fc=s[0]
    for i in range(1,len(s)):
        if s[i]==fc:
            newStr+="$"
        else: 
            newStr+=s[i]
    return newStr
st="restart"
print(changeStr(st))