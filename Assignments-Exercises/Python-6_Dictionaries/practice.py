# dictionary = collection of {key:value} pairs.
#            = ordered and changeable. No duplicates.

capitals = {
              "USA": "Washington D.C.",
              "India": "New Delhi",
              "China": "Beijing",
              "Russia": "Moscow"            
           }

print("\n=========================== Dir: ===========================\n")
# To check the attributes and methods of the dictionary.
print(dir(capitals))

print("\n=========================== Help: ===========================\n")
# To display the in-depth description of attributes and methods.
# print(help(capitals))

print("\n=========================== Get Value: ===========================\n")

                  # Key
print(capitals.get("USA"))
print(capitals.get("India"))
print("If no value like \"Japan\":", capitals.get("Japan"))

print("\n=========================== If Else Practice: ===========================\n")


print("Japan:")
if capitals.get("Japan"):
    print("That capital exists.")
else:
    print("That capital doesn't exist.")

print("China:")
if capitals.get("China"):
    print("That capital exists.")
else:
    print("That capital doesn't exist.")

print("\n=========================== Update: ===========================\n")

                  # Key   :  Value
capitals.update({"Germany": "Berlin"})

print("Added Germany: ", capitals)

capitals.update({"USA": "Wash D.C."})

print("Updated \"USA\":", capitals)

print("\n=========================== Pop: ===========================\n")

capitals.pop("China")
print("Popped China:", capitals)

capitals.popitem()
print("popitem:", capitals)
     
print("\n=========================== Getting Keys: ===========================\n")

              # keys = object that resembles a list
keys = capitals.keys()
print("capitals.keys:", keys)

print("")
for key in capitals.keys():
    print(key)

print("\n=========================== Getting Values: ===========================\n")

values = capitals.values()
print("capitals.values:", values)

print("")
for value in capitals.values():
    print(value)

print("\n=========================== Getting Items: ===========================\n")

# items = returns dictionary object which resembles a 2D list of tuples
items = capitals.items()

print(items)

print("\nKey-Value Pair:\n")
for key, value in capitals.items():
    print(f"{key}: {value}")

print("\n=========================== Clear: ===========================\n")

capitals.clear()
print("Clear:", capitals)
