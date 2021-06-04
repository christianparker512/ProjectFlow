import random
answer = random.randint(1,10)

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guess it")
    else:
        print("Sorry, you have not guessed correctly")
