# random math question

import random

num = random.randint(0, 200)
guess = 0
while True:
    guess += 1
    print("I am thinking of a number, can you guess what it is? ")
    ans = int(input())
    if ans == num:
        break
    elif ans < num:
        print("Too low")
    elif ans > num:
        print("Too high")
    else:
        print("Wrong")
print(f"Correct you took {guess} guesses")
