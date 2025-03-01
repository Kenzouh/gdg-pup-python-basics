# Function that greets the user.
def create_greeting(name, age, fave_food, year_level):

    if year_level == 1:
        return f"\nHello, {name}! You are a {year_level}st year level at the age of {age}!\nYour favorite food is {fave_food}! Welcome to college! :D"

    elif year_level == 2:
        return f"\nHello, {name}! You are a {year_level}nd year level at the age of {age}!\nYour favorite food is {fave_food}! How's college life? :)"

    elif year_level == 3:
        return f"\nHello, {name}! You are a {year_level}nd year level at the age of {age}!\nYour favorite food is {fave_food}! 2 more years to go! :D"

    elif year_level == 4:
        return f"\nHello, {name}! You are a {year_level}nd year level at the age of {age}!\nYour favorite food is {fave_food}! Wow! You're almost done in college! :D"

    else:
        return f"\nHello, {name}! You are currently year {year_level} at the age of {age}!\nYour favorite food is {fave_food}! Wow! Still studying! Keep it up! :D"

try:
    name = str(input("Enter your name: "))

        # Checks if the name is a number or not
    if name.isdigit():
        raise ValueError("Invalid input: Please enter a valid name.")

    # =============================================================

    age = int(input("How old are you: "))

    if age < 0: # If negative number.
        raise ValueError("Invalid input: Age cannot be a negative number.")

    # =============================================================

    fave_food = input("What is your favorite food: ")

    if fave_food.isdigit():
        raise ValueError("Invalid input: Food cannot be a number.")

    # =============================================================

    year_level = int(input("What year level are you in: "))

    if year_level < 1: # Runs if the user inputted 0 or negative year levels.
        raise ValueError("Year levels can't be less than 1. :(")
    
    # Prints out the greeting function.
    print(create_greeting(name, age, fave_food, year_level))


except ValueError as e: 
    print("")
    print(e)
    
     # str(e) = converts the exception message into string.
    if str(e) == "Invalid input: Please enter a valid name.":
        print("Name must consist of letters.")

    elif str(e) == "Invalid input: Age cannot be a negative number.":
        print("Age must be a positive number.")

    elif str(e) == "Invalid input: Food cannot be a number.":
        print("Food must consist of letters.")

    elif str(e) == "Year levels can't be less than 1. :(":
        print("Year levels should be 1 onwards.")

    else:
        print("Please, fix your errors. :(")