import random
options = ("ROCK", "PAPER", "SCISSOR")
condition=True

while condition:
    my_input = None
    Computer_input = random.choice(options)
    while my_input not in options:
        my_input = input("Enter rock,paper,scissor\n").upper()
        print("please Enter one of the following options😕😕😕😕😕")

    print(f"player: {my_input}")
    print(f"computer bot: {Computer_input}")
    if my_input == Computer_input:
        print("Its a draw!😊")
    elif my_input == "ROCK" and Computer_input == "SCISSOR":
        print("CONGRATS!YOU WON💃💃💃💃🥳🥳")
    elif my_input == "PAPER" and Computer_input == "ROCK":
        print("CONGRATS!YOU WON💃💃💃💃🥳🥳")
    elif my_input == "SCISSOR" and Computer_input == "PAPER":
        print("CONGRATS!YOU WON💃💃💃💃🥳🥳")
    else:
        print("OOPS! YOU LOOSE😭😭😭🥹🥹")
    if not input("want to play again? y/n?:").lower() == 'y':
        condition = False
print("Thank you for playing!")