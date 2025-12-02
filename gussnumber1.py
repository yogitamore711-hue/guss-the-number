import random 

#Computer genreat a random number
computerNumber=random.randrange(1,101)

#computer genreated number is user guess
userInput=int(input("Enter your number :"))

if userInput>computerNumber:
    print("computer number",computerNumber)
    print("Your guess number is too high")
    
elif userInput<computerNumber:
    print("computer number",computerNumber)
    print("Your guess number is too low")

else:
    print("computer number",computerNumber)
    print("Your guess number is correct")
    