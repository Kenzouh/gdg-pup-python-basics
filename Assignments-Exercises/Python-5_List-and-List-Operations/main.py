# Food, Drinks, Milks and other stuff in the fridge. 
fridge_contents = ["Milk", "Mustard", "Cola", "Choco Syrup", "Yoghurt"]

print("Fridge Contents List:", fridge_contents)


try:

    while(True):

        print("\n================== Choose below =================")
        print("|| [1] = To print the list                     ||") # Finished
        print("|| [2] = To select an index to view an element ||") # TODO 
        print("|| [3] = To append an item in the list         ||") # Finished
        print("|| [4] = To remove an item in the list         ||") # Finished
        print("|| [5] = To sort the list                      ||") # Finished
        print("|| [N] = To exit the program                   ||") # Finished
        print("=================================================\n")

        choice = input("Your choice: ").strip() # Removes spaces

                # Makes the user input uppercase.
        if choice.upper() == "N":
            print("Exiting the program...")
            break   

        try:

            choice = int(choice)

            if choice == 1:
                print("\nFridge Content List:",  fridge_contents)
            
            # ==========================================================================================

            elif choice == 2: # TODO
                
                while True:
                                    # Counts how many items are in the list
                    fridge_content = len(fridge_contents) # It'll output "5", so "-1" for indexing.

                    try:


                        pick = int(input(f"Choose a number from [0–{fridge_content - 1}]:"))

                        if 0 <= pick < fridge_content:

                            item_to_pick = fridge_contents[pick]

                            print(f"\nItem {pick}: {fridge_contents[pick]}")
                            break

                        else:
                            print(f"\nInvalid input: Enter a number of range [0–{fridge_content -1}] only:")
                            continue

                    except ValueError:
                        print("\nInvalid input: Pleae, enter a valid number.")

            # ==========================================================================================

            elif choice == 3:

                while True:
                         
                    add_item = input("Add another fridge content: ")

                    if add_item.isdigit():
                        print("\nInvalid input: Please, enter characters only.")
                        continue
                        
                    fridge_contents.append(add_item)

                    print(f"\nItem [{add_item}] successfully updated!")
                    break
                
            # ==========================================================================================
            
            elif choice == 4:

                while True:

                    fridge_content = len(fridge_contents)

                    try:

                        remove_item = int(input(f"Remove item [0–{fridge_content -1}]:"))

                         # 0 <= remove_item = Ensures the user didn't enter a negative numnber.
                              # remove_item < fridge_content = Ensures index is less than the length of the list.
                        if 0 <= remove_item < fridge_content:

                            item_to_remove = fridge_contents[remove_item]
                                            # Not working since int is not subscriptable
                            # print(f"\nItem {fridge_content[remove_item]} has been removed!")
                            print(f"\nItem [{item_to_remove}] has been removed!")
                            fridge_contents.remove(item_to_remove)
                            break
                        
                        else:  
                            print(f"\nInvalid input: Enter a number of range [0–{fridge_content -1}] only:")

                    except ValueError:
                        print("\nInvalid input: Please, enter a valid number.")



            # ==========================================================================================

            elif choice == 5:

                while True: # To loop until the user chooses 1 or 2

                    print("\nPick [1] = order the list in Ascending order")
                    print("Pick [2] = order the list in Descending order.\n")

                    try:

                        order_choice = int(input("Your choice: "))

                    except ValueError:
                        print("Invalid input! Please, enter [1] or [2] only.")
                        continue # Lets the program go back to the start of the loop.

                    if order_choice == 1:
                        
                        fridge_contents.sort()

                        print("\nList successfully sorted in ascending order!")
                        print("Fridge Contents List: ", fridge_contents)

                        break # Exit the loop.

                    elif order_choice == 2:

                        fridge_contents.sort(reverse = True)

                        print("\nList successfully sorted in descending order!")
                        print("Fridge Contents List: ", fridge_contents)

                        break # Exits the loop.

                    else:
                        print("\bInvalid choice! Please, pick [1] or [2] only.")

            # ==========================================================================================
            
                
        except ValueError:
            print("Invalid input. Please, enter numbers 1–5 or N to exit.")

except ValueError as e:
    print(e)