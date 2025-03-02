# Dictionary with fictional shop names (keys) and products (values).
city_specialties = {
          # Fictional restaurant : Products Specialties
                     "Happy Shop": "Choco Ice Cream",
                     "Donutz": "Cream Donut",
                     "Joy King": "Cheeseburger",
                   }

print("City Specialties:\n", city_specialties)

# ================================================================================

print("\n=========================== Adding: ===========================\n")

# Adding Method 1:
city_specialties.update({"Royal Knights": "Pesto Pork Tenderloin"})
print("Added \"Royal Knights\":\n", city_specialties)

# Add Method 2:
city_specialties["Fish Kingdom"] = "Swordfish"
print("\nAdded \"Fish Kingdom\":\n", city_specialties)

# ================================================================================

print("\n=========================== Updating: ===========================\n")

# Updating method 1:
city_specialties.update({"Happy Shop": "Bread"})
print("Updated the value of \"Happy Shop\":\n", city_specialties)

# Updating method 2:
city_specialties["Fish Kingdom"] = "Fish Nuggets"
print("\nUpdated the value of \"Fish Kingdom\":\n", city_specialties)

# ================================================================================

print("\n=========================== Deletion: ===========================\n")

# Deletion Method 1: Specific
city_specialties.pop("Happy Shop")
print("Deleted \"Happy Shop\":\n", city_specialties)

# Deletion Method 2: Popping the end.
city_specialties.popitem()
print("\npopitem:\n", city_specialties)

# Deletion Method 3:
del city_specialties["Joy King"]
print("\ndel \"Joy King\":\n", city_specialties)

# ================================================================================

print("\n=========================== Printing The Updated List: ===========================\n")

print("Updated List:", city_specialties)

keys = city_specialties.keys()
print("\nKeys:")

for keys in city_specialties.keys():
    print(keys)

values = city_specialties.values()
print("\nValues:")

for values in city_specialties.values():
    print(values)