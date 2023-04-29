from character import Character
import random


class Fighter(Character):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "This is the Fighter Class Object."


class Priest(Character):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "This is the Priest Class Object."


class Thief(Character):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "This is the Thief Class Object."


class Wizard(Character):
    def __init__(self):
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
