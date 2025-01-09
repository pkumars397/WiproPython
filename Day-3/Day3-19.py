import sys
n=len(sys.argv)
countPos,posSum,countNeg,negSum=0,0,0,0
for i in range(1,n):
    argument=int(sys.argv[i])
    if argument>0:
       posSum+=argument
       countPos+=1
    else:
       negSum+=argument
       countNeg+=1
print("Total number of positives are: ",countPos,"and sum of positives is ",posSum,"\nTotal number of negatives are:",countNeg,"and Sum of negatives :",negSum)