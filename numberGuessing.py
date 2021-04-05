import random

number = random.randint(1, 10)
tries = 0

username = input("Your name: ")
username = username.strip()

print(f"Hey! {username}")
print("Lets play a game?")
print("1) Yes")
print("2) No")

option = input("Select your option: ")
option = int(option)

if option==1:
    print("Guess the number I'm thinking of between 1 and 10")
    print("You get three attemps")
elif option==2:
    print("Boring:(")
else:
    print("Invalid")

guess = input("Guess a number: ")
guess = int(guess)
tries+=1

if guess>number:
    print("Too high...")
if guess<number:
    print("Too low..")

while guess!=number and tries<3:
    guess = input("Try again: ")
    guess = int(guess)
    tries+=1

if guess>number:
    print("Too high...")
if guess<number:
    print("Too low..")

if guess==number:
    print("Well done!")
    print(f"It took you: {tries} Tries")
else:
    print("You Lost!")
