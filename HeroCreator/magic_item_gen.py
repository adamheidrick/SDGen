import logging

# from hero_logger import start_logger  # Remove this after tied into rest of program

from HeroCreator.magic_item_names import generate_name
from HeroCreator.armor import magical_armor
from HeroCreator.potion_crafting import make_potion
from HeroCreator.weapons import magical_weapon
from HeroCreator.magic_ulitity import make_magic_utility
from HeroCreator.scroll_crafting import make_magic_scroll_wand
from HeroCreator.character import Character

logger = logging.getLogger(__name__)
# start_logger()  # Remove this after tied into rest of program

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
    personality = calculate_personality_roll()
    log_magical_item(name, item_type, item_name, bonus, quality, personality)
    item = craft_item(item_type, quality, personality, name, item_name)
    return item


def log_magical_item(name, item_type, item_name, bonus, quality, personality):
    logger.info(
        f"Generated Name: {name}, Item Type: {item_type}, and Item Description: {item_name}"
    )
    logger.info(f"Generated Bonus: {bonus}")
    logger.info(f"Generated Quality: {quality}")
    logger.info(f"Generated Personality: {personality}")


def calculate_quality_roll(bonus):
    if bonus < 7:
        bonus = 0
    elif bonus <= 7:
        bonus = 1
    elif bonus <= 11:
        bonus = 2
    else:
        bonus = 3
    return Qualities[bonus]


def calculate_personality_roll():
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
    match item_type:
        case "Armor":
            return magical_armor(quality, personality, name, item_name)
        case "Potion":
            return make_potion(quality, name)
        case "Scroll":
            return make_magic_scroll_wand(quality, name, item_type)
        case "Utility":
            return make_magic_utility(quality, name, item_name)
        case "Wand":
            return make_magic_scroll_wand(quality, name, item_type)
        case "Weapon":
            return magical_weapon(quality, personality, name, item_name)


def magical_item():
    return generate_magical_item()
