import random
dice = [1, 2, 3, 4, 5, 6]
print("Randomly selecting same number of a dice")
for i in range(6):
    random.seed()
    print(random.choice(dice))