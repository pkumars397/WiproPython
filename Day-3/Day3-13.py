#import is being used to import the liberaries.

import random
import os
cwd=os.getcwd()
print("current working directory is:",)
for i in range(10):
   print(random.random())
   print(random.randint(1,3))
mylist=["apple","banana","gauva"]
print(random.choice(mylist))