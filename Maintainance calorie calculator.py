print("Calculate your Maintainance Calories :)")

Age = input("\nEnter Your Age: ")

height = input("\nEnter your height in cm :")
weight = input("\nEnter your weight in kg :")


BMR = int(10*int(weight) + 6.25*float(height) - 5*int(Age) + 5)




print("Your Basal Metabolic Rate is : " + str(BMR))

print("\nThank You for using my Calculator :)")