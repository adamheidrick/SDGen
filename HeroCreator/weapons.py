from HeroCreator.character import Character
from HeroCreator.magic_item_functions import choosing_qualities
from HeroCreator.personality import *

animals = ['Wolf', 'Raven', 'Dragon', 'Bear', 'Sloth', 'Rabbit', 'Tiger', 'Cat', 'Horse']
foes = ["Undead", "Demons", "Dragons", "Undead"]
unseen_foes = ["Undead", "Demons", "Snakes", "Spiders"]
Weapons = {
            "Bastard Sword": ["Type: M", "Range: C", "Damage: 1d8/1d10", "Properties: V, 2 slots"],
            "Club": ["Type: M", "Range: C", "Damage: 1d4", "Properties None"],
            "Crossbow": ["Type: R", "Range: F", "Damage: 1d6", "Properties: 2H, L"],
            "Dagger": ["Type: M/R", "Range: C/N", "Damage: 1d4", "Properties: F, Thrown"],
            "Greataxe": ["Type: M", "Range: C/N", "Damage: 1d4", "Properties: V, 2 slots"],
            "Greatsword": ["Type: M", "Range: C", "Damage: 1d12", "Properties: 2H, 2 slots"],
            "Javelin": ["Type: M/R", "Range: C/F", "Damage: 1d4", "Properties: Thrown"],
            "Longbow": ["Type: R", "Range: F", "Damage: 1d8", "Properties: 2H"],
            "Longsword": ["Type: M", "Range: C", "Damage: 1d8", "Properties: None"],
            "Mace": ["Type: M", "Range: C", "Damage: 1d6", "Properties: None"],
            "Shortbow": ["Type: R", "Range: F", "Damage: 1d4", "Properties: 2H"],
            "Shortsword": ["Type: M", "Range: C", "Damage: 1d6", "Properties: None"],
            "Spear": ["Type: M/R", "Range: C/N", "Damage: 1d6", "Properties: Thrown"],
            "Staff": ["Type: M", "Range: C", "Damage: 1d4", "Properties: 2H"],
            "Warhammer": ["Type: M", "Range: C", "Damage: 1d10", "Properties: 2H"],
            }

Arrows = {"Arrows": ["2d6"], "Crossbow bolts": ["2d6"]}

Weapon_Features = ["Trails sparkles.",
                   "Starmetal.",
                   "Rusted and chipped.",
                   f"Prominent inset gem in the shape of a {random.choice(animals)}.",
                   "Drips green ichor.",
                   "Moon motif and silvered.",
                   "Galaxies swirl on surface.",
                   "Ironwood.",
                   "Rune-scribed.",
                   "Faint, ghostly aura.",
                   "Inlaid with gold.",
                   "Trails incense.",
                   "Studded with gemstones.",
                   "Sparks dance on the surface.",
                   f"Shaped like an {random.choice(animals)}.",
                   "Carved from granite.",
                   "Dragonbone hardware.",
                   "Whispers in a language.",
                   "Drops ocean water.",
                   "Turns blood to rose petals."]

Weapon_benefits = ["Cut or smash through any material.",
                   "Once per day, ignites for 5 rounds, deals 1d4 extra damage.",
                   "DC15 CHA check to command a wild animal within far distance.",
                   "Behead the enemy on a critical hit.",
                   "When you hit a creature, learn its True Name.",
                   "Shoot a bolt of energy near with DEX, 1d6 damage.",
                   "Once per day, deflect a melee attack that would hit you.",
                   "Regain 1d6 hit points when you slay a creature.",
                   "You have advantage on initiative rolls.",
                   "Has thrown property, near distance, returns to you.",
                   f"Double damage to {random.choice(foes)}.",
                   "Re-roll natural 1s once each when attacking with this weapon."]

Weapon_curses = [f"You can't see {random.choice(unseen_foes)}.",
                 "You are compelled to swallow all gemstones at first sight.",
                 "Burn a straw doll daily or weapon temporarily loses magic.",
                 "Any light source you hold immediately extinguishes.",
                 "You must loudly praise a god whenever you see its symbol.",
                 "Venomous creatures always target you with attacks.",
                 "You turn into a rat every day at midnight.",
                 "Your checks to swim are always extreme (DC 18).",
                 "You are burned by the touch of gold.",
                 "Bathe weapon in blood daily or it temporarily loses its magic.",
                 "You cannot wear armor while wielding this weapon.",
                 "Weapon can possess you by winning contested CHA +2"]


def magical_weapon(qualities, personality, name, item_name):
    bonus = calculate_weapon_bonus()
    feature = random.choice(Weapon_Features)
    qualities = choosing_qualities(qualities, Weapon_curses, Weapon_benefits)
    virtue = choosing_personalities(personality)
    category, details = base_weapon(item_name)
    magic_weapon = {'Magical Weapon': name, 'Category': category, 'Details': details, "Bonus": '+ ' + str(bonus),
                    "Features": feature, "Qualities": qualities, "Personality": virtue}
    return magic_weapon


def base_weapon(item_name):
    weapons = list(Weapons)
    if item_name in weapons:
        return item_name, Weapons[item_name]
    return item_name, Arrows[item_name]


def calculate_weapon_bonus():
    bonus = sum(Character.roll_dice(6, 2))
    if bonus <= 5:
        bonus = 0
    elif bonus <= 8:
        bonus = 1
    elif bonus <= 11:
        bonus = 2
    else:
        bonus = 3

    return bonus
