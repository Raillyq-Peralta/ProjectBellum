# ========== LIBRARIES ========== #
import json
import time
import random
import sys
try:
    import keyboard
except ImportError:
    print("Error: Module 'keyboard' not found. Please install it and try again.")
    sys.exit()

# ========== JSON INTERPRETING ========== #
with open("paths.json", "r") as file:
    paths = json.load(file)

with open("player_data.json", "r") as file:
    player_data = json.load(file)

with open("enemy_data.json", "r") as file:
    enemy_data = json.load(file)

with open("information.json", "r") as file:
    information_data = json.load(file)

with open("dialogues.json", "r") as file:
    dialogues = json.load(file)

with open("inventory.json", "r") as file:
    inventory = json.load(file)

# ========== FUNCTIONS ========== #

# ===== PLAYER'S TURN ===== #
def players_turn(player_data, enemy_data, key):
    player_agility = player_data["agility"]
    enemy_agility = enemy_data[key]["agility"]

    if player_agility >= enemy_agility:
        type_text("It's your turn!\n")
    else:
        type_text(f"It's {key}'s turn!\n")
        return False

    choice = input("\n⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚"
                   "\n[1] ATTACK"
                   "\n[2] RUN"
                   "\n\nCOMMAND: ")

    if choice.strip() == "1":
        if player_hit_success(player_data, enemy_data, key):
            player_attack(player_data, enemy_data, key)
        else:
            type_text(f"{key} dodged your attack!\n")
        return True
    elif choice.strip() == "2":
        type_text("You ran away from the enemy...\n")
        return False
    else:
        print("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚")
        print("INVALID  INPUT INVALID INPUT INVALID INPUT  INVALID INPUT INVALID INPUT INVALID  INPUT")
        print("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚")
        print()
        return players_turn(player_data, enemy_data, key)


# ===== ENEMY'S TURN ===== #
def enemys_turn(enemy_data, player_data, key):
    if enemy_hit_success:
        enemy_attack(enemy_data, player_data, key)
    else:
        print("You successfully dodged the enemy's attack!\n")


# ===== HIT SUCCESS ===== #
def player_hit_success(player_data, enemy_data, key):
    player_agility = player_data["agility"]
    enemy_agility = enemy_data[key]["agility"]

    chance = 0.5 + (player_agility - enemy_agility) * 0.05
    chance = max(0, min(1, chance))

    hit_result = random.random() < chance
    if hit_result:
        return True
    else:
        return False

def enemy_hit_success(enemy_data, player_data, key):
    enemy_agility = enemy_data[key]["agility"]
    player_agility = player_data["agility"]

    chance = 0.5 + (enemy_agility - player_agility) * 0.05
    chance = max(0, min(1, chance))

    hit_result = random.random() < chance
    if hit_result:
        return True
    else:
        return False

