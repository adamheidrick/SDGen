from character import Character
from talents import *
from weapons import Weapons
import random
# TODO: Talents may impact stats, if so the modifiers will need to be recalculated.


class Fighter(Character):
    def __init__(self):
        self.hero_class = "Fighter"
        self.armor = "Leather Armor"
        self.weapons = ["All"]
        self.weapon = ""
        self.talents = []
        super().__init__()
        self.fighter_specs()
        self.random_weapon()
        self.weapon_mastery()
        self.grit()
        self.talent_roll()

    def __repr__(self):
        return "This is the Fighter Class Object."

    def fighter_specs(self):
        self.fighter_hp()
        self.fighter_ac()
        self.fighter_bonus_carry()

    def fighter_hp(self):
        print("Rolling for Fighter HP 1d8.")
        self.set_hp(sum(self.roll_dice(8, 1)))

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

    def grit(self):
        print("Rolling for Grit.")
        choices = ["Strength", "Dexterity"]
        chosen = random.choice(choices)
        print(f"{chosen} chosen.")
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
        self.set_notes({"Fighter Talent": "+1 to melee and ranged attacks."})
        self.set_weapon_notes(self.weapon_notes[self.weapon].append("Fighter Talent +1 to attack"))

    def stat_boost(self):
        print("Randomly Choosing Stat Boost.")
        random_stat = ["Strength", "Dexterity", "Constitution"]
        ran_choice = random.randint(0, 2)
        print(f"{random_stat[ran_choice]} Chosen.")
        print(f"Adjusting {random_stat[ran_choice]} by + 2.")
        print("Checking if Modifier Needs Adjusting.")
        match ran_choice:
            case 0:
                self.set_str(2)
                print(f"Strength now = {self.str}")
                mod = self.modifier_check([self.str], ["Str"])
                if mod[0] > self.str_mod:
                    print("Adjusting Strength Modifier.")
                    self.set_str_mod(mod[0])
            case 1:
                self.set_dex(2)
                print(f"Dexterity now = {self.dex}")
                mod = self.modifier_check([self.dex], ["Dex"])
                if mod[0] > self.dex_mod:
                    print("Adjusting Dexterity Modifier.")
                    self.set_dex_mod(mod[0])
            case 2:
                self.set_con(2)
                print(f"Constitution now = {self.con}")
                mod = self.modifier_check([self.con], ["Con"])
                if mod[0] > self.con_mod:
                    print("Adjusting Constitution Modifier.")
                    self.set_con_mod(mod[0])


    def additional_talent(self):
        # how to keep track of talents already? Enumerate with index.
        # add additional talent
        pass

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
