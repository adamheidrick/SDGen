from character import Character
import random


class Fighter(Character):
    def __init__(self):
        self.hero_class = "Fighter"
        self.armor = "Leather Armor"
        self.weapon = ""
        super().__init__()
        self.get_weapon()
        self.set_hp(self.roll_dice(8, 1))
        self.set_ac(11 + self.get_dex_mod())
        con_mod = self.get_con_mod()
        if con_mod > 0:
            self.set_gear_slot(con_mod)

    def __repr__(self):
        return "This is the Fighter Class Object."

    def get_weapon(self):
        self.weapon = "RANDOM WEAPON"


class Priest(Character):
    def __init__(self):
        self.hero_class = "Priest"
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
    new_hero = None

    match num:
        case 0:
            new_hero = Fighter()
        case 1:
            new_hero = Priest()
        case 2:
            new_hero = Thief()
        case 3:
            new_hero = Wizard()

    return new_hero
