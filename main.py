# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                                             ┓ ┳┳┓┳┓┏┓┳┓┳┏┓┏┓
#                                             ┃ ┃┣┫┣┫┣┫┣┫┃┣ ┗┓
#                                             ┗┛┻┻┛┛┗┛┗┛┗┻┗┛┗┛
# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                     ⊰════════════════════════✦ 𝑰𝑴𝑷𝑶𝑹𝑻𝑰𝑵𝑮 ✦════════════════════════⊱
import json
import time
import random
import sys
import os
import shutil
import msvcrt
import pygame

#                  ⊰════════════════════════✦ 𝑬𝑹𝑹𝑶𝑹 𝑯𝑨𝑵𝑫𝑳𝑰𝑵𝑮 ✦════════════════════════⊱
try:
    import keyboard
except ImportError as keyboard:
    print(
        "\033[31m𝐸𝑟𝑟𝑜𝑟: 𝑀𝑜𝑑𝑢𝑙𝑒 '𝑘𝑒𝑦𝑏𝑜𝑎𝑟𝑑' 𝑛𝑜𝑡 𝑓𝑜𝑢𝑛𝑑. 𝑃𝑙𝑒𝑎𝑠𝑒 𝑖𝑛𝑠𝑡𝑎𝑙𝑙 𝑖𝑡 𝑎𝑛𝑑 𝑡𝑟𝑦 𝑎𝑔𝑎𝑖𝑛.\033[0m")
    sys.exit()

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
#                    ⊰════════════════════════✦ 𝑻𝑬𝑿𝑻 𝑬𝑭𝑭𝑬𝑪𝑻𝑺 ✦════════════════════════⊱
#                                        ⊰═════ 𝑻𝒀𝑷𝑰𝑵𝑮 𝑬𝑭𝑭𝑬𝑪𝑻 ═════⊱
def type_text(text, speed, centered = False, skip = False):
    if centered:
        width = shutil.get_terminal_size().columns
        padding = (width - len(text)) // 2
        print(" " * max(padding, 0), end="")

    i = 0
    length = len(text)

    while i < length:
        if skip and keyboard.is_pressed("q"):
            print(text[i:], end="", flush=True)
            break

        print(text[i], end="", flush=True)
        time.sleep(speed)
        i += 1


#                                        ⊰═════ 𝑪𝑬𝑵𝑻𝑬𝑹 𝑬𝑭𝑭𝑬𝑪𝑻 ═════⊱
def center_text(text):
    width = shutil.get_terminal_size().columns
    print(text.center(width))


#                                        ⊰═════ 𝑹𝑬𝑺𝑬𝑻 𝑬𝑭𝑭𝑬𝑪𝑻 ═════⊱
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


#                                      ⊰═════ 𝑫𝑰𝑨𝑳𝑶𝑮𝑼𝑬 𝑬𝑭𝑭𝑬𝑪𝑻 ═════⊱
def press_space(space_prompt = False):
    if space_prompt:
        print("\033[33m𝑷𝒓𝒆𝒔𝒔 𝒔𝒑𝒂𝒄𝒆 𝒕𝒐 𝒄𝒐𝒏𝒕𝒊𝒏𝒖𝒆 ➤ \033[0m")
        keyboard.wait("space")
    else:
        print("\033[33m➤ \033[0m", end="", flush=True)
        keyboard.wait("space")

    while msvcrt.kbhit():
        msvcrt.getch()

#                 ⊰════════════════════════✦ 𝑫𝑰𝑨𝑳𝑶𝑮𝑼𝑬 𝑴𝑬𝑪𝑯𝑨𝑵𝑰𝑪𝑺 ✦════════════════════════⊱
#                                      ⊰═════ 𝑪𝑶𝑵𝑫𝑰𝑻𝑰𝑶𝑵 𝑪𝑯𝑬𝑪𝑲𝑬𝑹 ═════⊱
def check_conditions(conditions, dialogue_block):
# 𝑰𝑵𝑽𝑬𝑵𝑻𝑶𝑹𝒀 𝑪𝑯𝑬𝑪𝑲𝑬𝑹
    for item in conditions:
        if item not in inventory.values():
            return False

# 𝑻𝑨𝑲𝑬𝑺 𝑹𝑬𝑸𝑼𝑰𝑹𝑬𝑫 𝑰𝑻𝑬𝑴𝑺
    for item in conditions:
        for slot in inventory:
            if inventory[slot] == item:
                inventory[slot] = "Empty"
                break

