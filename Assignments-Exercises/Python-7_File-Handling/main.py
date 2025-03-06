# My other code that creates a file called "newfile.txt" is "main2.py". 
# Kindly check "main2.py" out! Thank you!

# ======================== Write Method ========================

# with statement = closes the file for you automatically
with open("sample.txt", "w") as file:
      file.write("Hello, this is a test file.\n")
      file.write("Python file handling is easy and fun!")

# ======================== Create Method ========================

try:
    
    with open("sample2.txt", "x") as file:
      file.write("I made a file in Python!\n")
      file.write("I used x (create) method for this one!")
            
except:
    print("FILE ALREADY EXISTS!")

print("\n")

# ======================== Read Method ========================

# Read method 1 (no need to put "r" because the method is defaulted to read):
f = open("sample.txt")
print(f.read())
print("\n")

# Read method 2:
f = open("sample2.txt", "r")
print(f.read())
print("\n")

# ======================== Append Method ========================

with open("sample2.txt", "a") as file:
    file.write("\nI appended this line!")

f = open("sample2.txt")
print(f.read())


# ======================== Summary of the task ========================

# 2 operations:

  # Read
  # Write

# Create:
  # Opens the file
  # Reads the file contents
  # Displays the contents
  # Overwrite data


# Creates a file
# f = open("sample.txt", "x")

















