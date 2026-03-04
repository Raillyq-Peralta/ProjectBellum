# ========== LIBRARIES ========== #
import json
import time
import random

# ========== FUNCTIONS ========== #
def game():
    time.sleep(1)
    print("Welcome to Project Bellum")
    time.sleep(1.5)
    print("You're a single middle aged man who works a regular 9-5 office job and its been a long day at work.")
    time.sleep(4.5)
    print("It's time to go home, you decide to take the bus home and you fall asleep because of how tired you are.")









def tutorial():
    print("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚")
    print("                                   HOW TO PLAY                                      ")
    print("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚")
    print("                                                                                    ")
    print("")

# ========== MAIN GAME LOOP ========== #
while True:
    try:
        # Opens the JSON in read mode
        with open("player_data.json", 'r') as file:
            # Loads the JSON data from the file
            data = json.load(file)

        # ========== MAIN MENU ========== #
        while True:
            print("▣▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▣")
            print("▥                                 PROJECT BELLUM                                    ▥")
            print("▣▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▣")
            print("                                                                                       ")
            print("                          ▣▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▣                              ")
            print("                          ▥            PLAY            ▥                              ")
            print("                          ▣▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▣                              ")
            print("                                        [1]                                            ")
            print("                                                                                       ")
            print("                          ▣▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▣                              ")
            print("                          ▥         HOW TO PLAY        ▥                              ")
            print("                          ▣▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▣                              ")
            print("                                        [2]                                            ")
            print("                                                                                       ")
            print("                          ▣▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▣                              ")
            print("                          ▥            QUIT            ▥                              ")
            print("                          ▣▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▣                              ")
            print("                                        [3]                                            ")
            print("                                                                                       ")

            choice = input("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚"
                           "\nCOMMAND: ")

            if choice == "1":
                game()
            elif choice == "2":
                tutorial()
            elif choice == "3":
                quit()
            else:
                print("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚")
                print("INVALID INPUT INVALID INPUT INVALID INPUT INVALID INPUT INVALID INPUT INVALID INPUT")
                print("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚")
                print()

    except FileNotFoundError:
        print("Error: The file 'data.json' was not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")