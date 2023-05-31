import random
from character import Character

Armor = {"Leather": {"type": "leather", "gear_slot": 1, "AC": 11,
                     "Properties": "Just a bit of leather."},
         "Chainmail": {"type": "chainmail", "gear_slot": 2, "AC": 13,
                       "Properties": "Disadvantage on Stealth and Swim."},
         "Plate Mail": {"type": "plate mail", "gear_slot:": 3, "AC": 15,
                        "Properties": "Disadvantage on Stealth. No Swim."},
         "Shield": {"type": "shield", "gear_slot": 1, "AC": 2,
                    "Properties": "Occupies one Hand."},
         "Mithral CM": {"type": "mithral chainmail", "gear_slot": -1, "AC": 13,
                        "Properties": "No Penalty on Stealth and Swim."},
         "Mithral PM": {"type": "mithral plate mail", "gear_slot": -1, "AC": 15,
                        "Properties": "No Penalty on Stealth and Swim."}}

magical_armor_description = ["Demonic, horned face", "Oak leaf motif", "Studded with shark teeth", "Dragon Scales",
                             "Bone Spikes", "Metal Spikes", "Faint, arcane runes", "Turtle shell plating",
                             "Made of scorpion chitin", "Gilded metal/gold thread", "Scorched, smells burned",
                             "Pearl-white fish scales", "Oozes blood", "Festooned with fungi", "Distant sound of ocean",
                             "Set with crystals", "Draped in holy symbols", "Exudes tree sap",
                             "Blurry, indistinct edges", "Large, golden cat eye", "Covered in frost"]

magical_armor_benefits = ["Once per day, deflect a ranged attack that would hit you.",
                          "Checks to stabilise you are easy DC(9).",
                          "You cannot be knocked over while you are conscious.",
                          "Undetected creatures do not have advantage to attack you.",
                          "You know Diabolic and are immune to fire, lava, and magma.",
                          "You are immune to the curses of one item you choose.",
                          "Once per day, gain advantage on all attacks for 3 rounds.",
                          "You have a +4 bonus to your death timers.",
                          "Gain immunity to poison after suffering its effects once.",
                          "You know Celestial and can fly for 3 rounds once per day.",
                          "Treat critical hits against you as normal hits.",
                          "Ignore any damage dealt to you of 3 points or below."]

magical_armor_curse = ["You take 2d10 damage if you remove this armor.",
                       "Your party cannot add CHA bonuses to reaction checks.",
                       "Mounts fear you and will not allow you to ride them.",
                       "DC 15 WIS first round of combat or attack nearest creature.",
                       "You take double damage from blunt/bludgeoning weapons.",
                       "Armor uses 5 gear slots and is extremely loud and clunky.",
                       "Ranged attacks against you have advantage.",
                       "Treat a natural 1 attack roll against you as a critical hit.",
                       "Benefit spells that target you are hard to cast (DC 15).",
                       "You have disadvantage on Dexterity Checks.",
                       "There's a secret 1 in 6 chance each NPC ally will betray you.",
                       "You take double damage from silvered weapons."]


def magical_armor(qualities, personality, name):
    armor = {}
    bonus = calculate_bonus()
    armor_type = random.choice(list(Armor))

    update_armor(armor, armor_type, bonus)
    update_armor_qualities(armor, name, qualities)

    return armor


def update_armor_qualities(armor, name, qualities):
    quality = choosing_qualities(qualities, armor)
    armor.update({'Armor Feature': random.choice(magical_armor_description)})
    armor.update({'Qualities': quality})
    armor.update({'Magical Item Name': name})


def update_armor(armor, armor_type, bonus):
    armor.update({armor_type: Armor[armor_type]})
    armor[armor_type]["AC"] = bonus


def calculate_bonus():
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


def calculate_quality_roll():
    bonus = sum(Character.roll_dice(6, 2))
    if bonus <= 3:
        bonus = 0
    elif bonus <= 7:
        bonus = 1
    elif bonus <= 11:
        bonus = 2
    else:
        bonus = 3

    return bonus


def choosing_qualities(qualities, armor):
    quality_1, quality_2 = qualities
    curse = random.choice(magical_armor_curse)
    benefit = random.choice(magical_armor_benefits)

    if check_gear_slot_curse(curse):
        armor['gear_slot'] = 5
        armor['Properties'] += ' Armor is Extremely Loud and Clunky (Cursed).'

    if quality_1 is None and quality_2 == "curse":
        return curse

    if quality_1 == "benefit" and quality_2 == 'curse':
        qualities = [benefit, curse]
        return qualities

    if quality_1 == "benefit" and quality_2 is None:
        return benefit

    return random.sample(magical_armor_benefits, 2)


def check_gear_slot_curse(curse):
    if curse == "Armor uses 5 gear slots and is extremely loud and clunky.":
        return True
