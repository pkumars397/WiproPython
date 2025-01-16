def find_shortest_word(l):
    # minWord=min(l,key=len)
    # print("Smallest word is",minWord,"and length is ",len(minWord))
    
    # smallestWord=""
    # for word in l:
    #     if len(word)>len(longestWord):
    #         smallestWord=word
    # return [smallestWord,len(smallestWord)]
    
    #sir Method
    wordlist=[]
    for item in l:
        wordlist.append((len(item),item))
    wordlist.sort()
    return wordlist[0][1],wordlist[0][0]

smallestW,length = find_shortest_word(["PHP", "Exercises", "Backend"])

print((f'Shortest word is {smallestW} and length is {length}'))