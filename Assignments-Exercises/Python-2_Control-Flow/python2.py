try:
    numerator = int(input("Enter a number to divide:"))
    denominator = int(input("Enter a number to divide by:"))

    result = numerator / denominator

except ZeroDivisionError as e:
    print(e) # Optional. Prints out the problem
    print("You can't divide by 0.")

except ValueError as e:
    print(e)
    print("Enter only numbers please.")

# Good practice  = Have more than 1 except block
except Exception as e:
   print(e)
   print("something went wrong :(")

else:
    print(result)

finally: # Whether we not catch an exception, this will always execute within this.
    
    print("This will always execute.")