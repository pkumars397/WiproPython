import re
txt = "hallo planet"

#Check if the string starts with 'hello':

x = re.search("^hallo", txt) #returns boolean
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")