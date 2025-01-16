import random
def guessNum():
    generatedNum=random.randint(1,10)
    count=5
    while True:
        userInput=int(input("Guess a number between 1 and 10: "))
        if userInput==generatedNum:
            print(f'You have guessed it correct ,Random number is {generatedNum}')
            break
        elif userInput<generatedNum:
            count-=1
            print("Oops you entered too low and your attempt left is",count)
        else:
            count-=1
            print("Oops you entered too High and your attempt left is",count)
        
        if count==0:
            print(f"You have exceeded your limit  and random number was ",generatedNum)
            break
    # print(generatedNum)
guessNum()