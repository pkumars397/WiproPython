'''Check If String Contains Brackets In Python
text = "Hello {  how are you"
 
# Enter type of bracket you want check (), [], {}
 
if '{' in text:
    print("there is a bracket in text")'''
    
def checkBraces(typeBrace,str):
    for item in str:
        if typeBrace in str:
            return True
        else:
            return False
ans=checkBraces("{","Hello {  how are you")
if ans:
    print("There is brace in text")
else:
     print("This is no brace in text")