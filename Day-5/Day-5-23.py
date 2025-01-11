try:
    f=open("sample.txt")
    for i in f:
         print(i)
except FileNotFoundError:
     print("Wrong File Name ")