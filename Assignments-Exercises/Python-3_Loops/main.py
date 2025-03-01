fave_foods = ["Takoyaki", "Omelette", "Ferrero Rocher", "Ice cream", "Spinach Pizza",
              "Sushi", "Spring rolls", "Beef steak", "Eggs", "Skewered foods"]

# Iterating through the list using for loop.   
for i in range(len(fave_foods)):

                     # i = index number which increments each loop.
                         # 1 = tells the program to start at 1, then increment each loop.

                          # The item number is based on the number which increments each turn.  
    
    print(f"Fave food {i + 1}: {fave_foods[i]}")


try:
    # Countdown using while loop.

    start_num = int(input("\nEnter starting number (e.g. 20): "))

    print("")

    if start_num <= 0:
        raise ValueError("Number must be a positive integer that is 1 or higher.")
    
    # For Looping Decrementation.
    i = 1

    while start_num >= i:
        print(start_num)

        start_num -= 1

        # Prints out if the countdown is down to "1"
        if start_num == 0:
            print("Countdown complete!")

except ValueError as e:
    print(e)
    print("Invalid input: Please enter a positive integer.")