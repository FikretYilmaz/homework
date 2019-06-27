midterm1 = (input("Please Enter Your First Midterm Score: "))
midterm2 = (input("Please Enter Your Second Midterm Score: "))
finalNote =(input("Please Enter Your Final Score: "))

if bool(midterm1)== True and bool(midterm2) == True and bool(finalNote) == True and midterm1!=" " and midterm2!=" " and finalNote!=" ":
    midterm1=float(midterm1)
    midterm2=float(midterm2)
    finalNote=float(finalNote)
    noteCalculate = midterm1 * 0.3 + midterm2 * 0.3 + finalNote * 0.4
    if midterm1 > 100 or midterm2 > 100 or finalNote > 100 or midterm1 < 0 or midterm2 < 0 or finalNote < 0:
        print("Your Midterms Scores and Final Scores Can Be Up To 100")
    elif noteCalculate >= 90:
        print("Your Total Score is >=", noteCalculate, "-----> AA")
    elif 90 > noteCalculate >= 85:
        print("Your Total Score is >=", noteCalculate, "-----> BA")
    elif 85 > noteCalculate >= 80:
        print("Your Total Score is >=", noteCalculate, "-----> BB")
    elif 80 > noteCalculate >= 75:
        print("Your Total Score is >=", noteCalculate, "-----> CB")
    elif 75 > noteCalculate >= 70:
        print("Your Total Score is >=", noteCalculate, "-----> CC")
    elif 70 > noteCalculate >= 65:
        print("Your Total Score is >=", noteCalculate, "-----> DC")
    elif 65 > noteCalculate >= 60:
        print("Your Total Score is >=", noteCalculate, "-----> DD")
    elif 60 > noteCalculate >= 55:
        print("Your Total Score is >=", noteCalculate, "-----> FD")
    elif 55 > noteCalculate:
        print("Your Total Score is >=", noteCalculate, "-----> FF")
else:
    print("You Couldn't Enter Gap")