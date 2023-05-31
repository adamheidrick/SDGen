import random
from magic_item_names import generate_name
from armor import magical_armor, calculate_quality_roll

Curse = "curse"
Benefit = "benefit"
Flaw = "flaw"
Virtue = "virtue"

Qualities = [(None, Curse), (Benefit, Curse), (Benefit, None), (Benefit, Benefit)]
Personality = [(None, Flaw), (None, None), (Virtue, Flaw), (Virtue, None)]

name, item_type = generate_name()
quality = Qualities[calculate_quality_roll()]

match item_type:
    case 'Armor':
        print("Armor")
        armor = magical_armor(quality, random.choice(Personality), name)
    case 'Potion':
        print("Potion")
    case 'Scroll':
        print("Scroll")
    case "Utility":
        print("Utility")
    case "Wand":
        print("Wand")
    case "Weapon":
        print("Weapon")
