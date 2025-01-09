import sys
n=len(sys.argv)
biggest=int(sys.argv[1])
for i in range(2,n):
   if biggest<int(sys.argv[i]):
       biggest=int(sys.argv[i])
print("\nBiggest of all the arguments are: ",biggest)