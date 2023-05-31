import random
from magic_item_names import generate_name
from armor import magical_armor
from character import Character

Curse = "curse"
Benefit = "benefit"
Flaw = "flaw"
Virtue = "virtue"

Qualities = [(None, Curse), (Benefit, Curse), (Benefit, None), (Benefit, Benefit)]
Personality = [(None, Flaw), (None, None), (Virtue, Flaw), (Virtue, None)]


def generate_magical_item():
    name, item_type, item_name = generate_name()
    bonus = sum(Character.roll_dice(6, 2))
    quality = calculate_quality_roll(bonus)
    personality = calculate_personality_roll(bonus)
    item = craft_item(item_type, quality, personality, name, item_name)
    print(item)


def calculate_quality_roll(bonus):
    if bonus <= 3:
        bonus = 0
    elif bonus <= 7:
        bonus = 1
    elif bonus <= 11:
        bonus = 2
    else:
        bonus = 3
    return Qualities[bonus]


def calculate_personality_roll(bonus):
    bonus = sum(Character.roll_dice(6, 2))
    if bonus <= 3:
        bonus = 0
    elif bonus <= 9:
        bonus = 1
    elif bonus <= 11:
        bonus = 2
    else:
        bonus = 3
    return Personality[bonus]


def craft_item(item_type, quality, personality, name, item_name):
    item_type = 'Potion'
    match item_type:
        case 'Armor':
            print("Armor")
            return magical_armor(quality, personality, name, item_name)
        case 'Potion':
            print("Potion")
            return 'Potion'
        case 'Scroll':
            print("Scroll")
            return 'Scroll'
        case "Utility":
            print("Utility")
            return 'Utility'
        case "Wand":
            print("Wand")
            return 'Wand'
        case "Weapon":
            print("Weapon")
            return 'Weapon'


generate_magical_item()
