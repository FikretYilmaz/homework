dataa=float(input("""
If You Want To Return Mile To KM Please Enter 1
If You Want To Return KM To Mile Please Enter 2
If You Want To Exit Please Enter 3
"""))

if dataa == 3:
    print("Bye! See You Later...")
elif dataa == 1:
	mile=float(input("Please Enter Length In Miles: "))
	kmTransformation = mile*1.609344
	print("Your Distance In Kilometer is",kmTransformation,)
elif dataa == 2:
	km=float(input("Please Enter Lenght in Kilometer: "))
	mileTransformation = km/1.609344
	print("Your Distance In Mile is",mileTransformation,)
else:
	print("Please Check Your Data")
	


