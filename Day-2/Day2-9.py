# enter ur name and count number of  vowels 

name=input("enter ur name:")
numVowels=0
for i in name:
    if(i=="a" or i=="e" or i=="o" or i=="i" or i=="u"):
      numVowels+=1

print("numVowels in my name:",name,"is",numVowels)