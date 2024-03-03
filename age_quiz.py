# request user input their age as a whole number and store as variable "age"
age_input = input("Please enter your age as a whole number between 1 and 100:")
# convert age input to integer
user_age = int(age_input)

# create conditionals starting with the equal to 21 conditional, then the 
# age conditionals starting with the highest age number conditional and descending in order

if user_age == 21:
    print("Congrats on your 21st!")
elif user_age > 100:
    print("Sorry, you're dead.")
elif user_age >= 65:
    print("Enjoy your retirement!")
elif user_age >= 40:
    print("You're over the hill.")
elif user_age < 13:
    print("You qualify for the kiddie discount.")
# Create an else conditional for all the other age input values
else:
    print("Age is but a number.")