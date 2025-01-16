#Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
def changeS(str):
    # sList=list(str)
    # sList[0],sList[-1]=sList[-1],sList[0]
    # return "".join(sList)
    return str[-1]+str[1:len(str)-1]+str[0]
    
str="hello"
print(changeS(str))