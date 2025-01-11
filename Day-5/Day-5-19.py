from collections import Counter
# file=open("txt2.txt")
# word=file.read().split(" ")

# wordCount=Counter(word)
# print(wordCount)

from collections import Counter
def word_count(fname):
        f=open(fname)
        return Counter(f.read().split())  #Counter takes list as argument and returns dictionary

print("Number of words in the file :",word_count("text.txt"))