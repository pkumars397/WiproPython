# Count the total number of words in a text file.

def count_words(file):
    # count=0
    # with open(file) as file:
    #     for line in file:
    #         line=line.split()
    #         count+=len([w for w in line])
    # return count
    
    with open(file,"r") as file:
        content=file.read()
        # print(type(content)) #returns string.
        return len(content.split()) #it create a list of words ,returns its length
print(f'total words in txt2.txt file is {count_words("txt2.txt")}')