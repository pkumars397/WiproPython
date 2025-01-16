'''
Check If Backslash In String In Python:
how to check if a backslash(\) is there in a string in python, to check whether there is a backslash
in a string we will use if statement and check if there is a backslash in the string so let’s see it in code.
 
text = "hi \ how are you"
'''

text = "hi \ how are you"

if r'\\' in text:
    print("There is a backslash")
else:
    print("No backslash found")
