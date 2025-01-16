'''Calculate the sum and average of the digits present in a string
 
Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other
 
characters.
 
Given:
 
str1 = "PYnative29@#8496"'''

def sumAvg(s):
    #Method 1
    # sum=0
    # count=0
    # avg=0
    # for i in s:
    #     if i.isdigit():
    #         sum+=int(i)
    #         count+=1
    # if count:
    #     avg=sum/count
    #     return (sum,avg)
    
    #Method 2
    digitList=[int(i) for i in s if i.isdigit()]
    total=sum(digitList)
    avg=total/len(digitList)
    return total,avg

str1="PYnative29@#8496"
sum,avg=sumAvg(str1)
print(f"Sum is {sum} and average is {avg}")