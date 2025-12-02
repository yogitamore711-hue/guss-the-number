import random

print("Guess the number")

# Computer generates random number
computerNumber = random.randrange(1, 101)

turns = 0

while True:
    userInput = int(input("Enter your guess number: "))
    turns += 1

    if userInput > computerNumber:
        print("Your guess is too high")

    elif userInput < computerNumber:
        print("Your guess is too low")

    else:           # userInput == computerNumber
        print("Your guess is correct!")
        print("Number of turns =", turns)
        break
