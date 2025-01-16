'''Regular expression for adharcard in python


It should have 12 digits.
It should not start with 0 and 1.
It should not contain any alphabet and special characters.
It should have white space after every 4 digits.


Input: str = “3675 9834 6012” 
Output: true 
Explanation: 
The given string satisfies all the above mentioned conditions. Therefore, it is a valid Aadhaar number.
Input: str = “3675 9834 6012 8” 
Output: false 
Explanation: 
The given string contains 13 digits. Therefore, it is not a valid Aadhaar number.'''

import re

def checkAadhar(str):
    pattern=r'^[2-9]{1}[0-9]{3}\s[1-9]{4}\s[1-9]{4}$' # between 2 and 9 both included,one time.then 0 to 9,3 times ,\\s means space should be there.we can also use only \s if using r.
    if re.search(pattern,str):
        return "Valid"
    else:
        return "Not valid"
str="2343 2332 2334 "
print(checkAadhar(str))