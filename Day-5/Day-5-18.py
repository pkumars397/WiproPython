#import counter class from collections module
from collections import Counter
#Creating a Counter class object using list as an iterable data container
a = [12, 3, 4, 3, 5, 11, 12, 6, 7]
x = Counter(a)
#directly printing whole x
print(x) # will give dictionary as key value pair