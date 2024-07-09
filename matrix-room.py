def main():
    print("Welcome to the Matrix Escape Room!")
    print("You find yourself in a dimly lit room. A red pill lies on a table.")
    print("A sign reads, 'Choose wisely.'")
    choice = input("Will you take the red pill or the blue pill? (red/blue): ")

    if choice.lower() == "red":
        red_pill_riddle()
    elif choice.lower() == "blue":
        blue_pill_riddle()
    else:
        print("Invalid choice. Try again.")

def red_pill_riddle():
    print("\nYou've taken the red pill. The room shifts around you.")
    print("Suddenly, a holographic image appears:")
    print("What has keys but can't open locks?")
    answer = input("Your answer: ")
    if answer.lower() == "piano":
        print("Correct! The door opens, revealing the next room.")
    else:
        print("Incorrect. The walls close in, and you're trapped forever.")

def blue_pill_riddle():
    print("\nYou've taken the blue pill. Everything fades to black.")
    print("What is the one thing that can bend fate, yet remains invisible to the naked eye?")
    answer = input("Your answer: ")
    if answer.lower() == "the power of choice":
        print("Correct! The darkness lifts, and you move to the next room.")
    else:
        print("Incorrect. You remain in the void, lost and confused.")


