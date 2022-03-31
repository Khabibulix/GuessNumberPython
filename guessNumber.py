import random

#ask the range to user and defend against stupid user

topRange = input("Choose the range: ")
if topRange.isdigit():
	topRange = int(topRange)
	if topRange <= 0:
		print("Type a number larger than zero, next time, dummy!")
		quit()
else:
	print("Type a number, next time, dummy!")
	quit()

#generate nummber between 0 and user input

randomNumber = random.randint(0, topRange)
guesses = 0


while True:
	userGuess = input("\nMake a number guess: ")
	guesses += 1

	if userGuess.isdigit():
		userGuess = int(userGuess)
	else:
		print("Type a number, next time, dummy!")
		continue
	
	if userGuess == randomNumber:
		print("\nYou got this! Well Done! \n")
		break
	
	elif userGuess > randomNumber:
		print("\nThe number you are searching is smaller!")
	else:
		print("\nThe number you are searching is greater!")

print("You got it in", guesses, "guesses")