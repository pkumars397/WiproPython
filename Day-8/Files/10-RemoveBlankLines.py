# Remove all blank lines from a text file.
 
def remove_blanks(filename):
     with open(filename, 'r') as file:
        lines = file.readlines()
        # print(type(lines))
     with open(filename, 'w') as file:

        for line in lines:
            if line.strip():
                file.write(line)
    
remove_blanks("txt2.txt")