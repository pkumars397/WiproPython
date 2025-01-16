# Read a text file line by line and print its content.

def readFile(file):
    with open(file,"r") as file:
        for line in file:
            print(line.strip()) #removes trailing and ending
readFile("./txt1.text")