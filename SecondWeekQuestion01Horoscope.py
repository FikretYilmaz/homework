day= input("Please Enter Your Day of Birth: ")
month= input("Please Enter Your Month of Birth:  ")
if bool(day)==False or bool(month) ==False or day==" " or month==" ":
	print("You Can Not Enter Gap!")
else:
	day=int(day)
	month=int(month)
	if (month==3 and 21<=(day)<=31) or(month==4 and 1<=day<=21):
		print("Your horoscope is Aries")
	elif (month==4 and 22<=day<=30) or(month==5 and 1<=day<=21):
		print("Your horoscope is Taurus")
	elif (month==5 and 22<=day<=31) or(month==6 and 1<=day<=22):
		print("Your horoscope is Gemini")
	elif (month==6 and 23<=day<=30) or(month==7 and 1<=day<=22):
		print("Your horoscope is Crap")
	elif (month==7 and 23<=day<=31) or(month==8 and 1<=day<=22):
		print("Your horoscope is Leo")
	elif (month==8 and 23<=day<=31) or(month==9 and 1<=day<=22):
		print("Your horoscope is Virgo")		
	elif (month==9 and 23<=day<=30) or(month==10 and 1<=day<=22):
		print("Your horoscope is Scales")
	elif (month==10 and 23<=day<=31) or(month==11 and 1<=day<=21):
		print("Your horoscope is Scorpion")
	elif (month==11 and 22<=day<=30) or(month==12 and 1<=day<=22):
		print("Your horoscope is Sagittarius")
	elif (month==12 and 23<=day<=31) or(month==1 and 1<=day<=21):
		print("Your horoscope is Capricorn")
	elif (month==1 and 22<=day<=31) or(month==2 and 1<=day<=19):
		print("Your horoscope is Aquarius")
	elif (month==2 and 20<=day<=29) or(month==3 and 1<=day<=20):
		print("Your horoscope is Fishes")
	else:
		print("Please Check The Values You Entered ")
