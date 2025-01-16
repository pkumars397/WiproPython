# Check if a specific word exists in a file and count its occurrences.

def searchAndCountWord(filename,word):
    with open(filename) as file:
        content=file.read()
        return content.lower().count(word.lower())
    
    
print(searchAndCountWord("txt2.txt","appended"))