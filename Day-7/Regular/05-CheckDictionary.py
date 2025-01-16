#Check if a variable is dictionary in python

d={"name":"prashant","age":25}

if isinstance(d,dict): # it checks whether entered object d is instance of dict class
    print("It is dictionary")
else:
    print("it is not dictionary")
    
#Sir Method   
if type(d) is dict:
     
    print("It is a dictionary")
 
else:
 
    print("Not a dictionary")