import random

secretNumber = random.randint(1,1000)
print("Please type number between 1 and 1000")
guess = None

for guessesTaken in range(1,15):
    print ("Try to guess my number （。＾▽＾）")
    guess=int(input())

    if(guess < secretNumber):
        print("Your number is smaller")
    elif(guess > secretNumber):
        print("Your number is bigger")
    else:
        break
if guess == secretNumber:
    print("Congratulations! You guessed it!")
else:
    print("Don't worry! You will get it next time!")
