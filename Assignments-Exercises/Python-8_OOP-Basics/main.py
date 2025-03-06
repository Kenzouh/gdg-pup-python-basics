class Car:

    # __init__ = will construct objects for us.
                # arguments = parameters of a function.
                # self = object we're currently working on. 
    def __init__(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

     # Passing self is important to execute the method.
    def describe(self):
        # Grammatically correct: color, year, make, model, mileage
        print(f"This car is a {self.color} {self.year} {self.make} {self.model} that traveled {self.mileage} miles.")

    def start(self):
        print(f"The {self.model}'s engine is revving! Your {self.model} started!")

    def stop(self):
        print(f"You stepped on brakes. Your {self.model} stopped!")


           # make, model, year, color, mileage
nissan = Car("Nissan", "Altima", 2020, "Gold", 50000)

print("\nCar(\"Nissan\", \"Altima\", 2020, \"Gold\", 50000)\n")


print(f"Car manufacturer: {nissan.make}")
print(f"Car model: {nissan.model}")
print(f"Year made: {nissan.year}")
print(f"Color: {nissan.color}")
print(f"{nissan.model} miles traveled: {nissan.mileage}")

print("\nnissan.start()")
nissan.start()

print("\nnissan.stop()")
nissan.stop()

# ====================================================================

print("\n=============================\n")

ford = Car("Ford", "Mustang", 2021, "Black", 35000)

print("Car(\"Ford\", \"Mustang\", 2021, \"Black\", 35000)")

print(f"Car manufacturer: {ford.make}")
print(f"Car model: {ford.model}")
print(f"Year made: {ford.year}")
print(f"Color: {ford.color}")
print(f"{ford.model} miles traveled: {ford.mileage}")

print("\nford.start()")
ford.start()

print("\nford.stop()")
ford.stop()

# ===================== Summary of Tasks =====================
 
# 1. Create a "Car" class
# Attributes: "make", "model", "year"
# Method: describe


# add a constructor method __init__ to initialize "make", "model", "year"

# Create "describe" method (e.g., "This car is a 2020 Toyota Corolla.")

# Create an instance of the class

# Test and print

# - Try creating multiple instances of the `Car` class to test your program with different car details.
# - You can later extend this class by adding more attributes (like `color` or `mileage`) or more methods (like `start` or `stop`).