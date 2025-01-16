'''
An autobiographical number is a type of number where each digit in the number tells us how many times that
# digit appears in the number itself. Let’s take the number 21200 for example, the first digit in 0 position of the 
# number is two which indicates that there are 2 zeros in the number, then at 1 position there is one which tells us
# that there is only 1 one in the number,next we have at the 2 position the number two which indicates that
# there are only 2 two’s in the number.

2 1 2 0 0

0th position contains 2  [  two 0's ]
1th postiton contains 1  [ only 1  ]
2nd postion contains  2   [ 2 twos ]
3rd postion  cotains  0  [ how many 3rs are here ]
'''

def autoBioN(n):
    '''for i,item in enumerate(n): #21200
       # Mine method
        counter=int(item)
        countIndex=0
        for item in n:
            if int(item)==i:
                countIndex+=1
        if countIndex==counter:
           continue
        else: 
            return "not an autobiographical number"
            break
    return "an autobiographical number"'''
    
    #Sir method
    number_str = str(n)
    count = [0] * 10 #Creating an list for storing howmany times each digit appeared
 
    for digit in number_str:
        count[int(digit)] += 1
 
    for i in range(len(number_str)):
        if int(number_str[i]) != count[i]:
            return False
 
    return True
        
n=input("enter a number: ")
print(autoBioN(n))