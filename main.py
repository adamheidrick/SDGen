import random
from heroes import Fighter, Priest, Thief, Wizard


def roll_dice(sided, times):
    return sum([random.randint(1, sided) for num in range(times)])


def calculate_modifiers(num):
    pass


def roll_stats(hero):
    rolls = [roll_dice(6, 3) for num in range(7)]
    print(rolls)


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


def main():
    hero = random_class()
    roll_stats(hero)


if __name__ == "__main__":
    main()
