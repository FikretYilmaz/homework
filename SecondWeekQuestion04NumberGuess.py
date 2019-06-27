guessNumber =10
guess1 	= int(input("Please Estimate a Number Between 0-10 "))

if guess1 == guessNumber:
	print("Congratulations! You Won on Your First Try ","\u2605"*3,)
elif guess1 != guessNumber:
	guess2 	= int(input("This is Your Second Chance! Please Estimate a Number Between 0-10 "))
	if guess2== guessNumber:
		print("Congratulations You Won Your Second Try","\u2605"*3,)
	elif guess2!=guessNumber:
		guess3 	= int(input("This is Your Third Chance! Please Estimate a Number Between 0-10 "))
		if guess3== guessNumber:
			print("Congratulations You Won on Your Third Try","\u2605"*2,)
		elif guess3 != guessNumber:
			guess4 	= int(input("This is Your Fourth Chance! Please Estimate a Number Between 0-10 "))
			if guess4 == guessNumber:
				print("Congratulations You Won  on Your Fourth Try","\u2605"*2,)
			elif guess4 != guessNumber:
				guess5 	= int(input("This is Your Last Chance! Please Estimate a Number Between 0-10 "))
				if guess5== guessNumber:
					print("Congratulations You Won on Your Last Chance","\u2605"*1,)
				elif guess5 != guessNumber:
					print("Your Guess Right is Over. Sorry You Couldn't Guess")