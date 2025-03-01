try:

    age = int(input("Please, enter your age: "))

    print("Your age is:", age, "\n")
    
    if age < 0: # Raising an error-handler for negative unmbers.
        raise ValueError("Invalid input: Age cannot be negative.")
    
    elif age < 13:
        print("You are categorized as: Child")

    elif age < 20:
        print("You are categorized as: Teenager")

    elif age < 60:
        print("You are categorized as: Adult!")

    elif age >= 60:
        print("You are categorized as: Senior")

# Outputs during an error.
except ValueError as e:

    # Only outputs if the input is a string and not the same value error as the negative number input.
    if str(e) != "Invalid input: Age cannot be negative.":

        print(f"\nError: {e}\n")
        print("Invalid input: Age cannot be a non-number nor a string.\n")

    # Outside the if block, so this outputs for both negative and string inputs.
    print("==========================================")
    print("|| Please, enter positive numbers only. ||")
    print("==========================================")
    
# Outputs after the program. Just practicing the "finally" keyword.
finally:
    print("\nThank you for using my program! :D")