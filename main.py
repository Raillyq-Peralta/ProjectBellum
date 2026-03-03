# ========== LIBRARIES ========== #
import json
import time

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
            print("▥                                 PROJECT BELLUM                                     ▥")
            print("▣▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▣")
            print("                                                                                       ")
            print("                          ▣▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▣                              ")
            print("                          ▥            PLAY            ▥                              ")
            print("                          ▣▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▣                              ")
            print("                                        [Q]                                            ")
            print("                                                                                       ")
            print("                          ▣▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▣                              ")
            print("                          ▥          CREDITS           ▥                              ")
            print("                          ▣▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▣                              ")
            print("                                        [E]                                            ")
            print("                                                                                       ")
            print("                          ▣▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▣                              ")
            print("                          ▥            QUIT            ▥                              ")
            print("                          ▣▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▣                              ")
            print("                                        [X]                                            ")
            print("                                                                                       ")

            choice = input("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚"
                           "\nCOMMAND: ")

    except FileNotFoundError:
        print("Error: The file 'data.json' was not found.")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")