# made improvements from code in the video

import random

rand_num = random.randint(1, 10)
guessed_nums = []
allowed_guesses = 5

def higher_or_lower(guess):
	if guess < rand_num:
		return "higher"
	else:
		return "lower"

def guesses_remaining(tries):
	if allowed_guesses - tries != 0:
		return "You have " + str(allowed_guesses - tries) + " tries left."
	else:
		return ""


while len(guessed_nums) < allowed_guesses:
	guess = input("Guess a number between 1 and 10: ")

	try:
		player_num = int(guess)
	except:
		print("That's not a whole number. Please try again.")
		continue

	if not player_num > 0 or not player_num < 11:
		print("That number isn't between 1 and 10. Please try again.")
		continue

	guessed_nums.append(player_num)

	if player_num == rand_num:
		print("You win! My number was {}.".format(rand_num))
		print("It took you {} tries.".format(len(guessed_nums)))
		break
	else:
		print("Nope! My number is {} than {}. {}".
			format(
				higher_or_lower(player_num), 
				player_num, 
				guesses_remaining(len(guessed_nums))))
	continue

if not rand_num in guessed_nums:
	print("Sorry, You've run out of tries. My number was {}.".format(rand_num))



