#Remove all punctuation from a string.
import string

def remove_punctuation(s):

    return ''.join(char for char in s if char not in string.punctuation)


print(remove_punctuation("Hello, world!"))  # Output: "Hello world"