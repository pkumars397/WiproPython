#A PAN (Permanent Account Number) card issued in India follows a specific format: 10 characters long, starting with 5 uppercase letters, followed by 4 digits, and ending with 1 uppercase letter.
import re
def panCheck(p):
    pt=r'[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if re.search(pt,p):
        return "Valid PAN"
    return "invalid pan"
p="GUIPK4048G"
p1="sfjksdjdfkjkj334"
print(panCheck(p),"\n",panCheck(p1))