# 𝑮𝑰𝑽𝑬𝑺 𝑻𝑯𝑬 𝑹𝑬𝑾𝑨𝑹𝑫
    for slot in inventory:
        if inventory[slot] == "Empty":
            inventory[slot] = dialogue_block["reward"]
            break

    return True

#                                      ⊰═════ 𝑫𝑰𝑨𝑳𝑶𝑮𝑼𝑬 𝑬𝑿𝑬𝑪𝑼𝑻𝑶𝑹 ═════⊱
def execute_dialogue(dialogue_block):
# 𝑷𝑹𝑰𝑵𝑻𝑺 𝑫𝑰𝑨𝑳𝑶𝑮𝑼𝑬 𝑰𝑵 𝑨 𝑻𝑬𝑿𝑻 𝑩𝑶𝑿
    clear()
    for line in dialogue_block["lines"]:
        center_text("\033[33m⊰══════════════════════════════════════════════════════════════════════════════════════════✦❘ ༻༺ ❘✦══════════════════════════════════════════════════════════════════════════════════════════⊱\033[0m")
        print()
        center_text("\033[33m⊰══════════════════════════════════════════════════════════════════════════════════════════✦❘ ༻༺ ❘✦══════════════════════════════════════════════════════════════════════════════════════════⊱\033[0m")
        print("\033[F\033[F", end="")
        type_text(line, 0.05, True, True)
        print("\n")
        press_space(True)
        clear()

#                                      ⊰═════ 𝑵𝑷𝑪 𝑬𝑿𝑬𝑪𝑼𝑻𝑶𝑹 ═════⊱
def execute_npc(npc):
# 𝑰𝑵𝑰𝑻𝑰𝑨𝑳𝑰𝒁𝑬𝑺 𝑻𝑯𝑬 𝑭𝑨𝑳𝑳𝑩𝑨𝑪𝑲
    incomplete_dialogue = None

# 𝑫𝑰𝑨𝑳𝑶𝑮𝑼𝑬 𝑺𝑻𝑨𝑮𝑬 𝑬𝑽𝑨𝑳𝑼𝑨𝑻𝑶𝑹
    for dialogue_block in dialogues[npc]:
        condition = dialogue_block.get("conditions")

# 𝑰𝑵𝑰𝑻𝑰𝑨𝑳𝑰𝒁𝑬𝑺 𝑻𝑯𝑬 𝑭𝑨𝑳𝑳𝑩𝑨𝑪𝑲
        if condition == "Incomplete":
            incomplete_dialogue = dialogue_block
            continue

# 𝑸𝑼𝑬𝑺𝑻 𝑫𝑬𝑻𝑨𝑰𝑳𝑺
        if condition is None and dialogue_block.get("access"):
            execute_dialogue(dialogue_block)
            dialogue_block["access"] = False

            for d_block in dialogues[npc]:
                if isinstance(d_block["conditions"], list):
                    d_block["access"] = True
                if d_block["conditions"] == "Incomplete":
                    d_block["access"] = True
            return

# 𝑸𝑼𝑬𝑺𝑻 𝑪𝑯𝑬𝑪𝑲𝑬𝑹
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
# 𝑷𝑶𝑺𝑻-𝑸𝑼𝑬𝑺𝑻 𝑫𝑰𝑨𝑳𝑶𝑮𝑼𝑬
        elif condition == "Finished" and dialogue_block.get("access"):
            execute_dialogue(dialogue_block)
            return

# 𝑸𝑼𝑬𝑺𝑻 𝑪𝑶𝑵𝑫𝑰𝑻𝑰𝑶𝑵𝑺 𝑵𝑶𝑻 𝑴𝑬𝑻
    if incomplete_dialogue:
        execute_dialogue(incomplete_dialogue)

