#Replace Substring
 
#Problem: Replace all occurrences of a substring with another.
 
def replace_substring(s, old, new):
    return s.replace(old, new)
 
print(replace_substring("hello world", "world", "Python"))  # Output: "hello Python"