# Youtube Video [https://youtu.be/t8pPdKYpowI]

# IDE = Integrated Development Environment
# Print(int)
print("INTEGER NUMBER:")
print(100)

# Print(float)
print("FLOAT NUMBER:")
print(100.01)

# Print("string")
print("STRING CARAC:")
print("Hello World")

# Calculation of minutes for 20 days
print("20 days in seconds are:")
print(20 * 24 * 60)

# String concatenation
print("20 days are " + str(20 * 24 * 60) + " seconds")

# This string concatenation only works on python 3 or superior
print(f"30 days are {30 * 24 * 60} seconds")

# Using Variables => name = value
# Type1
var_1 = 40 * 24 * 60
und = "seconds"
print(f"40 days are {var_1} {und}")

# Type2
var_2 = 50 * 24 * 60
und = "seconds"
print("50 days are " + str(var_2) + " " + und)

#  There's some keywords that are reserved in Python:
#  and, as, assert, break, class, continue, def, del, elif, else
#  except, finally, false, for, from, global, if, import, in, is, lambda, nonlocal, none
#  not, or, pass, raise, return, true, try, with, while, yield

# Function

# Variables

day_hours = 24
name_of_unit = "hours"


# Creating a function
def days_to_hours():
    # This function transforms day unit to hour
    print(f"20 days are {20 * day_hours} {name_of_unit}")
    print("Sweet, it's correctly! oh yeah")


# Calling the Function created
days_to_hours()

# Pep8 tells how must be written the code, STUDY FOR LATER ON!

# Setting function parameters
# Function

# Global Variables
day_hours2 = 24
name_of_unit2 = "hours"


# Creating a function with two local variables
def days_to_hours(number_of_days, message):
    # This function transforms day unit to hour and prints a message
    print(f"{number_of_days} days are {number_of_days * day_hours2} {name_of_unit2}")
    print(message)


# Calling the Function created with a number of days and the message
days_to_hours(35, "Cool!")
days_to_hours(70, "Awesome!")
days_to_hours(140, "Sweet!")
days_to_hours(280, "Oh yeah!")


# Learning Scope
# A variable is only available from inside the region it is created
# Global Scope = variables available from within any Scope

def scope_check(num_of_days):
    my_var = "variable inside function"
    print(name_of_unit)  # global variables
    print(num_of_days)  # local variable
    print(my_var)


scope_check(66)  # the 66 will it apear in num_of_days [local variables - line 87/90]

# Learning Inputs
# Used to ask the user for an input
user_input = input("First Question: Enter a value for a number of days and I will convert it to seconds!\n")

# Creating a function with two local variables
def days_to_hours3(number_of_days, message):
    # This function transforms day unit to hour and prints a message
    print(f"{number_of_days} days are {int(number_of_days) * 24 * 60} seconds")
    print(message)
print(f"{int(user_input)*24*60} seconds")
#or
user_input2 = input("Second Question: Enter a value for a number of days and I will convert it to seconds!\n")
# Calling the Function created with a number of days and the message
days_to_hours3(user_input2, "DEU CERTO! UHUL")

# We as programmers when we allow user input a value, we must restrict them and validate what they provided as input.


# Learning If/else statements

# Creating a function with two local variables
def days_to_hours4(number_of_days):
    #If operators: == equal / =! not igual / > grater / < less than / >= greater than of equal to / <= less than or equal to
    if number_of_days > 0:
        return f"{number_of_days} days are {number_of_days * 24 * 60} seconds"
    elif number_of_days == 0:
        return "Zero days ins't a proper answer!"
    else:
        return "A negative number isn't a proper answer!"

user_input3 = input("Third Question: Enter a value for a number of days and I will convert it to seconds!\n")
# Calling the Function created with a number of days and the message
days_to_hours3(user_input3, "DEU CERTO! UHUL")