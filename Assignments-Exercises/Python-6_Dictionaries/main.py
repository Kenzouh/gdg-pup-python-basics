# NOTE: I made main2.py for practicing on my own with my own dictionary.

# Creating a dictionary

    # name: Sparky, age: 25

gdg_dictionary = {
                    "name": "Sparky", 
                    "age": 25
                 }

print("gdg_dictionary:\n", gdg_dictionary)

# Add new key-value pair
    
    # city: "New York"
gdg_dictionary.update({"city": "New York"})

print("\nAdded city: New York:\n", gdg_dictionary)



# Update an existing key-value pair

    # update age to 26
gdg_dictionary.update({"age": 26})

print("\nUpdated age:\n", gdg_dictionary)

# Removing a key-value pair

    #del or pop()
    # Remove the age key  

gdg_dictionary.pop("age")
print("\nDeleted age key:\n", gdg_dictionary)

# Display the dictionary

print("\nFinal output:")
print(gdg_dictionary)