data = input("""
Please Type "triangle" if The Shape You Want to Find
is Triangle, or "square" if It is Square.
""")

if data == "triangle":
	side1 = input("Please Enter Side1: ")
	side2 = input("Please Enter Side2: ")
	side3 = input("Please Enter Side3: ")
	if (bool(side1) == True and bool(side2) == True and bool(side3) == True and side1 !=" " and side2 !=" " and side3 !=" "):
		side1 = int(side1)
		side2 = int(side2)
		side3 = int(side3)	
		if (side1 < abs(side2 - side3) or side2 < abs(side1 - side3) or side3 < abs(side1 - side2) or side1 > (side2 + side3) or side2 > (side1 + side3) or side3 > (side1 + side2)):
			print("Tis is Not Triangle")
		elif (side1 == side2 == side3):
			print("This is an Equilateral Triangle") 
		elif ((side1 == side2) or (side1 == side3) or (side2 == side3)):
			print("This is an Isosceles Triangle")
		else:
			print("This is Normal Triangle")
	else:
		print("You Can Not Enter Gap")		
elif data == "square":
	side1 = input("Please Enter Side1: ")
	side2 = input("Please Enter Side2: ")
	side3 = input("Please Enter Side3: ")
	side4 = input("Please Enter Side3: ")
	if (bool(side1) == True and bool(side2) == True and bool(side3) == True and bool(side4) == True and side1 !=" " and side2 !=" " and side3 !=" " and side4 !=" "):
		side1 = int(side1)
		side2 = int(side2)
		side3 = int(side3)
		side4 = int(side4)
		if (side1 == side2 == side3 == side4):
			print("Your Sahepe is Square")
		elif(side1 == side3) and (side2 == side4):
			print("Your Shape is Rectangle")
		elif (side1 != side2 != side3 != side4):
			print("Your Shape is Assorted Rectangle")
		else:
			print("This is Not Square!")
	else:
		print("You Can Not Enter Gap")