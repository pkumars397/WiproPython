# take temp in cel and convert into feh
#print both temp in celcius and fahren
#fah=1.8 * cel +32 ,formula

temp=float(input("enter the temperature:"))
fah=1.8*(temp)+32
print("Temperature in fah is: ",fah)

fah=float(input("enter the temperature in fah:"))
cel=(fah-32)/1.8
print("temperature in cel is: ",cel)

