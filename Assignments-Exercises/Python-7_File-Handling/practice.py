

txt_data = "I like pizza!"

            # Outputs in the root.
file_path = "ouput.txt"

# with = closes the file for you automatically

try:
                        # w = writes file and overwrites the file if it's created already.
                        # x = writes if the file doesn't exist
                        # a = appending. Adds text, and doesn't overwrite the file.
    with open(file_path, "w") as file:
        # file = object
        file.write("\n" + txt_data)
        print(f"txt file '{file_path}' was created")
        pass

except FileExistsError: # So the program won't be interrupted if the file is created already.
    print("That file already exists!")
    
