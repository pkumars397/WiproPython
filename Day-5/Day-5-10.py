def fnc(*a):
    print("Entered arguments are: ",a)   #returns list of arguments
    
fnc(1,2,3)

def fnc2(**a):
    print("entered arguments :",a)   #returns dictionary of key value pair 
    
fnc2(name="prashant",age=24)