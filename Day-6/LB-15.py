'''Swap first 2 chars of 2 strings.
 
Write a Python program to get a single string from two given strings, separated by a space and swap the
first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'''

def sweapChar(s1,s2):
   newStr1=s2[0:2]+s1[2:]
   news2=s1[:2]+s2[2:]
   return newStr1+" "+news2
   

s1="abc"
s2="xyz"
print(sweapChar(s1,s2))
        