try:
#    x=5
   print(x)
except NameError: #when a variable is not defined
       print("value of the variable is not defined ")
except :
       print("Error in the Program  ")
else:
       print("No Errors , works fine ") # block executed when there is no error
       
finally:
      print("Program ends    ")  #block executes irrespective of got error or not