# request user input their age as a whole number and store as variable "age"
age = input("Please enter your age as a whole number between 1 and 100:")
# convert age input to integer
age = int(age)
# create conditionals starting with the equal to 21 conditional, then the age conditionals starting with the highest age number conditional and descending in order
if age == 21:
    print("Congrats on your 21st!")
elif age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age < 13:
    print("You qualify for the kiddie discount.")
# Create an else conditional for all the other age input values
else:
    print("Age is but a number.")