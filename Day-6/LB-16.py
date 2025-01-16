def find_longest_word(l):
    # maxWord=max(l,key=len)
    # print("Longest word is",maxWord,"and length is ",len(maxWord))
    
    # longestWord=""
    # for word in l:
    #     if len(word)>len(longestWord):
    #         longestWord=word
    # return [longestWord,len(longestWord)]
    
    #sir Method
    wordlist=[]
    for item in l:
        wordlist.append((len(item),item))
    wordlist.sort()
    return wordlist[-1][1],wordlist[-1][0]

longestW,length = find_longest_word(["PHP", "Exercises", "Backend"])

print((f'Longest word is {longestW} and length is {length}'))