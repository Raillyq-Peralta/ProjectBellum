# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                                             ┓ ┳┳┓┳┓┏┓┳┓┳┏┓┏┓
#                                             ┃ ┃┣┫┣┫┣┫┣┫┃┣ ┗┓
#                                             ┗┛┻┻┛┛┗┛┗┛┗┻┗┛┗┛
# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                     ⊰════════════════════════✦ 𝑰𝑴𝑷𝑶𝑹𝑻𝑰𝑵𝑮 ✦════════════════════════⊱
import json
import time
import random
import re
import sys
import os
import shutil
import msvcrt
import pygame

# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                                                ┏┳┏┓┏┓┳┓┏┓
#                                                 ┃┗┓┃┃┃┃┗┓
#                                                ┗┛┗┛┗┛┛┗┗┛
# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                    ⊰════════════════════════✦ 𝑰𝑵𝑻𝑬𝑹𝑷𝑹𝑬𝑻𝑰𝑵𝑮 ✦════════════════════════⊱
try:
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

    with open("items.json", "r") as file:
        item_data = json.load(file)

#                  ⊰════════════════════════✦ 𝑬𝑹𝑹𝑶𝑹 𝑯𝑨𝑵𝑫𝑳𝑰𝑵𝑮 ✦════════════════════════⊱
except FileNotFoundError:
    print(
        "\033[31m𝐸𝑟𝑟𝑜𝑟: 𝑆𝑜𝑚𝑒 𝐽𝑆𝑂𝑁 𝑓𝑖𝑙𝑒𝑠 𝑎𝑟𝑒 𝑚𝑖𝑠𝑠𝑖𝑛𝑔. 𝑃𝑙𝑒𝑎𝑠𝑒 𝑟𝑒𝑖𝑛𝑠𝑡𝑎𝑙𝑙 𝑎𝑛𝑑 𝑡𝑟𝑦 𝑎𝑔𝑎𝑖𝑛.\033[0m")
    sys.exit()
except json.JSONDecodeError as e:
    print(f"\033[31m𝐸𝑟𝑟𝑜𝑟: 𝐹𝑎𝑖𝑙𝑒𝑑 𝑡𝑜 𝑑𝑒𝑐𝑜𝑑𝑒 𝐽𝑆𝑂𝑁: {e}\033[0m")
    sys.exit()

# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                                            ┏┓┳┳┳┓┏┓┏┳┓┳┏┓┳┓┏┓
#                                            ┣ ┃┃┃┃┃  ┃ ┃┃┃┃┃┗┓
#                                            ┻ ┗┛┛┗┗┛ ┻ ┻┗┛┛┗┗┛
# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                                    ┳┓┏┓┏┳┓┏┓  ┳┳┓┏┓┳┓┏┓┏┓┏┓┳┳┓┏┓┳┓┏┳┓
#                                    ┃┃┣┫ ┃ ┣┫  ┃┃┃┣┫┃┃┣┫┃┓┣ ┃┃┃┣ ┃┃ ┃
#                                    ┻┛┛┗ ┻ ┛┗  ┛ ┗┛┗┛┗┛┗┗┛┗┛┛ ┗┗┛┛┗ ┻
# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                       ⊰════════════════════════✦ 𝑺𝑨𝑽𝑰𝑵𝑮 ✦════════════════════════⊱
def save_game(current_player_data, current_inventory, current_location):
    save_data = {
        "player_data": current_player_data,
        "inventory": current_inventory,
        "current_location": current_location,
        "paths": paths,
        "dialogues": dialogues
    }

    clear()
    center_text("\033[32m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
    center_text("\033[32m                                          ┏┓┏┓┳┳┓┏┓  ┏┓┏┓┓┏┏┓┳┓                                         \033[0m")
    center_text("\033[32m                                          ┃┓┣┫┃┃┃┣   ┗┓┣┫┃┃┣ ┃┃                                         \033[0m")
    center_text("\033[32m                                          ┗┛┛┗┛ ┗┗┛  ┗┛┛┗┗┛┗┛┻┛                                         \033[0m")
    center_text("\033[32m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
    press_space(True)

    with open("savefile.json", "w") as file:
        json.dump(save_data, file, indent=4)

#                       ⊰════════════════════════✦ 𝑳𝑶𝑨𝑫𝑰𝑵𝑮 ✦════════════════════════⊱
def load_game():
    try:
        with open("savefile.json", "r") as file:
            data = json.load(file)
            clear()
            center_text("\033[32m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
            center_text("\033[32m                                    ┏┓┏┓┓┏┏┓  ┏┓┳┓ ┏┓  ┓ ┏┓┏┓┳┓┏┓┳┓                                      \033[0m")
            center_text("\033[32m                                    ┗┓┣┫┃┃┣   ┣ ┃┃ ┣   ┃ ┃┃┣┫┃┃┣ ┃┃                                      \033[0m")
            center_text("\033[32m                                    ┗┛┛┗┗┛┗┛  ┻ ┻┗┛┗┛  ┗┛┗┛┛┗┻┛┗┛┻┛                                      \033[0m")
            center_text("\033[32m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
            press_space(True)
        return data

    except FileNotFoundError:
        clear()
        center_text("\033[31m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
        center_text("\033[31m                                   ┳┓┏┓  ┏┓┏┓┓┏┏┓  ┏┓┳┓ ┏┓  ┏┓┏┓┳┳┳┓┳┓                                   \033[0m")
        center_text("\033[31m                                   ┃┃┃┃  ┗┓┣┫┃┃┣   ┣ ┃┃ ┣   ┣ ┃┃┃┃┃┃┃┃                                   \033[0m")
        center_text("\033[31m                                   ┛┗┗┛  ┗┛┛┗┗┛┗┛  ┻ ┻┗┛┗┛  ┻ ┗┛┗┛┛┗┻┛                                   \033[0m")
        center_text("\033[31m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
        press_space(True)
        return None

# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                                                ┳┳┓┳┳┏┓┳┏┓
#                                                ┃┃┃┃┃┗┓┃┃
#                                                ┛ ┗┗┛┗┛┻┗┛
# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                       ⊰════════════════════════✦ 𝑴𝑼𝑺𝑰𝑪 ✦════════════════════════⊱
# INITIALIZES MUSIC MODULE
pygame.mixer.init()
current_music = None

# MUSIC PLAYER
def play_music(music, volume = 100, fade = 0):
    global current_music

    if current_music == music and pygame.mixer.music.get_busy():
        return

    pygame.mixer.music.fadeout(fade)
    pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(volume / 100)
    pygame.mixer.music.play(-1)

    current_music = music

#                    ⊰════════════════════════✦ 𝑺𝑶𝑼𝑵𝑫 𝑬𝑭𝑭𝑬𝑪𝑻𝑺 ✦════════════════════════⊱
def play_sfx(sfx, volume = 100):
    sfx = pygame.mixer.Sound(sfx)
    sfx.set_volume(volume / 100)
    sfx.play()
    return sfx

# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                                    ┳┏┳┓┏┓┳┳┓  ┳┳┓┏┓┳┓┏┓┏┓┏┓┳┳┓┏┓┳┓┏┳┓
#                                    ┃ ┃ ┣ ┃┃┃  ┃┃┃┣┫┃┃┣┫┃┓┣ ┃┃┃┣ ┃┃ ┃
#                                    ┻ ┻ ┗┛┛ ┗  ┛ ┗┛┗┛┗┛┗┗┛┗┛┛ ┗┗┛┛┗ ┻
# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                 ⊰════════════════════════✦ 𝑰𝑵𝑽𝑬𝑵𝑻𝑶𝑹𝒀 𝑺𝒀𝑺𝑻𝑬𝑴 ✦════════════════════════⊱
# INITIALIZES KEYBINDS
key_map = {
    "1": 0, "2": 1, "3": 2, "4": 3, "5": 4,
    "6": 5, "7": 6, "8": 7, "9": 8, "0": 9,
    "Q": 10, "W": 11, "E": 12, "R": 13,
    "T": 14, "Y": 15
}
index_for_key = {v: k for k, v in key_map.items()}

# INVENTORY MENU
def show_inventory(inv, player_data=None):
    clear()
    play_sfx("inventory.mp3")

    center_text("\033[92m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
    center_text("\033[92m                                           ┳┳┓┓┏┏┓┳┓┏┳┓┏┓┳┓┓┏                                            \033[0m")
    center_text("\033[92m                                           ┃┃┃┃┃┣ ┃┃ ┃ ┃┃┣┫┗┫                                            \033[0m")
    center_text("\033[92m                                           ┻┛┗┗┛┗┛┛┗ ┻ ┗┛┛┗┗┛                                            \033[0m")
    center_text("\033[92m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")

    slots = list(inv.keys())

    # DISPLAY INVENTORY
    for i, slot in enumerate(slots):
        item = inv[slot]

        # GETS KEY LABEL
        key_label = index_for_key.get(i)

        center_text(f"[{key_label}] {slot} ➣ \033[96m{item}\033[0m")
        center_text("\033[92m༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻༺༻\033[0m")

    # INPUT DETECTION
    while True:
        pressed_key = get_key()

        # EXIT INVENTORY
        if pressed_key == " ":
            break

        # INPUT EVALUATION
        elif pressed_key in key_map:
            index = key_map[pressed_key]

            if 0 <= index < len(slots):
                selected_item = inv[slots[index]]

                if selected_item == "Empty":
                    continue

                inspect_item(selected_item, player_data)
                return

# ITEM INSPECTION
def inspect_item(item_name, player_data):
    item = item_data[item_name]
    clear()

    # ITEM INSPECTION MENU
    center_text("\033[92m⊰═══════════════════════════════════════════════✦❘ ༻ 𝑰𝑻𝑬𝑴 𝑰𝑵𝑭𝑶𝑹𝑴𝑨𝑻𝑰𝑶𝑵 ༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
    print()
    center_text(f"\033[96m{item_name}\033[0m")
    print()

    desc = item.get("description")
    center_text(desc)
    print()

    # ITEM TYPE IDENTIFICATION
    if item["type"] == "healing":
        heal = item["heal"]
        center_text(f"Heal: \033[92m{heal}\033[0m")
        print()
        center_text("[1] USE    [2] BACK")
    elif item["type"] == "stat":
        stat = item["stat"]
        value = item["value"]

        if stat == "max_hp":
            stat = "Max Health"

        center_text(f"{stat.capitalize()}: \033[96m+{value}\033[0m")
        print()
        center_text("[1] USE    [2] BACK")
    elif item["type"] == "equipment":
        print()
        center_text("[1] EQUIP    [2] BACK")
    elif item["type"] == "quest":
        print()
        center_text("[1] BACK")

    # INPUT DETECTION
    while True:
        pressed_key = get_key()

        # INPUT EVALUATION
        if pressed_key == "1":
            if item["type"] == "quest":
                return
            if player_data:
                use_item(item_name, player_data)
                press_space(True)
                return
        elif pressed_key == "2" and item["type"] != "quest":
            return
#                   ⊰════════════════════════✦ 𝑰𝑻𝑬𝑴 𝑨𝑫𝑫𝑰𝑻𝑰𝑶𝑵 ✦════════════════════════⊱
def add_item(item_name):
    # FINDS EMPTY SLOTS
    for slot in inventory:
        if inventory[slot] == "Empty":

            # ADDS ITEM
            inventory[slot] = item_name
            return True
    return False

#                  ⊰════════════════════════✦ 𝑰𝑻𝑬𝑴 𝑺𝑼𝑩𝑻𝑹𝑨𝑪𝑻𝑰𝑶𝑵 ✦════════════════════════⊱
def remove_item(item_name):
    # FINDS ITEM
    for slot in inventory:
        if inventory[slot] == item_name:

            # REMOVES ITEM
            inventory[slot] = "Empty"
            return True
    return False

#                  ⊰════════════════════════✦ 𝑰𝑻𝑬𝑴 𝑪𝑶𝑵𝑺𝑼𝑴𝑷𝑻𝑰𝑶𝑵 ✦════════════════════════⊱
def use_item(item_name, player_data):
    item = item_data[item_name]

    # HEALING ITEMS
    if item["type"] == "healing":
        heal_value = item["heal"]

        # FULL HEAL
        if heal_value == "full":
            if player_data["hp"] == player_data["max_hp"]:
                print()
                type_text("You're already at full HP.", 0.05, True, True, "talk.mp3")
                print()
                return
            else:
                heal_amount = player_data["max_hp"] - player_data["hp"]
                player_data["hp"] = player_data["max_hp"]

        # NORMAL HEAL
        else:
            if player_data["hp"] == player_data["max_hp"]:
                print()
                type_text("You're already at full HP.", 0.05, True, True, "talk.mp3")
                print()
                return
            heal_amount = heal_value
            player_data["hp"] += heal_amount
            player_data["hp"] = min(player_data["hp"], player_data["max_hp"])

        # REMOVES ITEM
        remove_item(item_name)
        print()
        type_text(f"You used \033[96m{item_name}\033[0m and restored \033[92m{heal_amount}\033[0m HP!\n", 0.05, True, True, "talk.mp3")
        print()

    # STAT BOOSTING ITEMS
    elif item["type"] == "stat":
        stat = item["stat"]
        value = item["value"]

        player_data[stat] += value

        if stat == "max_hp":
            stat = "Max Health"

        # REMOVE ITEM
        remove_item(item_name)
        print()
        type_text(f"You used \033[96m{item_name}\033[0m and increased your \033[96m{stat.capitalize()}\033[0m by \033[92m{value}\033[0m.", 0.05, True,True, "talk.mp3")
        print()

    # EQUIPMENTS
    elif item["type"] == "equipment":
        equip_key = item["equip_key"]

        # EQUIPS AND REMOVES ITEM FROM INVENTORY
        player_data[equip_key] = True
        remove_item(item_name)
        print()
        type_text(f"You equipped \033[96m{item_name}\033[0m.\n", 0.05, True, True, "talk.mp3")
        print()
# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                                      ┏┳┓┏┓┏┓┏┓┏┳┓  ┏┓┏┓┏┓┏┓┏┓┏┳┓┏┓
#                                       ┃ ┣  ┃┃  ┃   ┣ ┣ ┣ ┣ ┃  ┃ ┗┓
#                                       ┻ ┗┛┗┛┗┛ ┻   ┗┛┻ ┻ ┗┛┗┛ ┻ ┗┛
# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                    ⊰════════════════════════✦ 𝑻𝑬𝑿𝑻 𝑬𝑭𝑭𝑬𝑪𝑻𝑺 ✦════════════════════════⊱
def get_key():
    # DETECTS PRESSED KEY
    if not msvcrt.kbhit():
        return None

    # CONVERTS BYTE TO AN UPPERCASE STRING
    try:
        return msvcrt.getch().decode().upper()
    except:
        return None

#                    ⊰════════════════════════✦ 𝑻𝒀𝑷𝑰𝑵𝑮 𝑬𝑭𝑭𝑬𝑪𝑻 ✦════════════════════════⊱
def type_text(text, speed, centered = False, skip = False, sfx = None):
    # CENTERING EFFECT
    if centered:
        width = shutil.get_terminal_size().columns
        visible_len = len(re.sub(r'\033\[[0-9;]*m', '', text))
        padding = (width - visible_len) // 2
        print(' ' * max(padding, 0), end="", flush=True)

    # SOUND EFFECT
    channel = None
    if sfx:
        sound = pygame.mixer.Sound(sfx)
        channel = sound.play(-1)

    # SKIP EFFECT
    current_text = 0
    total_text_length = len(text)

    while current_text < total_text_length:
        if skip and msvcrt.kbhit():
            skip_key = msvcrt.getch().decode().upper()
            if skip_key == "Q":
                print(text[current_text:], end="", flush=True)
                break

        # DETECTS AND SKIPS OVER ANSI ESCAPE CODES
        if text[current_text] == '\033':
            match = re.match(r'\033\[[0-9;]*m', text[current_text:])
            if match:
                print(match.group(), end="", flush=True)
                current_text += len(match.group())
                continue

        # TYPING
        print(text[current_text], end="", flush=True)
        time.sleep(speed)
        current_text += 1

    # STOPS SFX
    if channel:
        channel.stop()

#                    ⊰════════════════════════✦ 𝑪𝑬𝑵𝑻𝑬𝑹 𝑬𝑭𝑭𝑬𝑪𝑻 ✦════════════════════════⊱
def center_text(text):
    # DETECTS TERMINAL WIDTH
    width = shutil.get_terminal_size().columns
    visible_len = len(re.sub(r'\033\[[0-9;]*m', '', text))
    padding = (width - visible_len) // 2

    # CENTERS TEXT
    print(' ' * max(padding, 0) + text)

#                    ⊰════════════════════════✦ 𝑹𝑬𝑷𝑬𝑨𝑻 𝑬𝑭𝑭𝑬𝑪𝑻 ✦════════════════════════⊱
def repeat_text(text):
    # DETECTS TERMINAL WIDTH
    width = shutil.get_terminal_size().columns

    # CENTERS TEXT
    print(text * width)

#                    ⊰════════════════════════✦ 𝑹𝑬𝑺𝑬𝑻 𝑬𝑭𝑭𝑬𝑪𝑻 ✦════════════════════════⊱
def clear():
    # RUNS COMMAND
    os.system("cls")

#                  ⊰════════════════════════✦ 𝑪𝑶𝑵𝑻𝑰𝑵𝑼𝑬 𝑬𝑭𝑭𝑬𝑪𝑻 ✦════════════════════════⊱
def press_space(prompt = False):
    # SHOW PROMPT
    if prompt:
        center_text("\033[33m◄ 𝑷𝒓𝒆𝒔𝒔 𝒔𝒑𝒂𝒄𝒆 𝒕𝒐 𝒄𝒐𝒏𝒕𝒊𝒏𝒖𝒆 ►\033[0m")
        center_text("")
    # SHOWS ARROW
    else:
        print("\033[33m➤ \033[0m", end="", flush=True)

    # INPUT DETECTION
    while True:
        if msvcrt.kbhit():
            space_key = msvcrt.getch().decode().upper()

            # INPUT EVALUATION
            if space_key == " ":
                break

        time.sleep(0.01)

    while msvcrt.kbhit():
        msvcrt.getch()

# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                                    ┳┓┳┏┓┓ ┏┓┏┓┳┳┏┓  ┳┳┓┏┓┏┓┓┏┏┓┳┓┳┏┓┏┓
#                                    ┃┃┃┣┫┃ ┃┃┃┓┃┃┣   ┃┃┃┣ ┃ ┣┫┣┫┃┃┃┃ ┗┓
#                                    ┻┛┻┛┗┗┛┗┛┗┛┗┛┗┛  ┛ ┗┗┛┗┛┛┗┛┗┛┗┻┗┛┗┛
# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                 ⊰════════════════════════✦ 𝑪𝑶𝑵𝑫𝑰𝑻𝑰𝑶𝑵 𝑪𝑯𝑬𝑪𝑲𝑬𝑹 ✦════════════════════════⊱
def check_conditions(conditions, dialogue_block):
# INVENTORY CHECKER
    for item in conditions:
        if item not in inventory.values():
            return False

# TAKES REQUIRED ITEMS
    for item in conditions:
        for slot in inventory:
            if inventory[slot] == item:
                inventory[slot] = "Empty"
                break

# GIVES REWARD
    for slot in inventory:
        if inventory[slot] == "Empty":
            inventory[slot] = dialogue_block["reward"]
            break

    return True

#                 ⊰════════════════════════✦ 𝑫𝑰𝑨𝑳𝑶𝑮𝑼𝑬 𝑬𝑿𝑬𝑪𝑼𝑻𝑶𝑹 ✦════════════════════════⊱
def execute_dialogue(dialogue_block):
# PRINTS DIALOGUE IN A TEXT BOX
    clear()
    for line in dialogue_block["lines"]:
        center_text("\033[33m⊰═════════════════════════════════════════════════════════════════════════════════════✦❘ ༻༺ ❘✦═════════════════════════════════════════════════════════════════════════════════════⊱\033[0m")
        print()
        center_text("\033[33m⊰═════════════════════════════════════════════════════════════════════════════════════✦❘ ༻༺ ❘✦═════════════════════════════════════════════════════════════════════════════════════⊱\033[0m")
        print("\033[F\033[F", end="")
        type_text(line, 0.05, True, True, "talk.mp3")
        print("\n")
        press_space(True)
        clear()

#                 ⊰════════════════════════✦ 𝑵𝑷𝑪 𝑬𝑿𝑬𝑪𝑼𝑻𝑶𝑹 ✦════════════════════════⊱
def execute_npc(npc):
    # INITIALIZES THE FALLBACK
    incomplete_dialogue = None

    # DIALOGUE STAGE EVALUATOR
    for dialogue_block in dialogues[npc]:
        condition = dialogue_block.get("conditions")

        # RE-INITIALIZES THE FALLBACK
        if condition == "Incomplete":
            incomplete_dialogue = dialogue_block
            continue

        # QUEST DETAILS
        if condition is None and dialogue_block.get("access"):
            execute_dialogue(dialogue_block)
            dialogue_block["access"] = False

            for d_block in dialogues[npc]:
                if isinstance(d_block["conditions"], list):
                    d_block["access"] = True
                if d_block["conditions"] == "Incomplete":
                    d_block["access"] = True
            return

        # QUEST CHECKER
        elif isinstance(condition, list) and dialogue_block.get("access"):
            if check_conditions(condition, dialogue_block):
                execute_dialogue(dialogue_block)
                dialogue_block["access"] = False

                for d_block in dialogues[npc]:
                    if d_block["conditions"] == "Finished":
                        d_block["access"] = True
                    if d_block["conditions"] == "Incomplete":
                        d_block["access"] = False
                return

        # POST-QUEST DIALOGUE
        elif condition == "Finished" and dialogue_block.get("access"):
            execute_dialogue(dialogue_block)
            return

    # UNMET QUEST CONDITIONS
    if incomplete_dialogue:
        execute_dialogue(incomplete_dialogue)


# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                                    ┏┓┏┓┳┳┓┳┓┏┓┏┳┓  ┳┳┓┏┓┏┓┓┏┏┓┳┓┳┏┓┏┓
#                                    ┃ ┃┃┃┃┃┣┫┣┫ ┃   ┃┃┃┣ ┃ ┣┫┣┫┃┃┃┃ ┗┓
#                                    ┗┛┗┛┛ ┗┻┛┛┗ ┻   ┛ ┗┗┛┗┛┛┗┛┗┛┗┻┗┛┗┛
# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                ⊰════════════════════════✦ 𝑯𝑰𝑻𝑹𝑨𝑻𝑬 𝑪𝑨𝑳𝑪𝑼𝑳𝑨𝑻𝑰𝑶𝑵 ✦════════════════════════⊱
# PLAYER
def player_hit_success(p_data, e_data, enemy_key):
    p_agility = p_data["agility"]
    e_agility = e_data[enemy_key]["agility"]

# INITIALIZES BASE HIT RATE AND SCALING OF HIT RATE
    base = 0.70
    chance_scaling = 0.05

# COMPUTES DIFFERENCE IN AGILITY AND CHANGES HIT RATE
    agility_difference = p_agility - e_agility
    chance = base + (agility_difference * chance_scaling)

# SETS A MAXIMUM AND MINIMUM HIT RATE FOR BALANCING
    if chance > 0.95:
        chance = 0.95
    if chance < 0.10:
        chance = 0.10

# RANDOMLY ( GUIDED WITH CHANCE ) DECIDES WHETHER THE HIT LANDS OR NOT
    return random.random() < chance

# ENEMY
def enemy_hit_success(e_data, p_data, enemy_key):
    e_agility = e_data[enemy_key]["agility"]
    p_agility = p_data["agility"]

# INITIALIZES BASE HIT RATE AND SCALING OF HIT RATE
    base = 0.5
    chance_scaling = 0.05

# COMPUTES DIFFERENCE IN AGILITY AND CHANGES HIT RATE
    agility_difference = e_agility - p_agility
    chance = base + (agility_difference * chance_scaling)

# SETS A MAXIMUM AND MINIMUM HIT RATE FOR BALANCING
    if chance > 0.95:
        chance = 0.95
    if chance < 0.10:
        chance = 0.10

# RANDOMLY ( GUIDED WITH CHANCE ) DECIDES WHETHER THE HIT LANDS OR NOT
    return random.random() < chance

#                ⊰════════════════════════✦ 𝑫𝑨𝑴𝑨𝑮𝑬 𝑪𝑨𝑳𝑪𝑼𝑳𝑨𝑻𝑰𝑶𝑵 ✦════════════════════════⊱
# PLAYER
def player_attack(p_data, e_data, enemy_key):
    p_attack = p_data["attack"]
    e_defense = e_data[enemy_key]["defense"]

# INITIALIZES BASE DAMAGE AND DAMAGE REDUCTION
    base_damage = p_attack * 1.2
    reduced = e_defense * 0.6

# CALCULATES AND ROUNDS FINAL DAMAGE
    damage = base_damage - reduced
    if damage <= 0:
        damage = 1
    damage = int(damage)

# SUBTRACTS HEALTH POINTS FROM THE ENEMY
    e_data[enemy_key]["hp"] -= damage

# PREVENTS NEGATVIE HEALTH
    if e_data[enemy_key]["hp"] < 0:
        e_data[enemy_key]["hp"] = 0

# OUTPUT
    return f"You hit \033[91m{enemy_key}\033[0m for \033[92m{damage}\033[0m damage!"

# ENEMY
def enemy_attack(e_data, p_data, enemy_key):
    e_attack = e_data[enemy_key]["attack"]
    p_defense = p_data["defense"]

# INITIALIZES BASE DAMAGE AND DAMAGE REDUCTION
    base_damage = e_attack * 1.2
    reduced = p_defense * 0.6

# CALCULATES AND ROUNDS FINAL DAMAGE
    damage = base_damage - reduced
    if damage <= 0:
        damage = 1
    damage = int(damage)

# SUBTRACTS HEALTH POINTS FROM THE PLAYER
    p_data["hp"] -= damage

# PREVENTS NEGATIVE HEALTH
    if p_data["hp"] < 0:
        p_data["hp"] = 0

# OUTPUT
    return f"\033[91m{enemy_key}\033[0m hit you for \033[91m{damage}\033[0m damage!"

#                   ⊰════════════════════════✦ 𝑻𝑼𝑹𝑵 𝑺𝒀𝑺𝑻𝑬𝑴 ✦════════════════════════⊱
# PLAYER
def players_turn(p_data, e_data, enemy_key):
    # PROMPT
    center_text("⟦1⟧ ATTACK          ⟦2⟧ INVENTORY          ⟦3⟧ RUN")

    # INPUT DETECTTION
    while True:
        pressed_key = get_key()

        # INPUT EVALUATION
        if pressed_key == "1":
            # HIT EVALUATION
            if player_hit_success(p_data, e_data, enemy_key):
                return player_attack(p_data, e_data, enemy_key)
            else:
                return f"You \033[91mmissed\033[0m your attack!"
        elif pressed_key == "2":
            show_inventory(inventory, p_data)
            return "Opened \033[96minventory\033[0m"
        elif pressed_key == "3":
            return "Run"

# ENEMY
def enemys_turn(e_data, p_data, enemy_key):
    # HIT EVALUATION
    if enemy_hit_success(e_data, p_data, enemy_key):
        return enemy_attack(e_data, p_data, enemy_key)
    else:
        return f"\033[31m{enemy_key}\033[0m \033[92mmissed\033[0m its attack!"

#                   ⊰════════════════════════✦ 𝑺𝑻𝑨𝑻 𝑺𝒀𝑺𝑻𝑬𝑴 ✦════════════════════════⊱
def draw_stats(p_data, e_data=None, enemy_key=None):
    clear()

    # PLAYER
    center_text("\033[92m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
    center_text("\033[92m                                                 Player                                                  \033[0m")
    center_text(f"HP: {p_data['hp']}/{p_data['max_hp']} | ATK: {p_data['attack']} | DEF: {p_data['defense']} | AGI: {p_data['agility']}")

    # ENEMY
    if e_data and enemy_key:
        enemy = e_data[enemy_key]
        center_text("\033[91m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
        center_text(f"\033[91m                                              {enemy_key}                                               \033[0m")
        center_text(f"HP: {enemy['hp']}/{enemy['max_hp']} | ATK: {enemy['attack']} | DEF: {enemy['defense']} | AGI: {enemy['agility']}")

    # BORDER
    print()
    repeat_text("═")

#                   ⊰════════════════════════✦ 𝑪𝑶𝑴𝑩𝑨𝑻 𝑹𝑬𝑵𝑫𝑬𝑹𝑰𝑵𝑮 ✦════════════════════════⊱
def render_combat(p_data, e_data, enemy_key, player_action, enemy_action):
    # STATS
    draw_stats(p_data, e_data, enemy_key)

    # COMBAT LOG
    if player_action:
        center_text("⟦\033[32mYou\033[0m⟧")
        type_text(player_action, 0.05, True, True, "talk.mp3")
    if enemy_action:
        print()
        center_text(f"⟦\033[91m{enemy_key}\033[0m⟧")
        type_text(enemy_action, 0.05, True, True, "talk.mp3")
    print()

# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                                      ┏┓┏┓┳┳┓┏┓  ┏┓┳┳┳┓┏┓┏┳┓┳┏┓┳┓┏┓
#                                      ┃┓┣┫┃┃┃┣   ┣ ┃┃┃┃┃  ┃ ┃┃┃┃┃┗┓
#                                      ┗┛┛┗┛ ┗┗┛  ┻ ┗┛┛┗┗┛ ┻ ┻┗┛┛┗┗┛
# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                                            ⊰═════ 𝑸𝑼𝑰𝑻 ═════⊱
def quit_detector():
    while True:
        # QUIT MENU
        clear()
        play_sfx("pause.mp3")
        center_text("⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱")
        center_text("                                              ┏┓┏┓┳┳┏┓┏┓┳┓                                               ")
        center_text("                                              ┃┃┣┫┃┃┗┓┣ ┃┃                                               ")
        center_text("                                              ┣┛┛┗┗┛┗┛┗┛┻┛                                               ")
        center_text("⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱")
        print()
        center_text("                                       𝑫𝒐 𝒚𝒐𝒖 𝒘𝒂𝒏𝒕 𝒕𝒐 𝒆𝒙𝒊𝒕 𝒕𝒉𝒆 𝒈𝒂𝒎𝒆?                                      ")
        center_text("                 ༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺           ༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺                 ")
        center_text("                              𝒀𝑬𝑺                                       𝑵𝑶                               ")
        center_text("                 ༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺           ༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺                 ")
        center_text("                              ⟦𝟙⟧                                       ⟦𝟚⟧                               ")

        # INPUT DETECTION
        while True:
            pressed_key = get_key()

            # INPUT EVALUATION
            if pressed_key == "1":
                clear()
                sys.exit()
            elif pressed_key == "2":
                clear()
                break

        break


#                                        ⊰═════ 𝑰𝑵𝑭𝑶𝑹𝑴𝑨𝑻𝑰𝑶𝑵 ═════⊱
def information():
    clear()
    play_sfx("pause.mp3", 100)
    center_text("⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱")
    center_text("                                           ┳  ┏          •                                              ")
    center_text("                                           ┃┏┓╋┏┓┏┓┏┳┓┏┓╋┓┏┓┏┓                                          ")
    center_text("                                           ┻┛┗┛┗┛┛ ┛┗┗┗┻┗┗┗┛┛┗                                          ")
    center_text("⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱")
    print()
    center_text("༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺                                                 ")
    center_text("                    𝑴𝑨𝑰𝑵 𝑶𝑩𝑱𝑬𝑪𝑻𝑰𝑽𝑬                                                                     ")
    center_text("──────────────────────────────────────────────────────                                                  ")
    center_text("             𝐹𝑖𝑛𝑑 𝑎 𝑤𝑎𝑦 𝑡𝑜 𝑔𝑜 𝑏𝑎𝑐𝑘 𝑡𝑜 𝑟𝑒𝑎𝑙𝑖𝑡𝑦…                                                              ")
    center_text("༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺                                                  ")
    print()
    center_text("                                                 ༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺")
    center_text("                                                                     𝑺𝑼𝑩-𝑶𝑩𝑱𝑬𝑪𝑻𝑰𝑽𝑬𝑺                     ")
    center_text("                                                  ──────────────────────────────────────────────────────")
    center_text("                                                                  𝐸𝑥𝑝𝑙𝑜𝑟𝑒 𝑎𝑙𝑙 𝑜𝑓 𝑡ℎ𝑒 𝑙𝑜𝑐𝑎𝑡𝑖𝑜𝑛𝑠                ")
    center_text("                                                                    𝐹𝑖𝑛𝑖𝑠ℎ 𝑎𝑙𝑙 𝑜𝑓 𝑡ℎ𝑒 𝑞𝑢𝑒𝑠𝑡𝑠                 ")
    center_text("                                                                      𝐷𝑒𝑓𝑒𝑎𝑡 𝑎𝑙𝑙 𝑏𝑜𝑠𝑠𝑒𝑠                     ")
    center_text("                                                   ༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺")
    print()
    center_text("༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺                                                 ")
    center_text("                     𝑯𝑶𝑾 𝑻𝑶 𝑷𝑳𝑨𝒀                                                                      ")
    center_text("──────────────────────────────────────────────────────                                                  ")
    center_text("   𝐸𝑛𝑡𝑒𝑟 𝑡𝘩𝑒 𝑎𝑠𝑠𝑖𝑔𝑛𝑒𝑑 𝑘𝑒𝑦 𝑜𝑟 𝑡𝑦𝑝𝑒 𝑤𝘩𝑎𝑡 𝑎𝑐𝑡𝑖𝑜𝑛 𝑦𝑜𝑢 𝑤𝑎𝑛𝑡 𝑡𝑜 𝑑𝑜                                                   ")
    center_text("                 𝑃𝑟𝑒𝑠𝑠 '𝑆𝑃𝐴𝐶𝐸' 𝑡𝑜 𝑐𝑜𝑛𝑡𝑖𝑛𝑢𝑒                                                                ")
    center_text("                𝑃𝑟𝑒𝑠𝑠 '𝑄' 𝑡𝑜 𝑠𝑘𝑖𝑝 𝑑𝑖𝑎𝑙𝑜𝑔𝑢𝑒𝑠                                                                ")
    center_text("             𝑃𝑟𝑒𝑠𝑠 '𝐼' 𝑡𝑜 𝑎𝑐𝑐𝑒𝑠𝑠 𝑦𝑜𝑢𝑟 𝑖𝑛𝑣𝑒𝑛𝑡𝑜𝑟𝑦                                                                   ")
    center_text("                  𝑃𝑟𝑒𝑠𝑠 '𝐻' 𝑡𝑜 𝑜𝑝𝑒𝑛 𝑡𝘩𝑖𝑠                                                              ")
    center_text("                𝑃𝑟𝑒𝑠𝑠 '𝑋' 𝑡𝑜 𝑞𝑢𝑖𝑡 𝑡𝘩𝑒 𝑔𝑎𝑚𝑒                                                                ")
    center_text("༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺                                                  ")
    print()
    press_space(True)
    clear()


# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                                            ┳┳┓┏┓┳┳┓  ┏┓┏┓┳┳┓┏┓
#                                            ┃┃┃┣┫┃┃┃  ┃┓┣┫┃┃┃┣
#                                            ┛ ┗┛┗┻┛┗  ┗┛┛┗┛ ┗┗┛
# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
def game(current_location = None):
#                       ⊰════════════════════════✦ 𝑰𝑵𝑻𝑹𝑶 ✦════════════════════════⊱
    clear()
    play_music("magic.mp3", 100, 100)
    for line in dialogues["intro"]:
        center_text("\033[33m⊰═════════════════════════════════════════════════════════════════════════════════════✦❘ ༻༺ ❘✦═════════════════════════════════════════════════════════════════════════════════════⊱\033[0m")
        print()
        center_text("\033[33m⊰═════════════════════════════════════════════════════════════════════════════════════✦❘ ༻༺ ❘✦═════════════════════════════════════════════════════════════════════════════════════⊱\033[0m")
        print("\033[F\033[F", end="")
        type_text(line, 0.05, True, True, "talk.mp3")
        print("\n")
        press_space(True)
        play_sfx("click.mp3", 100)
        clear()

#                     ⊰════════════════════════✦ 𝑬𝑿𝑷𝑳𝑶𝑹𝑰𝑵𝑮 ✦════════════════════════⊱
    # INITIALIZES AREA REQUIREMENTS
    required_items = {
        "Icy": "jacket",
        "Snow": "jacket",
        "Deep": "lantern",
        "Nuuk" : "grapple",
        "Hole" : "grapple"
    }

    # INITIALIZES THE LOCATION
    if current_location is None:
        current_location = "Lalaque Forest"

    # MUSIC
    while True:
        clear()
        if "Cave" in current_location:
            play_music("cave.mp3", 100)
        elif "Lalaque" in current_location:
            play_music("lalaque.mp3", 100)
        elif "Nuuk" in current_location:
            play_music("nuuk.mp3", 100)
        else:
            play_music("vavelia.mp3", 100)

        # EXPLORATION MENU
        options = paths[current_location]
        option_keys = list(options.keys())
        print(f"\n⊰════════════════════════✦ {current_location.upper()} ✦════════════════════════⊱")
        for i, k in enumerate(option_keys, 1):
            print(f"\033[1m[{i}]\033[0m{k} ⊱ {options[k]}")

        # INPUT DETECTION
        while True:
            result = None
            pressed_key = get_key()

            # INPUT EVALUATION
            try:
                if pressed_key.isdigit():
                    play_sfx("click.mp3")
                    choice = int(pressed_key) - 1

                    if 0 <= choice < len(option_keys):
                        result = options[option_keys[choice]]
                        break
            except AttributeError:
                continue

            if pressed_key == "H":
                information()
                break
            elif pressed_key == "I":
                show_inventory(inventory, player_data)
                break
            elif pressed_key == "S":
                save_game(player_data, inventory, current_location)
                break
            elif pressed_key == "L":
                data = load_game()

                if data:
                    player_data.update(data["player_data"])
                    inventory.update(data["inventory"])
                    current_location = data["current_location"]
                    paths.clear()
                    paths.update(data["paths"])
                    dialogues.clear()
                    dialogues.update(data["dialogues"])
                break
            elif pressed_key == "X":
                quit_detector()
                break

        # PATH EVALUATION
        try:
            # LOCATION
            # REQUIREMENT CHECKING
            if result in paths:
                blocked = False
                for keyword, equip_key in required_items.items():
                    if keyword in result and not player_data.get(equip_key):
                        clear()
                        center_text(f"You need a \033[96m{equip_key.capitalize()}\033[0m equipped to go there.")
                        press_space(True)
                        blocked = True
                        break

                # ASSIGNS NEW LOCATION
                if not blocked:
                    current_location = result

            # ITEM
            elif result in item_data:
                # ADDS ITEM TO INVENTORY
                if add_item(result):
                    type_text(f"\nYou picked up \033[96m{result}\033[0m!\n", 0.05, False, False, "talk.mp3")
                    time.sleep(1.5)

                    # REMOVES ITEM FROM PATH
                    for key in list(paths[current_location].keys()):
                        if paths[current_location][key] == result:
                            del paths[current_location][key]
                            break

            # NPC
            elif result in dialogues:
                # BOSSFIGHT
                required_orbs = ["Fire Orb", "Ice Orb", "Seed Orb", "Vavelia Orb"]
                if result == "???" and all(orb in inventory.values() for orb in required_orbs):
                    play_music("bossfight.mp3", 150, 50)
                    enemy_name = "Umbra"

                    clear()
                    type_text("\033[31mTHE END HAS BEGUN.\033[0m", 0.15, True, False, "talk.mp3")
                    time.sleep(1)

                    # COMBAT SYSTEM
                    while player_data["hp"] > 0 and enemy_data[enemy_name]["hp"] > 0:
                        player_action = ""
                        enemy_action = ""

                        render_combat(player_data, enemy_data, enemy_name, player_action, enemy_action)

                        center_text("\033[96mCHOOSE YOUR ACTION:\033[0m")
                        print()

                        player_result = players_turn(player_data, enemy_data, enemy_name)

                        if player_result == "Run":
                            enemy_data[enemy_name]["hp"] = enemy_data[enemy_name]["max_hp"]
                            break

                        if isinstance(player_result, str):
                            player_action = player_result

                        if enemy_data[enemy_name]["hp"] > 0:
                            enemy_action = enemys_turn(enemy_data, player_data, enemy_name)

                        render_combat(player_data, enemy_data, enemy_name, player_action, enemy_action)
                        print()
                        press_space(True)

                    if player_data["hp"] <= 0:
                        clear()
                        time.sleep(1)
                        center_text("\033[31m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
                        center_text("\033[31m                                  ┓┏┏┓┳┳  ┓ ┏┏┓┳┓┏┓  ┳┓┏┓┏┓┏┓┏┓┏┳┓┏┓┳┓                                   \033[0m")
                        center_text("\033[31m                                  ┗┫┃┃┃┃  ┃┃┃┣ ┣┫┣   ┃┃┣ ┣ ┣ ┣┫ ┃ ┣ ┃┃                                   \033[0m")
                        center_text("\033[31m                                  ┗┛┗┛┗┛  ┗┻┛┗┛┛┗┗┛  ┻┛┗┛┻ ┗┛┛┗ ┻ ┗┛┻┛                                   \033[0m")
                        center_text("\033[31m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
                        time.sleep(1)
                        press_space(True)
                        player_data["hp"] = player_data["max_hp"]
                        enemy_data[enemy_name]["hp"] = enemy_data[enemy_name]["max_hp"]

                    elif enemy_data[enemy_name]["hp"] <= 0:
                        clear()
                        play_music("ending.mp3", 200, 200)
                        time.sleep(2)
                        center_text("\033[93m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
                        center_text("\033[93m                                             ┓┏┏┓┳┳  ┓ ┏┏┓┳┓                                             \033[0m")
                        center_text("\033[93m                                             ┗┫┃┃┃┃  ┃┃┃┃┃┃┃                                             \033[0m")
                        center_text("\033[93m                                             ┗┛┗┛┗┛  ┗┻┛┗┛┛┗                                             \033[0m")
                        center_text("\033[93m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
                        time.sleep(5)
                        clear()
                        time.sleep(2)
                        type_text("After defeating the Umbra, you suddenly pass out", 0.05, True, False, "talk.mp3")
                        time.sleep(3)
                        clear()
                        type_text("You wake up.", 0.20, True, False, "talk.mp3")
                        time.sleep(2)
                        clear()
                        type_text("You found your way back to reality.", 0.05, True, False, "talk.mp3")
                        time.sleep(5)
                        clear()
                        type_text("Everything you did felt real. Yet, your journey ends here.", 0.05, True, False, "talk.mp3")
                        time.sleep(5)
                        clear()
                        type_text("\033[93mYou can stop walking in your past memories now...\033[0m", 0.10, True, False, "talk.mp3")
                        time.sleep(5)
                        clear()
                        sys.exit()
                else:
                    execute_npc(result)

            # ENEMY
            elif result in enemy_data:
                # MUSIC
                if "Golem" in result:
                    play_music("bossfight.mp3", 150, 50)
                else:
                    play_music("battle.mp3", 100, 100)

                # ASSIGNS ENEMY NAME
                enemy_name = result

                # COMBAT SYSTEM
                while player_data["hp"] > 0 and enemy_data[enemy_name]["hp"] > 0:
                    # INITIALIZES ACTIONS
                    player_action = ""
                    enemy_action = ""

                    # GUI
                    render_combat(player_data, enemy_data, enemy_name, player_action, enemy_action)

                    center_text("\033[96mCHOOSE YOUR ACTION:\033[0m")
                    print()

                    # INPUT EVALUATION
                    player_result = players_turn(player_data, enemy_data, enemy_name)

                    # RUN
                    if player_result == "Run":
                        enemy_data[enemy_name]["hp"] = enemy_data[enemy_name]["max_hp"]
                        break

                    # ACTION
                    if isinstance(player_result, str):
                        player_action = player_result

                    # ENEMY'S TURN
                    if enemy_data[enemy_name]["hp"] > 0:
                        enemy_action = enemys_turn(enemy_data, player_data, enemy_name)

                    # RERENDERS GUI
                    render_combat(player_data, enemy_data, enemy_name, player_action, enemy_action)
                    print()
                    press_space(True)

                # BATTLE ASSESSMENT
                # ENEMY VICTORY
                if player_data["hp"] <= 0:
                    # GUI
                    clear()
                    time.sleep(1)
                    center_text("\033[31m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
                    center_text("\033[31m                                  ┓┏┏┓┳┳  ┓ ┏┏┓┳┓┏┓  ┳┓┏┓┏┓┏┓┏┓┏┳┓┏┓┳┓                                   \033[0m")
                    center_text("\033[31m                                  ┗┫┃┃┃┃  ┃┃┃┣ ┣┫┣   ┃┃┣ ┣ ┣ ┣┫ ┃ ┣ ┃┃                                   \033[0m")
                    center_text("\033[31m                                  ┗┛┗┛┗┛  ┗┻┛┗┛┛┗┗┛  ┻┛┗┛┻ ┗┛┛┗ ┻ ┗┛┻┛                                   \033[0m")
                    center_text("\033[31m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
                    time.sleep(1)
                    press_space(True)

                    # RESETS HP
                    player_data["hp"] = player_data["max_hp"]
                    enemy_data[enemy_name]["hp"] = enemy_data[enemy_name]["max_hp"]

                # PLAYER VICTORY
                elif enemy_data[enemy_name]["hp"] <= 0:
                    # GUI
                    clear()
                    type_text(f"You defeated \033[31m{enemy_name}\033[0m!\n", 0.10, True, False, "talk.mp3")
                    time.sleep(1.5)

                    # RESETS HP
                    player_data["hp"] = player_data["max_hp"]

                    # LOOT DETECTION
                    loot = enemy_data[enemy_name].get("loot")
                    if loot:
                        if add_item(loot):
                            print()
                            type_text(f"You obtained \033[96m{loot}\033[0m!\n", 0.05, True, False, "talk.mp3")

                    print()
                    press_space(True)

                    # REMOVES ENEMY FROM PATHS
                    for key in list(paths[current_location].keys()):
                        if paths[current_location][key] == enemy_name:
                            del paths[current_location][key]
                            break
        except UnboundLocalError:
            pass



# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                                            ┳┳┓┏┓┳┳┓  ┳┳┓┏┓┳┓┳┳
#                                            ┃┃┃┣┫┃┃┃  ┃┃┃┣ ┃┃┃┃
#                                            ┛ ┗┛┗┻┛┗  ┛ ┗┗┛┛┗┗┛
# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                  ⊰════════════════════════✦ 𝑴𝑨𝑰𝑵 𝑴𝑬𝑵𝑼 𝑳𝑶𝑶𝑷 ✦════════════════════════⊱
while True:
    # MUSIC
    play_music("main_menu.mp3", 50, 500)

    # MAIN MENU
    clear()
    center_text("▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄\n")
    center_text("                       ▄▄▄▄▄▄                                         ▄▄▄           ▄▄ ▄▄                                        ")
    center_text("                       █▀██▀▀▀█▄                              █▄      ██▀▀█▄         ██ ██                                       ")
    center_text("                       ██▄▄▄█▀▄              ▀▀              ▄██▄     ██ ▄█▀         ██ ██           ▄                           ")
    center_text("                       ██▀▀▀  ████▄▄ ███▄   ██  ▄█▀█▄  ▄███▀  ██      ██▀▀█▄  ▄█▀█▄  ██ ██   ██ ██   ███▄███▄                    ")
    center_text("                     ▄ ██     ██     ██ ██  ██ ██▄█▀  ██      ██    ▄ ██  ▄█  ██▄█▀  ██ ██   ██ ██   ██ ██ ██                    ")
    center_text("                     ▀██▀    ▄█▀    ▄▀███▀ ▄██ ▀█▄▄▄   ▀███ ▄▄██    ▀██████▀▄ ▀█▄▄▄▄ ██▄██▄  ▀██▀  █▄██ ██ ▀█                    \n")
    center_text("▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄༻⟡༺▄▄▄\n")
    center_text("                                     ༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺                                     ")
    center_text("                                                            ┏┓┓ ┏┓┓┏                                                            ")
    center_text("                                                            ┃┃┃ ┣┫┗┫                                                            ")
    center_text("                                                            ┣┛┗┛┛┗┗┛                                                            ")
    center_text("                                     ༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺                                     ")
    center_text("                                                              ⟦𝟙⟧                                                               ")
    center_text("                                     ༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺                                     ")
    center_text("                                                     ┳┳┓┏┓┏┓┳┓┳┳┓┏┓┏┳┓┳┏┓┳┓                                                     ")
    center_text("                                                     ┃┃┃┣ ┃┃┣┫┃┃┃┣┫ ┃ ┃┃┃┃┃                                                     ")
    center_text("                                                     ┻┛┗┻ ┗┛┛┗┛ ┗┛┗ ┻ ┻┗┛┛┗                                                     ")
    center_text("                                     ༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺                                     ")
    center_text("                                                              ⟦𝟚⟧                                                               ")
    center_text("                                     ༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺                                     ")
    center_text("                                                            ┏┓┳┳┳┏┳┓                                                            ")
    center_text("                                                            ┃┃┃┃┃ ┃                                                             ")
    center_text("                                                            ┗┻┗┛┻ ┻                                                             ")
    center_text("                                     ༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺                                     ")
    center_text("                                                              ⟦𝟛⟧                                                               ")

    # INPUT DETECTION
    while True:
        pressed_key = get_key()

        # INPUT EVALUATION
        if pressed_key == "1":
            game()
            break
        elif pressed_key == "2":
            information()
            break
        elif pressed_key == "3":
            quit_detector()
            break