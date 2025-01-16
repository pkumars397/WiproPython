# Count the total number of lines in a file.

def countL(file):
    with open(file) as f1:
        return sum([1 for line in f1])
print(f'total number of lines in txt2.txt is {countL("txt2.txt")}')