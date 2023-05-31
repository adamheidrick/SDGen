import random
from weapons import Weapons

names = ["The Crimson", "The Ashen", "Ortival's", "The Doom", "The Twilight", "The Astral",
         "Krull's", "The Vicious", "Memmon's", "The Blessed", "The Infernal", "Madeera's",
         "The Whispering", "The Unholy", "Shune's", "The Lost", "Ord's", "The Righteous",
         "The Demonic", "The Primordial"]

weapon_type_names = {"Armor": ["Shield", "Armor"],
                     "Potion": ["Poultice", "Elixir"],
                     "Scroll": ["Rite", "Scroll", "Tome", ],
                     "Utility": ["Cape", "Skull", "Orb", "Eye"],
                     "Weapon": list(Weapons),
                     "Wand": ["Wand", "Rod"]}

item_description = ["of Thundering Death", "of Ages", "of the Archmage", "of Destruction", "of Brak", "of Power",
                    "of the Covenant", "of the Wilds", "of the Horde", "of Blood", "of Time", "of the Lich Queen",
                    "of the Elders", "of Madness", "of Withering", "of Annihilation", "of the Dragon", "of the Risen",
                    "of Elemental Fury", "of the Spirits"]


def generate_name():
    prefix = random.choice(names)
    item_type = random.choice(list(weapon_type_names))
    item_name = random.choice(weapon_type_names[item_type])
    suffix = random.choice(item_description)
    magical_item_name = prefix + ' ' + item_name + ' ' + suffix
    return magical_item_name, item_type


