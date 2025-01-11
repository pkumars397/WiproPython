try:
    a=int(input("Enter value for a   "))
    b=int(input("Enter value for b   "))
    print(a/b)
except ZeroDivisionError:
     print("Denomintaor can not be zero")
     
else:
    print("No erros in the programm ")

finally:
    print("Program ends ")