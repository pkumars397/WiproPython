#format of indian mobile number
'''Indian mobile numbers have 10 digits.
They generally start with the digits 6, 7, 8, or 9.
The number may or may not include a country code (+91 or 91).
If a country code is included, it may be followed by a space, a hyphen (-), or nothing.'''
import re
def mobCheck(number):
    pattern = r'^(\+91[\s-]?)?[6-9][0-9]{9}$' 
    if re.search(pattern, number):
        return 'valid phone number'
    else:
        return 'Not a phone number'

n="+919185219968"
print(mobCheck(n))