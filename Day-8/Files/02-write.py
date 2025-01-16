# Write a list of strings to a file, each on a new line.
def write_to_file(filename, lines):
     
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + '\n')
            
write_to_file('./txt2.txt', ['Hello', 'World', 'Python is great!'])
