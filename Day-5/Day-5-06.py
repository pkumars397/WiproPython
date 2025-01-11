import re
txt = "hallo planet"

#Check if the string starts with 'hello':

x = re.search("planet$", txt)
if x:
  print("Yes, the string ends  with 'planet'")
else:
  print("Does not end with planet ")