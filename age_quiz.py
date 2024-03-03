# request user input their age as a whole number and store as variable "age"
age_input = input("Please enter your age as a whole number between 1 and 100:")
# convert age input to integer
user_age = int(age_input)

# create conditionals starting with the equal to 21 conditional, then the 
# age conditionals starting with the highest age number conditional and descending in order

if user_age == 21: #for users aged 21
    print("Congrats on your 21st!")
elif user_age > 100: #for users older than 100
    print("Sorry, you're dead.")
elif user_age >= 65: #for users 65 years old and older
    print("Enjoy your retirement!")
elif user_age >= 40: #for users 40 years old and older
    print("You're over the hill.")
elif user_age < 13: #for users under 13
    print("You qualify for the kiddie discount.")

else: #for user who are in another age category than the ones above
    print("Age is but a number.") 