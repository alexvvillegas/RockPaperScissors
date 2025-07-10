# -------------------------------------------- 
# Day 2 Challenges
# -------------------------------------------- 

message = "Welcome to Day 4.\nToday we are learning about conditionals.\nLet's practice writing some conditionals of our own!"
print(message)
# -------------------------------------------- 

print("------------------- Challenge 1 -------------------")
# Can the person drive?
   # Prompt the user to enter their age.
   # Write an if-else statement that prints out whether the person can drive in your city, based solely on age
   # if the person is equal to or older than 16, print "You can drive!"
   # elif the person is equal to or older than 15, print "You may be able to get a permit"
   # else, print "You can't drive yet"

age = int(input("What is your age? "))
if age >= 16:
   print("you can drive!")
elif age >= 15:
   print("you may be able to get a permit")
else :age < 15
print("You cannot drive!")









# -------------------------------------------- 

print("------------------- Challenge 2 -------------------") 

# Who placed first?
   # Write conditional statements that checks which is the highest and prints the highest score

score1 = 180
score2 = 150
score3 = 200










# -------------------------------------------- 

print("------------------- Challenge 3 -------------------")

# One of the most common parts of our daily routine is checking the weather. 
# Our accessories are dependent on the temperature and conditions outside. 

# **** Challenge 3: Part 1 ****
# Write a conditional statement that checks the value of the weather variable 
# and prints out a weather report based on the current weather:
# rainy: "Bring an umbrella"
# sunny: "Wear a hat and sunglasses"
# snowing: "Wear gloves and a scarf ""

# Here's a variable to get you started:
weather = "rainy"
# Tip: Try changing the value of the weather variable to test your other conditions.









# -------------------------------------------- 

print("------------------- Challenge 4 -------------------")

# Prompt the user to enter the day of the week (1-7 representing Sunday - Saturday)
    # Write a set of conditionals that will examine day, which is a number from 1 to 7 
    # and print out the corresponding day of the week. 
    # Make sure to add a statement that accounts of any numbers out of range! 
    # i.e. any numbers greater than 7 should print "Error!"

# Uncomment the below line to get started:
# day = input("Enter a number from 1 - 7, where 1 is Sunday and 7 is Saturday: ")









# -------------------------------------------- 

print("------------------- Challenge 5 -------------------")

# A leap year is a calendar year that contains an additional day added 
   # to keep the calendar year synchronized with the astronomical year or seasonal year.
   # To calculate if a specific year is/was a leap year, you can follow the following steps:
     # 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
     # 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
     # 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
     # 4. The year is a leap year (it has 366 days). Print out "Leap year!"
     # 5. The year is not a leap year (it has 365 days). Print out "Sorry, not a leap year"

  # Those are a lot of conditions... But you got this!

# Hint: a number n is "evenly divisible" by 4 if the remainder is 0. That is, if n % 4 == 0

# Uncomment the below line to get started:
# year = input("Enter a year: ")


