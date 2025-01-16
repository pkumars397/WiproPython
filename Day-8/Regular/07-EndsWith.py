#Check if a String Ends With a Substring
#Verify if a string ends with a specific substring.

def EndsWith(str,sub):
    return str.endswith(sub)
def StartsWith(str,sub):
    return str.startswith(sub)

print(EndsWith("hello world","world"))
print(StartsWith("hello world","hello"))