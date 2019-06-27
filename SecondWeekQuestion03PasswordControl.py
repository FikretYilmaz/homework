passControl=open('SecondWeekPassControl.txt','w')
userName= input("""
Please Enter Your Username(Note: the number of characters must be between
3 and 18 and should not contain numbers)
""")
charactersOfUserName= len(userName)
password = input("""
	Please Enter Your Password(Note: Your Password Can Not Be Shorter
	Than 6 Characters Or Longer Than 12 Characters)
	""")

if ("1" in (userName) or "2" in (userName) or "3" in (userName) or "4" in (userName) or "5" in (userName) or "6" in (userName) or "7" in (userName) or "8" in (userName) or "9" in (userName) or "0" in (userName)):
	print("You Can Not Use Numeric Values In Your Username")
elif((charactersOfUserName<=3) or (charactersOfUserName>=18)):
	print("The Number of Characters Must Be Between 3 and 18")
elif len(password)<6 or len(password)>12:
	print("Your Password Can Not Be Shorter Than 6 Characters Or Longer Than 12 Characters")
else:
	print("Your Username is=",userName, "and,\nYour Password is =",password,file=passControl)
	passControl.close()
