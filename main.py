import random
# generating random number between
x = random.randint(0, 5)
print("You've only 5 chances to guess the integer!")

# Initializing the number of guesses.
count = 0

while count < 5:
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	# Condition testing
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

if count ==5:
	print("\nThe number is: " , x)
	print("\tBetter Luck Next time!")

