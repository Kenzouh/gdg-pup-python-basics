# My Python CRUD file with customized text file contents.


# ======================== Write Method ========================

print("\n========================== Write Method (w) ==========================\n")

print("with open(\"newfile.txt\", \"w\") as file:")
# No need to use try and except since it overwrites the file, and 
# not getting a mental breakdown if it exists.
# But for good practice, I included it

with open("newfile.txt", "w") as file:
    file.write("\"w\" method: I wrote this file using Python's write method (w).\n\n")

    file.write("I'm really grateful for the knowledge I learned in GDG club!\n")
    file.write("Thank you for teaching me Python file handling!")

print("\nFile successfully created/overwrote! :D")
print("Check out \"newfile.txt\". :) ")


# ======================== Create Method ========================

print("\n========================== Create Method (x) ==========================\n")

print("with open(\"newfile2.txt\", \"x\") as file:")

try:
    with open("newfile2.txt", "x") as file:
        file.write("\"x\" method: I wrote this file using Python's create method (x).")
        print("\nFile successfully created! :D")
except:
    print("\nFile already exists...")


# ======================== Read Method ========================

print("\n========================== Read Method (r) ==========================\n")

print("f = open(\"newfile.txt\")")
print("f.read()\n")

print("------------ newfile.txt ------------\n")

# No need to put "r" method after the file since "r" (read) is its default method.
f = open("newfile.txt")
print(f.read())

print("\n-------------------------------------\n")

print("f = open(\"newfile2.txt\", \"r\")")
print("f.read()\n")

print("------------ newfile2.txt ------------\n")

# "r" = You can put this if you want to make your program with more guide.
f = open("newfile2.txt", "r")
print(f.read())

print("\n-------------------------------------\n")


# ======================== Append Method ========================

try:
        
    with open("append.txt", "x") as file:
        file.write("This file is for appending practices.")

except:
    print("append.txt has been created.")
    print("Try running the code multiple times to see how the append function works.")

print("\n========================== Append Method (a) ==========================\n")

print("with open(\"append.txt\", \"a\") as file:\n")

with open("append.txt", "a") as file:
    file.write("\n\n\"a\" method: I updated the file using the append function.")
    file.write("\n\nWith Python, coding is limitless!")

print("------------ append.txt ------------\n")

f = open("append.txt")
print(f.read())

print("\n-------------------------------------\n\n")