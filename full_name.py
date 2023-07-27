full_name=(input("Enter your full name:"))
if (len)(full_name)==0:
    print("You haven't entereted anything.")
elif (len)(full_name)<4:
    print("You have entered less than four character. Please make sure you've entered both your forename and surname.")
elif (len)(full_name)>25:
    print("You have entered more than 25 character. Please make sure you've entered only your forename and surname.")
else:
    print("Thank you for entering your full name.")