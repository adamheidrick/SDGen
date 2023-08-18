from HeroCreator.magic_item_functions import choosing_qualities
from HeroCreator.personality import *

elements = ["Fire", "Cold", "Electricity", "Poison"]

utility_features = ["Shaped like a raven.",
                    "Iridescent.",
                    "Cruel spikes and spines.",
                    "Made from a big frog.",
                    "Gem-studded.",
                    "Gold thread/hardware.",
                    "Made of basilisk hide.",
                    "Possessed by a spirit.",
                    "Made of shaped smoke.",
                    "Covered in small thorns.",
                    "Made with rare feathers.",
                    "Has tiny wings.",
                    "Slowly changes colors.",
                    "Shaped like a bat.",
                    "Tarnished silver hardware.",
                    "Made of spider-silk.",
                    "Hums quiet, sweet tones.",
                    "Jolts of pain at first touch.",
                    "Throbs like a heart.",
                    "Trails faint mist."]

utility_benefit = ["You can't be magically scryed upon or detected.",
                   "Connects to an interdimensional pocket with 5 gear slots.",
                   "A stat becomes 18 (+4) while using/wearing item.",
                   "Once per day, teleport a near distance.",
                   "Harmful spells that target you are DC 15 to cast.",
                   f"You're immune to 1d4: {random.choice(elements)}.",
                   "Sense secret doors when they're within close range.",
                   "You can see invisible and incorporeal creatures.",
                   "Your movement isn't hindered by any terrain.",
                   "You can hold your breath for 1 hour.",
                   "You do not need to eat or drink to survive.",
                   "You can walk on non-solid surfaces for 2 rounds at a time."]

utility_curse = ["Slowly rots all other non-magical items that touch it"
                 "Deals 1d4 damage and leaves blisters whenever used",
                 "Item attracts bad weather to its location",
                 "You cannot be healed by magic; only by resting",
                 "Crashes like a gong whenever wielder slays a creature",
                 "Item attracts all undead within a far distance",
                 "Temporarily loses magic if doused in water",
                 "You have disadvantage on CON checks",
                 "You are compelled to light parchment objects on fire",
                 "You must drink blood once a day or take 1d8 damage",
                 "Item must eat 1d10 gp a day or it loses its magic until fed.",
                 "Item has horrid smell that makes all your CHA checks hard."]


def make_magic_utility(qualities, name, item_name):
    feature = random.choice(utility_features)
    qualities = choosing_qualities(qualities, utility_curse, utility_benefit)
    magic_utility = {"Magical Utility": name, "Type": item_name, "Features": feature,
                     "Qualities": qualities}
    return magic_utility
