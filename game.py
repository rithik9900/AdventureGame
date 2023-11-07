import time

def introduction():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a dark and mysterious forest. The moon casts eerie shadows through the trees.")
    time.sleep(2)
    print("You hear the sound of a running stream nearby and the faint hoot of an owl in the distance.")
    time.sleep(2)
    print("You can see two paths: a 'left' path that leads deeper into the forest and a 'right' path that goes uphill.")
    time.sleep(2)
    start_game()

def start_game():
    print("\nWhat's your choice? 'left' or 'right'?")
    choice = input().lower()
    
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")
        start_game()

def left_path():
    print("\nYou follow the left path and discover a hidden glade filled with fireflies.")
    time.sleep(2)
    print("In the center of the glade, you find a treasure chest. Do you want to 'open' it or 'leave' it?")
    choice = input().lower()
    
    if choice == "open":
        print("\nCongratulations! You found a chest filled with gold and precious gems.")
        play_again()
    elif choice == "leave":
        print("\nYou decide to leave the treasure chest behind and continue your journey.")
        start_game()
    else:
        print("Invalid choice. Please enter 'open' or 'leave'.")
        left_path()

def right_path():
    print("\nYou take the right path, which leads to a steep hill.")
    time.sleep(2)
    print("At the top of the hill, you encounter a fierce dragon. Do you want to 'fight' or 'run'?")
    choice = input().lower()
    
    if choice == "fight":
        print("\nWith bravery and skill, you defeat the dragon and continue your adventure.")
        play_again()
    elif choice == "run":
        print("\nYou wisely run away from the dragon and find yourself back at the starting point.")
        start_game()
    else:
        print("Invalid choice. Please enter 'fight' or 'run'.")
        right_path()

def play_again():
    print("\nDo you want to play again? 'yes' or 'no'?")
    choice = input().lower()
    
    if choice == "yes":
        introduction()
    elif choice == "no":
        print("\nThanks for playing the Text Adventure Game! Goodbye.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        play_again()

introduction()
