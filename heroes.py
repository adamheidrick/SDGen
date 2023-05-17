from character import Character
from background import Titles, Deities
from weapons import Weapons
from armor import Armor
from spells import Priest_Spells
import random


class Fighter(Character):
    def __init__(self):
        self.hero_class = "Fighter"
        super().__init__()
        self.fighter_specs()
        self.set_title()
        self.random_weapon()
        self.set_armor()
        self.weapon_mastery()
        self.grit()
        self.talent_roll()

    def __repr__(self):
        return "This is the Fighter Class Object."

    def set_title(self):
        title = Titles[self.hero_class][list(self.alignment)[0]]
        print("Generating Title.")
        print(f"\t{title}")
        self.title = title

    def fighter_specs(self):
        print("Generating Fighter Class Attributes.")
        self.fighter_hp()
        self.fighter_ac()
        self.fighter_bonus_carry()

    def fighter_hp(self):
        print("Rolling for Fighter HP 1d8.")
        result = self.roll_dice(8, 1)
        total = sum(result)
        print(f"\tResult of Roll: {result} for a Total of {total}.")
        self.set_hp(total)

    def fighter_ac(self):
        ac = 11 + self.get_dex_mod()
        print(f"\tSetting AC 11 + DEX Modifier: {self.get_dex_mod()} = {ac}.")
        self.set_ac(ac)

    def fighter_bonus_carry(self):
        print("Checking Fighter Hauler Perk.")
        con_mod = self.get_con_mod()
        if con_mod > 0:
            print(f"\tCon Modifier: {con_mod} > 0")
            self.set_notes({"Hauler": f"Gear Slot increased by {con_mod}"})
            self.set_gear_slot(con_mod)
        else:
            print(f"\tCon Modifier: {con_mod} < 0. Hauler perk not applied.")

    def random_weapon(self):
        print("Choosing Random Weapon.")
        weapon = random.choice(list(Weapons))
        print(f"\t{weapon} chosen.")
        self.weapon = weapon
        note = {weapon: Weapons[weapon]}
        self.set_weapon_notes(note)

    def weapon_mastery(self):
        self.weapon_notes[self.weapon].append("Weapon Mastery: +1 Attack and Damage + Half your level rounding down.")
        # Just a descriptor to notes regarding the random weapon chosen of a +1 attack

    def weapon_mastery_talent(self):
        print("\tTalent: Weapon Mastery Chosen: Weapon Mastery with One Additional Weapon.")
        self.set_notes({"Weapon Mastery Talent": "See Weapon Notes. Talent Applied."})
        self.set_weapon_notes({"Weapon Mastery Talent": "+1 Attack and Damage + Half your level rounding down. Applied"
                                                        "to any Weapon you choose that does not already have weapon"
                                                        "mastery."})

    def set_armor(self, armor=None):
        if armor is None:
            print(f"Equipping Leather Armor.")
            note = {"Armor Properties": Armor["Leather"]["Properties"]}
            self.set_armor_notes(note)
            self.armor = Armor["Leather"]
        else:
            print(f"Equipping {armor}.")
            self.armor = Armor[armor]

    def grit(self):
        print("Flipping a Coin for Grit.")
        choices = ["Strength", "Dexterity"]
        chosen = random.choice(choices)
        print(f"\tGrit Result: {chosen} chosen.")
        note = {chosen: f"True Grit: Advantage on {chosen} checks."}
        self.set_notes(note)

    def talent_roll(self):
        print("Rolling 2d6 for Talent.")
        roll = self.roll_dice(6, 2)
        total = sum(roll)
        print(f"\tRoll Result: {roll} = {total}")
        self.choose_talent(roll)

    def choose_talent(self, choice):
        print(f"Choosing Talent Based on {choice} roll.")
        talents = [self.weapon_mastery_talent, self.extra_weapon_dmg, self.stat_boost,
                   self.armor_boost, self.stat_distribute]
        choice = random.choice(talents)
        choice()
        talents.remove(choice)

    def extra_weapon_dmg(self):
        print("\tTalent +1 Melee and Ranged Attacks Being Applied.")
        self.set_notes({"Fighter Talent": "+1 Attack to Melee and Ranged."})
        print("\tAdding Weapon Boost to Weapon Notes.")
        self.weapon_notes[self.weapon].append("Fighter Talent +1 to attack")

    def stat_boost(self):
        print("\tTalent Strength, Dexterity, or Constitution Boost Being Applied")
        print("\tRandomly Choosing Stat Boost.")
        random_stat = ["Strength", "Dexterity", "Constitution"]
        ran_choice = random.randint(0, 2)
        print(f"\t{random_stat[ran_choice]} Chosen.")
        print(f"\tAdjusting {random_stat[ran_choice]} by + 2.")
        print("\tChecking if Modifier Needs Adjusting.")
        choice = None
        match ran_choice:
            case 0:
                choice = "Strength"
                self.set_str(2)
                print(f"\tStrength now = {self.str}")
                mod = self.modifier_check([self.str], ["Str"])
                if mod[0] > self.str_mod:
                    print("\tAdjusting Strength Modifier.")
                    self.set_str_mod(mod[0])
            case 1:
                choice = "Dexterity"
                self.set_dex(2)
                print(f"\tDexterity now = {self.dex}")
                mod = self.modifier_check([self.dex], ["Dex"])
                if mod[0] > self.dex_mod:
                    print("\tAdjusting Dexterity Modifier.")
                    self.set_dex_mod(mod[0])
            case 2:
                choice = "Constitution"
                self.set_con(2)
                print(f"\tConstitution now = {self.con}")
                mod = self.modifier_check([self.con], ["Con"])
                if mod[0] > self.con_mod:
                    print("\tAdjusting Constitution Modifier.")
                    self.set_con_mod(mod[0])
        self.set_notes({"Fighter Talent": f"+2 Added to {choice} and Modifier Adjusted."})

    def armor_boost(self):
        print("\tTalent: Armor Choice +1 to AC Boost Being Applied.")
        dex_mod = self.dex_mod
        ac = self.ac
        gear_slots = self.gear_slots

        print("\tRolling for Armor.")
        choice = random.choice(list(Armor))
        self.set_armor(choice)

        note = {"Fighter Talent Armor Properties": Armor[choice]["Properties"] + "+1 to AC is already set."}
        self.set_armor_notes(note)

        print(f"\tAdjusting AC and Gear Slots Based on {choice}.")
        match choice:
            case "Leather":
                print(f"\tLeather armor was already equipped. "
                      f"\n\tAC of {ac} and Gear Slot of {gear_slots} remains the same.")
            case "Chainmail":
                print(f"\tAdjusting AC {ac} to {ac + 2}")
                self.ac += 2
                print(f"\tAdjusting Gear Slots {gear_slots} to {gear_slots - 1} ")
                self.set_gear_slot(gear_slots - 1)

            case "Plate Mail":
                adjusted_ac = Armor["Plate Mail"]["AC"]
                print(f"\tAdjusting AC {ac} to {adjusted_ac}")
                self.ac += 3
                print(f"\tAdjusting Gear Slots {gear_slots} to {gear_slots - 2} ")
                self.set_gear_slot(gear_slots - 2)

            case "Shield":
                print(f"\tAdjusting AC {ac} to 2.")
                self.ac = 2
                print(f"\tGear Slot of  {gear_slots} does not need to be adjusted.")

            case "Mithral CM":
                print(f"\tAdjusting AC {ac} to {ac + 2}")
                self.ac += 2
                print(f"\tAdjusting Gear Slots {gear_slots} to {gear_slots - 1} ")
                self.set_gear_slot(gear_slots - 1)

        print("\tApplying Talent +1 to AC bonus")
        self.ac += 1
        print(f"\tFinal AC = {self.ac}")
        # TODO: Can there be Mithral PM? YES! IMPLEMENT IT.


