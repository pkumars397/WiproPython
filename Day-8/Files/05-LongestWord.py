# Identify the longest word in a text file.
def longest(file):
    with open(file,"r") as file:
        content=file.read()
        contentList=content.split()
        longestWords=max(contentList,key=len)
        return longestWords
    
print(longest('txt2.txt'))