low = 1
high = 1000

print("Please think of a number between {} and {}".format(low,high))
input("Press Enter to start")

guess = 1
while True:
    guess = low + (high - low)//2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                    "Enter h or l or c if the guess was correct"
                    .format(guess)).casefold()
    if high_low =="h":
        #Guess higher: the low end of the range becomes 1 greater than the guess
        pass
    elif high_low == "l":
        # guess lower. the high end of hte range becomes one less than the guess.
        high = guess - 1
    elif high_low == "c":
            print("I got it in {} guesses!".format(guess))
            break
    else: print("Please enter h, l or c")