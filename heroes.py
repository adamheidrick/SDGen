from character import Character
from talents import *
from weapons import Weapons
from armor import Armor
import random
# TODO: Talents may impact stats, if so the modifiers will need to be recalculated.


class Fighter(Character):
    def __init__(self):
        self.hero_class = "Fighter"
        self.armor = ""
        self.weapons = ["All"]
        self.weapon = ""
        self.talents = []
        super().__init__()
        self.fighter_specs()
        self.random_weapon()
        self.set_armor()
        self.weapon_mastery()
        self.grit()
        self.talent_roll()
        self.armor_boost()
        # if human extra talent roll.

    def __repr__(self):
        return "This is the Fighter Class Object."

    def fighter_specs(self):
        self.fighter_hp()
        self.fighter_ac()
        self.fighter_bonus_carry()

    def fighter_hp(self):
        print("Rolling for Fighter HP 1d8.")
        result = self.roll_dice(8, 1)
        total = sum(result)
        print(f"Result of Roll: {result} for a Total of {total}.")
        self.set_hp(total)

    def fighter_ac(self):
        ac = 11 + self.get_dex_mod()
        print(f"Setting AC 11 + DEX Modifier: {self.get_dex_mod()} = {ac}.")
        self.set_ac(ac)

    def fighter_bonus_carry(self):
        print("Checking Fighter Hauler Perk.")
        con_mod = self.get_con_mod()
        if con_mod > 0:
            print(f"Con Modifier: {con_mod} > 0")
            self.set_notes({"Hauler": f"Gear Slot increased by {con_mod}"})
            self.set_gear_slot(con_mod)
        else:
            print(f"Con Modifier: {con_mod} < 0. Hauler perk not applied.")

    def random_weapon(self):
        print("Choosing Random Weapon.")
        weapon = random.choice(list(Weapons))
        print(f"{weapon} chosen.")
        self.weapon = weapon
        note = {weapon: Weapons[weapon]}
        self.set_weapon_notes(note)

    def weapon_mastery(self):
        self.weapon_notes[self.weapon].append("Weapon Mastery: +1 Attack and Damage + Half your level rounding down.")
        # Just a descriptor to notes regarding the random weapon chosen of a +1 attack

    def weapon_mastery_talent(self):
        self.set_weapon_notes({"Weapon Mastery Talent": "+1 Attack and Damage + Half your level rounding down. Applied"
                                                        "to any Weapon you choose that does not already have weapon"
                                                        "mastery."})

    def set_armor(self, armor=None):
        if armor is None:
            print(f"Equipping Leather Armor.")
            self.armor = Armor["Leather"]
        else:
            print(f"Equipping {armor}.")
            self.armor = Armor[armor]

    def grit(self):
        print("Flipping a Coin for Grit.")
        choices = ["Strength", "Dexterity"]
        chosen = random.choice(choices)
        print(f"Grit Result: {chosen} chosen.")
        note = {chosen: f"True Grit: Advantage on {chosen} checks."}
        self.set_notes(note)

    def talent_roll(self):
        print("Rolling 2d6 for Talent.")
        roll = self.roll_dice(6, 2)
        total = sum(roll)
        print(f"Roll Result: {roll} = {total}")
        self.choose_talent(roll)

    def choose_talent(self, choice):
        print(f"Choosing Talent Based on {choice} roll.")
        talents = fighterTalents

    def extra_weapon_dmg(self):
        self.set_notes({"Fighter Talent": "+1 Attack to Melee and Ranged."})
        self.set_weapon_notes(self.weapon_notes[self.weapon].append("Fighter Talent +1 to attack"))

    def stat_boost(self):
        print("Randomly Choosing Stat Boost.")
        random_stat = ["Strength", "Dexterity", "Constitution"]
        ran_choice = random.randint(0, 2)
        print(f"{random_stat[ran_choice]} Chosen.")
        print(f"Adjusting {random_stat[ran_choice]} by + 2.")
        print("Checking if Modifier Needs Adjusting.")
        choice = None
        match ran_choice:
            case 0:
                choice = "Strength"
                self.set_str(2)
                print(f"Strength now = {self.str}")
                mod = self.modifier_check([self.str], ["Str"])
                if mod[0] > self.str_mod:
                    print("Adjusting Strength Modifier.")
                    self.set_str_mod(mod[0])
            case 1:
                choice = "Dexterity"
                self.set_dex(2)
                print(f"Dexterity now = {self.dex}")
                mod = self.modifier_check([self.dex], ["Dex"])
                if mod[0] > self.dex_mod:
                    print("Adjusting Dexterity Modifier.")
                    self.set_dex_mod(mod[0])
            case 2:
                choice = "Constitution"
                self.set_con(2)
                print(f"Constitution now = {self.con}")
                mod = self.modifier_check([self.con], ["Con"])
                if mod[0] > self.con_mod:
                    print("Adjusting Constitution Modifier.")
                    self.set_con_mod(mod[0])
        self.set_notes({"Fighter Talent": f"+2 Added to {choice} and Modifier Adjusted."})

    def armor_boost(self):
        dex_mod = self.dex_mod
        ac = self.ac
        gear_slots = self.gear_slots

        print("Rolling for Armor.")
        choice = random.choice(list(Armor))
        self.set_armor(choice)

        note = {"Fighter Talent Armor Properties": Armor[choice]["Properties"] + "+1 to AC is already set."}
        self.set_armor_notes(note)

        print(f"Adjusting AC and Gear Slots Based on {choice}.")
        match choice:
            case "Leather":
                print(f"Leather armor was already equipped. "
                      f"AC of {ac} and Gear Slot of {gear_slots} remains the same.")
            case "Chainmail":
                print(f"Adjusting AC {ac} to {ac + 2}")
                self.set_ac(ac + 2)
                print(f"Adjusting Gear Slots {gear_slots} to {gear_slots - 1} ")
                self.set_gear_slot(gear_slots - 1)

            case "Plate Mail":
                adjusted_ac = Armor["Plate Mail"]["AC"]
                print(f"Adjusting AC {ac} to {adjusted_ac}")
                self.set_ac(ac + 3)
                print(f"Adjusting Gear Slots {gear_slots} to {gear_slots - 2} ")
                self.set_gear_slot(gear_slots - 2)

            case "Shield":
                print(f"Adjusting AC {ac} to {ac + 2}")
                self.set_ac(ac + 2)
                print(f"Gear Slot of  {gear_slots} does not need to be adjusted.")

            case "Mithral CM":
                print(f"Adjusting AC {ac} to {ac + 2}")
                self.set_ac(ac + 2)
                print(f"Adjusting Gear Slots {gear_slots} to {gear_slots - 1} ")
                self.set_gear_slot(gear_slots - 1)

        print("Applying Talent +1 to AC bonus")
        self.ac += 1
        print(f"Final AC = {self.ac}")
        # TODO: Can there be Mithral PM?


    def stat_distribute(self):
        # +2 distribute to stats (find min)
        pass


class Priest(Character):
    def __init__(self):
        self.hero_class = "Priest"
        # TODO: Priest must choose one god.
        super().__init__()

    def __repr__(self):
        return "This is the Priest Class Object."


class Thief(Character):
    def __init__(self):
        self.hero_class = "Thief"
        super().__init__()

    def __repr__(self):
        return "This is the Thief Class Object."


class Wizard(Character):
    def __init__(self):
        self.hero_class = "Wizard"
        super().__init__()

    def __repr__(self):
        return "This is the Wizard Class Object."


def random_class():
    num = random.randint(0, 3)
    print("Creating Random Class.")
    print(f"Random Class Number = {num}")
    new_hero = None
    num = 0  # REMOVE THIS AS YOU DEVELOP

    match num:
        case 0:
            print("Fighter Class Chosen")
            new_hero = Fighter()
        case 1:
            print("Priest Class Chosen")
            new_hero = Priest()
        case 2:
            print("Thief Class Chosen")
            new_hero = Thief()
        case 3:
            print("Wizard Class Chosen")
            new_hero = Wizard()

    return new_hero