def show_inventory(inv):
    clear()
    center_text("\033[92m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
    center_text("\033[92m                                           ┳┳┓┓┏┏┓┳┓┏┳┓┏┓┳┓┓┏                                            \033[0m")
    center_text("\033[92m                                           ┃┃┃┃┃┣ ┃┃ ┃ ┃┃┣┫┗┫                                            \033[0m")
    center_text("\033[92m                                           ┻┛┗┗┛┗┛┛┗ ┻ ┗┛┛┗┗┛                                            \033[0m")
    center_text("\033[92m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
    center_text("\033[92m                                     『 𝑺𝑳𝑶𝑻 』   ✦   『 𝑰𝑻𝑬𝑴 』                                        \033[0m")
    center_text("\033[93m══════════════════════════════════════════════════\033[0m")
    for slot in inventory:
        center_text(f"\033[92m{slot} ➣ {inventory[slot]}\033[0m")
        center_text("\033[93m══════════════════════════════════════════════════\033[0m")
    press_space(True)
#                 ⊰════════════════════════✦ 𝑭𝑰𝑮𝑯𝑻𝑰𝑵𝑮 𝑴𝑬𝑪𝑯𝑨𝑵𝑰𝑪𝑺 ✦════════════════════════⊱
#                                     ⊰═════ 𝑯𝑰𝑻𝑹𝑨𝑻𝑬 𝑪𝑨𝑳𝑪𝑼𝑳𝑨𝑻𝑰𝑶𝑵 ═════⊱
def player_hit_success(p_data, e_data, enemy_key):
    p_agility = p_data["agility"]
    e_agility = e_data[enemy_key]["agility"]

    chance = 0.5 + (p_agility - e_agility) * 0.05
    chance = max(0.0, min(1.0, chance))
    return random.random() < chance


def enemy_hit_success(e_data, p_data, enemy_key):
    e_agility = e_data[enemy_key]["agility"]
    p_agility = p_data["agility"]

    chance = 0.5 + (e_agility - p_agility) * 0.05
    chance = max(0.0, min(1.0, chance))
    return random.random() < chance


#                                     ⊰═════ 𝑫𝑨𝑴𝑨𝑮𝑬 𝑪𝑨𝑳𝑪𝑼𝑳𝑨𝑻𝑰𝑶𝑵 ═════⊱
def player_attack(p_data, e_data, enemy_key):
    p_attack = p_data["attack"]
    e_defense = e_data[enemy_key]["defense"]

    damage = max(1, p_attack - e_defense // 2)
    e_data[enemy_key]["hp"] -= damage

    e_hp = e_data[enemy_key]['hp']
    type_text(f"You hit {enemy_key} for {damage} damage! {enemy_key} has {e_hp}HP left!\n", 0.05)
    return damage


def enemy_attack(e_data, p_data, enemy_key):
    e_attack = e_data[enemy_key]["attack"]
    p_defense = p_data["defense"]

    damage = max(1, e_attack - p_defense // 2)
    p_data["hp"] -= damage

    p_hp = p_data['hp']
    type_text(f"{enemy_key} hit you for {damage} damage! You have {p_hp}HP left!\n", 0.05)
    return damage


#                                        ⊰═════ 𝑻𝑼𝑹𝑵 𝑺𝒀𝑺𝑻𝑬𝑴 ═════⊱
def players_turn(p_data, e_data, enemy_key):
    p_agility = p_data["agility"]
    e_agility = e_data[enemy_key]["agility"]

    if p_agility >= e_agility:
        type_text("\nIt's your turn!\n", 0.10)
    else:
        type_text(f"It's {enemy_key}'s turn!\n", 0.10)
        return False

    action = input(
        "\n\033[33m༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺\033[0m"
        "\n\033[33m⟦𝟙⟧ 𝑨𝑻𝑻𝑨𝑪𝑲\033[0m"
        "\n\033[33m⟦𝟚⟧ 𝑹𝑼𝑵\033[0m"
        "\n\033[33m༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺\033[0m"
        "\n\033[33m𝑨𝑪𝑻𝑰𝑶𝑵: \033[0m"
    )

    if action.strip() == "1":
        if player_hit_success(p_data, e_data, enemy_key):
            player_attack(p_data, e_data, enemy_key)
        else:
            type_text(f"{enemy_key} dodged your attack!\n", 0.05)
        return True
    elif action.strip() == "2":
        type_text("You ran away from the enemy...\n", 0.20)
        return False
    else:
        clear()
        center_text("\033[31m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
        center_text("\033[31m                                          ┳      ┓• ┓  ┳                                                 \033[0m")
        center_text("\033[31m                                          ┃┏┓┓┏┏┓┃┓┏┫  ┃┏┓┏┓┓┏╋                                          \033[0m")
        center_text("\033[31m                                          ┻┛┗┗┛┗┻┗┗┗┻  ┻┛┗┣┛┗┻┗                                          \033[0m")
        center_text("\033[31m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
        press_space(True)
        return players_turn(p_data, e_data, enemy_key)


def enemys_turn(e_data, p_data, enemy_key):
    if enemy_hit_success(e_data, p_data, enemy_key):
        enemy_attack(e_data, p_data, enemy_key)
    else:
        print("You successfully dodged the enemy's attack!\n")


# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                                      ┏┓┏┓┳┳┓┏┓  ┏┓┳┳┳┓┏┓┏┳┓┳┏┓┳┓┏┓
#                                      ┃┓┣┫┃┃┃┣   ┣ ┃┃┃┃┃  ┃ ┃┃┃┃┃┗┓
#                                      ┗┛┛┗┛ ┗┗┛  ┻ ┗┛┛┗┗┛ ┻ ┻┗┛┛┗┗┛
# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                                            ⊰═════ 𝑸𝑼𝑰𝑻 ═════⊱
def quit_detector():
    while True:
        clear()
        center_text("⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱")
        center_text("                                              ┏┓┏┓┳┳┏┓┏┓┳┓                                               ")
        center_text("                                              ┃┃┣┫┃┃┗┓┣ ┃┃                                               ")
        center_text("                                              ┣┛┛┗┗┛┗┛┗┛┻┛                                               ")
        center_text("⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\n")
        center_text("                                       𝑫𝒐 𝒚𝒐𝒖 𝒘𝒂𝒏𝒕 𝒕𝒐 𝒆𝒙𝒊𝒕 𝒕𝒉𝒆 𝒈𝒂𝒎𝒆?                                      \n")
        center_text("                 ༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺           ༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺                 ")
        center_text("                                𝒀𝑬𝑺                                   𝑵𝑶                               ")
        center_text("                 ༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺           ༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺                 ")
        center_text("                                ⟦𝟙⟧                                   ⟦𝟚⟧                               \n")
        response = input(
            "\n\033[33m༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺\033[0m"
            "\n\033[33m𝑨𝑪𝑻𝑰𝑶𝑵: \033[0m"
        )

        if response.strip() == "1":
            clear()
            sys.exit()
        elif response.strip() == "2":
            clear()
            break
        else:
            clear()
            center_text("\033[31m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
            center_text("\033[31m                                          ┳      ┓• ┓  ┳                                                 \033[0m")
            center_text("\033[31m                                          ┃┏┓┓┏┏┓┃┓┏┫  ┃┏┓┏┓┓┏╋                                          \033[0m")
            center_text("\033[31m                                          ┻┛┗┗┛┗┻┗┗┗┻  ┻┛┗┣┛┗┻┗                                          \033[0m")
            center_text("\033[31m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
            press_space(True)
            continue


#                                        ⊰═════ 𝑰𝑵𝑭𝑶𝑹𝑴𝑨𝑻𝑰𝑶𝑵 ═════⊱
def information():
    clear()
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
def game():
#                       ⊰════════════════════════✦ 𝑰𝑵𝑻𝑹𝑶 ✦════════════════════════⊱
    clear()
    for line in dialogues["intro"]:
        center_text("\033[33m⊰══════════════════════════════════════════════════════════════════════════════════════════✦❘ ༻༺ ❘✦══════════════════════════════════════════════════════════════════════════════════════════⊱\033[0m")
        print()
        center_text("\033[33m⊰══════════════════════════════════════════════════════════════════════════════════════════✦❘ ༻༺ ❘✦══════════════════════════════════════════════════════════════════════════════════════════⊱\033[0m")
        print("\033[F\033[F", end="")
        type_text(line, 0.05, True, True)
        print("\n")
        press_space(True)
        clear()

    current_location = "Lalaque Forest"

#                     ⊰════════════════════════✦ 𝑬𝑿𝑷𝑳𝑶𝑹𝑰𝑵𝑮 ✦════════════════════════⊱
    while True:
        clear()
        print(f"\n⊰════════════════════════✦ {current_location.upper()} ✦════════════════════════⊱")
        options = paths[current_location]
        for k in options:
            print(f"{k} ⊱ {options[k]}")

#                       ⊰════════════════════════✦ 𝑰𝑵𝑷𝑼𝑻 ✦════════════════════════⊱
        command = input(
            "\n\033[33m༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺\033[0m"
            "\n\033[33m𝑨𝑪𝑻𝑰𝑶𝑵: \033[0m"
        )

#                 ⊰════════════════════════✦ 𝑰𝑵𝑷𝑼𝑻 𝑬𝑽𝑨𝑳𝑼𝑨𝑻𝑰𝑶𝑵 ✦════════════════════════⊱
        if command.upper().strip() == "I":
            show_inventory(inventory)

        if command.upper().strip() == "H":
            clear()
            information()
            continue

        if command.upper().strip() == "X":
            quit_detector()

        result = None
        found = False

        for k in options:
            if command.upper().replace(" ", "") == k.upper().replace(" ", ""):
                result = options[k]
                found = True
                break

        if not found:
            clear()
            center_text("\033[31m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
            center_text("\033[31m                                          ┳      ┓• ┓  ┳                                                 \033[0m")
            center_text("\033[31m                                          ┃┏┓┓┏┏┓┃┓┏┫  ┃┏┓┏┓┓┏╋                                          \033[0m")
            center_text("\033[31m                                          ┻┛┗┗┛┗┻┗┗┗┻  ┻┛┗┣┛┗┻┗                                          \033[0m")
            center_text("\033[31m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
            press_space(True)
            continue

#                       ⊰════════════════════════✦ 𝑬𝑿𝑷𝑳𝑶𝑹𝑰𝑵𝑮 ✦════════════════════════⊱
        if result in paths:
            current_location = result

        elif result in dialogues:
            execute_npc(result)

#                     ⊰════════════════════════✦ 𝑪𝑶𝑴𝑩𝑨𝑻 𝑺𝒀𝑺𝑻𝑬𝑴 ✦════════════════════════⊱
        elif result in enemy_data:
            enemy_name = result

            while player_data["hp"] > 0 and enemy_data[enemy_name]["hp"] > 0:
                player_first = players_turn(player_data, enemy_data, enemy_name)

                if player_first is False:
                    break

                if enemy_data[enemy_name]["hp"] > 0:
                    enemys_turn(enemy_data, player_data, enemy_name)

#                   ⊰════════════════════════✦ 𝑩𝑨𝑻𝑻𝑳𝑬 𝑨𝑺𝑺𝑬𝑺𝑺𝑴𝑬𝑵𝑻 ✦════════════════════════⊱
            if player_data["hp"] <= 0:
                type_text("You were defeated...", 0.25)
            elif enemy_data[enemy_name]["hp"] <= 0:
                type_text(f"You defeated {enemy_name}!\n", 0.10)


# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                                            ┳┳┓┏┓┳┳┓  ┳┳┓┏┓┳┓┳┳
#                                            ┃┃┃┣┫┃┃┃  ┃┃┃┣ ┃┃┃┃
#                                            ┛ ┗┛┗┻┛┗  ┛ ┗┗┛┛┗┗┛
# ⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱
#                  ⊰════════════════════════✦ 𝑴𝑨𝑰𝑵 𝑴𝑬𝑵𝑼 𝑳𝑶𝑶𝑷 ✦════════════════════════⊱
while True:
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

#                   ⊰════════════════════════✦ 𝑰𝑵𝑷𝑼𝑻 ✦════════════════════════⊱
    choice = input(
        "\n\033[33m༻━━━༺༻━━━༺༻━━━༺༻━━━༺༻━━━༺\033[0m"
        "\n\033[33m𝑨𝑪𝑻𝑰𝑶𝑵: \033[0m"
    )

#             ⊰════════════════════════✦ 𝑰𝑵𝑷𝑼𝑻 𝑬𝑽𝑨𝑳𝑼𝑨𝑻𝑰𝑶𝑵 ✦════════════════════════⊱
    if choice.strip() == "1":
        game()
    elif choice.strip() == "2":
        information()
    elif choice.strip() == "3":
        quit_detector()
    else:
        clear()
        center_text("\033[31m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
        center_text("\033[31m                                          ┳      ┓• ┓  ┳                                                 \033[0m")
        center_text("\033[31m                                          ┃┏┓┓┏┏┓┃┓┏┫  ┃┏┓┏┓┓┏╋                                          \033[0m")
        center_text("\033[31m                                          ┻┛┗┗┛┗┻┗┗┗┻  ┻┛┗┣┛┗┻┗                                          \033[0m")
        center_text("\033[31m⊰═══════════════════════════════════════════════✦❘ ༻༺ ❘✦═══════════════════════════════════════════════⊱\033[0m")
        press_space(True)