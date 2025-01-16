#Remove all whitespace from a string.
 
def remove_whitespace(s):
    return ''.join(s.split(" "))
 
print(remove_whitespace(" h e l l o "))  # Output: "hello"