# ========== LIBRARIES ========== #
import json
import time
import sys
import random
try:
    import keyboard
except ImportError:
    print("Error: Module 'keyboard' not found. Please install it and try again.")
    quit()

# ========== JSON INTERPRETING ========== #
with open("player_data.json", "r") as file:
    player_data = json.load(file)

with open("information.json", "r") as file:
    information_data = json.load(file)

with open("dialogues.json", "r") as file:
    dialogues = json.load(file)

with open("inventory.json", "r") as file:
    inventory = json.load(file)

# ========== FUNCTIONS ========== #

# ===== INPUT DETECTION ===== #
def press_key():
    print(" ➤ ", end="")
    keyboard.read_event(suppress=True)

# ===== TYPING EFFECT ===== #
def type_text(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)


# ===== MAIN GAME ===== #
def game():
    # ===== INTRO ===== #
    print("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚")
    for line in dialogues["intro"]:
        type_text(line)
        print()
        press_key()


def information():
    print("=============== INFORMATION ===============")
    for line in information_data:
        print(line)
    press_key()
    print()


# ========== MAIN GAME LOOP ========== #
while True:
    try:
        # Opens the JSON in read mode
        with open("player_data.json", 'r') as file:
            # Loads the JSON data from the file
            data = json.load(file)

        # ========== MAIN MENU ========== #
        while True:
            print("▣====================================================================================▣")
            print("▥                                 PROJECT BELLUM                                     ▥")
            print("▣====================================================================================▣")
            print("                                                                                       ")
            print("                          ▣============================▣                              ")
            print("                          ▥            PLAY            ▥                              ")
            print("                          ▣============================▣                              ")
            print("                                        [1]                                            ")
            print("                                                                                       ")
            print("                          ▣============================▣                              ")
            print("                          ▥         INFORMATION        ▥                              ")
            print("                          ▣============================▣                              ")
            print("                                        [2]                                            ")
            print("                                                                                       ")
            print("                          ▣============================▣                              ")
            print("                          ▥            QUIT            ▥                              ")
            print("                          ▣============================▣                              ")
            print("                                        [3]                                            ")
            print("                                                                                       ")

            choice = input("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚"
                           "\nCOMMAND: ")

            if choice == "1":
                game()
            elif choice == "2":
                information()
            elif choice == "3":
                quit()
            else:
                print("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚")
                print("INVALID  INPUT INVALID INPUT INVALID INPUT  INVALID INPUT INVALID INPUT INVALID  INPUT")
                print("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚")
                print()



    except FileNotFoundError:
        print("Error: Some JSON files are missing, please reinstall and try again.")
        quit()
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON: {e}")
        quit()