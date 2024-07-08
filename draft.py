def welcome():
    print("Welcome to the Virtual Escape Room!")
    print("You find yourself in a dimly lit hallway.")
    print("There are five doors ahead. Which room would you like to explore?")
    room_choice = input("Enter the number 1-5: ")

    # Handle room selection
    if room_choice == "1":
        room_1()
    elif room_choice == "2":
        room_2()
    elif room_choice == "3":
        room_3()
    elif room_choice == "4":
        room_4()
    elif room_choice == "5":
        room_5()
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")


welcome()
