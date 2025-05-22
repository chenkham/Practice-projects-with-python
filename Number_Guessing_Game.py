import random
new=random.randint(1,50)
attempts=7

while attempts>0:
    try:
       guess=int(input("Guess a number between 1 and 50:(you will be given 10 attempts choose smartly😊good luck)\n"))
    except Exception as e:
        print(e)
        guess= int(input("Guess a number between 1 and 50:(you will be given 10 attempts choose smartly😊good luck)\n"))
    if guess>new:
        print("Too high! choose a little lower")
    elif guess<new:
        print("Too low! choose a little higher")
    else:
        print("congrats! you guessed it!:")
    attempts-=1
if attempts==0:
    print("Oops sorry! your have used all you attempts to guess a number between 1 and 50.")