# ===== DAMAGE CALCULATION ===== #
def player_attack(player_data, enemy_data, key):
    player_attack = player_data["attack"]
    enemy_defense = enemy_data[key]["defense"]

    damage = max(1, player_attack - enemy_defense // 2)
    enemy_data[key]["hp"] -= damage
    type_text(f"You hit {key} for {damage} damage!\n")
    return damage

def enemy_attack(enemy_data, player_data, key):
    enemy_attack = enemy_data[key]["attack"]
    player_defense = player_data["defense"]

    damage = max(1, enemy_attack - player_defense // 2)
    player_data["hp"] -= damage
    type_text(f"{key} hit you for {damage} damage! You have {player_data["hp"]}HP left!\n")
    return damage


# ===== NEXT DIALOGUE ===== #
def press_key():
    print(" ➤ ", end="")
    keyboard.read_event(suppress=True)

# ===== TYPING EFFECT ===== #
def type_text(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)

# ===== INFORMATION ===== #
def information():
    print("=============== INFORMATION ===============")
    for line in information_data:
        print(line)
        press_key()
    print()


# ===== MAIN GAME ===== #
def game():
    # ===== INTRO ===== #
    print("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚")
    for line in dialogues["intro"]:
        type_text(line)
        print()
        press_key()
    print("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚")

    # ========== ACTUAL GAME ========== #
    current_location = "Lalaque Forest"
    while True:
        print(F"========== {current_location.upper()} ==========")
        options = paths[current_location]
        for key in options:
            print(f"{key}: {options[key]}")
        command = input("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚"
                        "\nCOMMAND: ")

        valid = False
        for key in options:
            if command.upper().replace(" ", "") == key.upper().replace(" ", ""):
                valid = True
                result = options[key]
                valid = True
                break

        if not valid:
            print("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚")
            print("INVALID  INPUT INVALID INPUT INVALID INPUT  INVALID INPUT INVALID INPUT INVALID  INPUT")
            print("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚")
            print()
            continue

        if result in paths:
            current_location = result
        elif result == "Fight":
            while player_data["hp"] > 0 and enemy_data[key]["hp"] > 0:
                # ===== PLAYER'S TURN ===== #
                player_first = players_turn(player_data, enemy_data, key)

                if player_first == False:
                    break

                # ===== ENEMY'S TURN ===== #
                if enemy_data[key]["hp"] > 0:
                    if not player_first:
                        enemys_turn(enemy_data, player_data, key)
                    else:
                        enemys_turn(enemy_data, player_data, key)

            # ===== BATTLE ASSESSMENT ===== #
            if player_data["hp"] <= 0:
                type_text("You were defeated...")
            elif enemy_data[key]["hp"] > 0:
                type_text(f"You defeated {key}!")







# ========== MAIN GAME LOOP ========== #
while True:
    try:
        # Opens the JSON in read mode
        with open("player_data.json", 'r') as file:
            # Loads the JSON data from the file
            data = json.load(file)

        # ========== MAIN MENU ========== #
        while True:
            print(
                "  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
            print("")
            print("        ▄▄▄▄▄▄                                         ▄▄▄           ▄▄ ▄▄")
            print("        █▀██▀▀▀█▄                              █▄      ██▀▀█▄         ██ ██")
            print("        ██▄▄▄█▀▄              ▀▀              ▄██▄     ██ ▄█▀         ██ ██           ▄ ")
            print("        ██▀▀▀  ████▄▄ ███▄   ██  ▄█▀█▄  ▄███▀  ██      ██▀▀█▄  ▄█▀█▄  ██ ██   ██ ██   ███▄███▄ ")
            print("      ▄ ██     ██     ██ ██  ██ ██▄█▀  ██      ██    ▄ ██  ▄█  ██▄█▀  ██ ██   ██ ██   ██ ██ ██")
            print("      ▀██▀    ▄█▀    ▄▀███▀ ▄██▄▀█▄▄▄   ▀███ ▄▄██    ▀██████▀▄ ▀█▄▄▄▄ ██▄██▄  ▀██▀  █▄██ ██ ▀█")
            print("")
            print(
                " ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n ")

            print("                ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄")
            print("                ▄▄                                        ▄     ▄                ▄▄")
            print("                ██           █████▄ ▄▄     ▄▄▄  ▄▄ ▄▄   ▄█▀ ▄██ ▀█▄              ██")
            print("                ██           ██▄▄█▀ ██    ██▀██ ▀███▀   ██   ██  ██              ██")
            print("                ██           ██     ██▄▄▄ ██▀██   █     ▀█▄  ██ ▄█▀              ██")
            print("                ▀▀                                        ▀     ▀                ▀▀")
            print("                ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ \n   ")

            print("  ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ")
            print("  ▄▄                                                                            ▄       ▄         ▄▄")
            print("  ██         ██ ▄▄  ▄▄ ▄▄▄▄▄  ▄▄▄  ▄▄▄▄  ▄▄   ▄▄  ▄▄▄ ▄▄▄▄▄▄ ▄▄  ▄▄▄  ▄▄  ▄▄  ▄█▀ ████▄ ▀█▄       ██")
            print("  ██         ██ ███▄██ ██▄▄  ██▀██ ██▄█▄ ██▀▄▀██ ██▀██  ██   ██ ██▀██ ███▄██  ██   ▄██▀  ██       ██")
            print("  ██         ██ ██ ▀██ ██    ▀███▀ ██ ██ ██   ██ ██▀██  ██   ██ ▀███▀ ██ ▀██  ▀█▄ ███▄▄ ▄█▀       ██")
            print("  ▀▀                                                                            ▀       ▀         ▀▀")
            print("  ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄\n ")

            print("                   ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄")
            print("                   ▄▄                                   ▄       ▄             ▄▄")
            print("                   ██       ▄█████▄ ▄▄ ▄▄ ▄▄ ▄▄▄▄▄▄   ▄█▀ ████▄ ▀█▄           ██")
            print("                   ██       ██ ▄ ██ ██ ██ ██   ██     ██   ▄▄██  ██           ██")
            print("                   ██       ▀█████▀ ▀███▀ ██   ██     ▀█▄ ▄▄▄█▀ ▄█▀           ██")
            print("                   ▀▀            ▀▀                     ▀       ▀             ▀▀")
            print("                   ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄   ")

            choice = input("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚"
                           "\nCOMMAND: ")

            if choice.strip() == "1":
                game()
            elif choice.strip() == "2":
                information()
            elif choice.strip() == "3":
                sys.exit()
            else:
                print("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚")
                print("INVALID  INPUT INVALID INPUT INVALID INPUT  INVALID INPUT INVALID INPUT INVALID  INPUT")
                print("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚")
                print()



    except FileNotFoundError:
        print("Error: Some JSON files are missing, please reinstall and try again.")
        sys.exit()
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON: {e}")
        sys.exit()