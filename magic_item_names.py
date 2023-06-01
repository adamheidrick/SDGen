import random
from weapons import Weapons, Arrows

names = ["The Crimson", "The Ashen", "Ortival's", "The Doom", "The Twilight", "The Astral",
         "Krull's", "The Vicious", "Memmon's", "The Blessed", "The Infernal", "Madeera's",
         "The Whispering", "The Unholy", "Shune's", "The Lost", "Ord's", "The Righteous",
         "The Demonic", "The Primordial"]

item_type_names = {"Armor": ["Shield", "Armor"],
                   "Potion": ["Poultice", "Elixir", "Concoction", "Brew", "Tincture", "Draught"],
                   "Scroll": ["Rite", "Scroll", "Tome", "Script", "Book", "Lyrics"],
                   "Utility": ["Brooch", "Ring", "Boots", "Cloak", "Amulet", "Flask", "Circlet", "Eye-patch",
                               "Gauntlets", "Holy Symbol", "Hat", "Goblet", "Helm", "Statuette", "Goggles", "Bag",
                               "Rock", "Surcoat", "Mask"],
                   "Weapon": list(Weapons) + list(Arrows),
                   "Wand": ["Wand", "Rod"]}

item_description = ["of Thundering Death", "of Ages", "of the Archmage", "of Destruction", "of Brak", "of Power",
                    "of the Covenant", "of the Wilds", "of the Horde", "of Blood", "of Time", "of the Lich Queen",
                    "of the Elders", "of Madness", "of Withering", "of Annihilation", "of the Dragon", "of the Risen",
                    "of Elemental Fury", "of the Spirits"]


def generate_name():
    prefix = random.choice(names)
    item_type = random.choice(list(item_type_names))
    item_name = random.choice(item_type_names[item_type])
    suffix = random.choice(item_description)
    magical_item_name = prefix + ' ' + item_name + ' ' + suffix
    return magical_item_name, item_type, item_name