class Priest(Character):
    def __init__(self):
        self.hero_class = "Priest"
        self.spells = {}
        # TODO: Priest must choose one god.
        super().__init__()
        self.priest_specs()
        self.set_title()
        self.random_weapon()
        self.set_armor()
        self.set_spells()
        self.check_religion()

    def __repr__(self):
        return "This is the Priest Class Object."

    def priest_specs(self):
        print("Generating Priest Class Attributes.")
        self.priest_hp()
        self.priest_ac()

    def priest_hp(self):
        print("Rolling for Priest HP 1d6.")
        result = self.roll_dice(6, 1)
        total = sum(result)
        print(f"\tResult of Roll: {result} for a Total of {total}.")
        self.set_hp(total)

    def priest_ac(self):
        ac = 11 + self.get_dex_mod()
        print(f"\tSetting AC 11 + DEX Modifier: {self.get_dex_mod()} = {ac}.")
        self.set_ac(ac)

    def set_title(self):
        title = Titles[self.hero_class][list(self.alignment)[0]]
        print("Generating Title.")
        print(f"\t{title}")
        self.title = title

    def random_weapon(self):
        print("Choosing Random Weapon.")
        priest_weapons = ["Club", "Crossbow", "Dagger", "Mace", "Longsword", "Staff", "Warhammer"]
        random_weapon = random.choice(priest_weapons)
        print(f"\t{random_weapon} chosen.")
        self.weapon = random_weapon
        note = {random_weapon: Weapons[random_weapon]}
        self.set_weapon_notes(note)

    def set_armor(self, armor=None):
        if armor is None:
            print(f"Equipping Leather Armor.")
            note = {"Armor Properties": Armor["Leather"]["Properties"]}
            self.set_armor_notes(note)
            self.armor = Armor["Leather"]
        else:
            print(f"Equipping {armor}.")
            self.armor = Armor[armor]

    def set_spells(self):
        default = "Turn Undead"
        print(f"Priest is Learning two Random Spells and {default}.")
        spells = [item for item in Priest_Spells.keys() if item != default]
        choices = random.sample(set(spells), 2)
        choices.append(default)
        for spell in choices:
            self.spells.update({spell: Priest_Spells[spell]})
            print(f"\tPriest learned {spell}")
            print(f"\t\tAdding {spell} to Notes")

    def check_religion(self):
        print("Checking Religion.")
        if self.deity is None:
            self.deity = random.choice(list(Deities[0].items()))

        deity = list(self.deity)[0]
        print(f"\tPriest found {deity}.")
        print(f"\tAdding {deity} Symbol to Gear.")
        self.gear.update({deity + "symbol": [{"Quantity": 1}, {"Gear Slot": 0}]})

    def roll_priest_talents(self):
        pass

    def advantage_on_spell(self):
        pass

    def attack_bonus(self):
        pass

    def cast_bonus(self):
        pass

    def str_wis_boost(self):
        pass


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
    print(f"Rolling for Random Class = {num}")
    print("Generating Random Class.")
    new_hero = None
    num = 1  # REMOVE THIS AS YOU DEVELOP

    match num:
        case 0:
            print("\tFighter Class Chosen")
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
