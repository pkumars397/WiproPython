#Find the list of words that are longer than n from a given list of words

#"The quick brown fox jumps over the lazy dog"

#read n value from the console and list of words who have length  > n


str="The quick brown fox jumps over the lazy dog"
n=int(input("enter the n: "))
ansList=[];
word=""
for i in str:
      if i!=" ":
         word+=i
      else:
        
         if len(word)>n:
          ansList.append(word)
         word=""

print(ansList)
         
    
    