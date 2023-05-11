from character import Character
from talents import *
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
        self.grit()
        self.roll_talents()

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

    def weapon_mastery(self):
        pass

    def grit(self):
        pass

    def talent_roll(self):
        # Roll for a talent. Talent names in list so if additional talent, then same talent is not chosen twice.
        pass

    def extra_weapon_dmg(self):
        # +1 to melee and ranged attacks.
        pass

    def stat_boost(self):
        # +2 to strength, dex, or constitution (Random).
        pass

    def choose_armor(self):
        # Choose one kind of armor, Add +1 AC from that armor.
        pass

    def additional_talent(self):
        # how to keep track of talents already? Enumerate with index.
        # add additional talent
        pass

    def stat_distribute(self):
        # +2 distribute to stats (find min)
        pass

    def roll_talents(self):
        # TODO: Write the Talent mechanic here. Use the above methods to set stats.
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
