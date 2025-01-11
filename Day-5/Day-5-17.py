# file=open("txt2.txt")
# longestW=""
# for line in file:
#     l=line.split(" ")
#     for word in l:  
#         if len(word)>len(longestW):
#             longestW=word
# file.close()
# print("Longest word is:",longestW)
        
        
f=open("txt2.txt")
words=f.read().split()
maxword= max(words,key=len)
maxlen=len(maxword)
result= [word for word in words if len(word)==maxlen]
print(result)