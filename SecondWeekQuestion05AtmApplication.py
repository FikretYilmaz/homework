account= float(1000)
print("You Have",account, "€ in Your Account")
operation= int(input("Press 1 to check balance\nPress 2 to make a deposit\nPress 3 to withdraw money")) 
if operation == 1:
	print("You Have",account,"€ in Your Account")
if operation ==2:
	deposit=float(input("Please Enter Value of You Want to Deposit Into Your Account"))
	depositMoney = account+deposit
	print("You Have",depositMoney,"€ In You Account")
if operation == 3:
	withdraw = float(input("Please Enter Value of Your Withdraw Money "))
	withdrawMoney = account-withdraw
	if withdrawMoney< 0:
		print("It is Impossible! Please Check Value of Your Withdraw Money")
	else:
		print("You Have",withdrawMoney,"€ In You Account") 

