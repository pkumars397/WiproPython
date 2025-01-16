# Append new content to an existing file.
def append_to_file(filename, text):
     
    with open(filename, 'a') as file:
        file.write(text + '\n')
 
append_to_file("./Day08-Logic-building/Files-Questions/txt2.txt","This is an appended line")