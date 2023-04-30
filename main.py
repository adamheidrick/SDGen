import random
from heroes import random_class
from ancestry import set_ancestry


def calculate_modifiers(rolls):
    # TODO: Is there an easier formula for calculating the mod?
    modifiers = []
    mod_dict = {3: -4, 5: -3, 7: -2, 9: -1, 11: 0, 13: 1, 15: 2, 17: 3}
    for num in rolls:
        for check in range(3, 18, 2):
            if num <= check:
                modifiers.append(mod_dict[check])
                break
            elif num >= 18:
                modifiers.append(4)
                break

    return modifiers


def main():
    hero = random_class()
    stat_rolls = hero.roll_stats()
    modifiers = calculate_modifiers(stat_rolls)
    stats = list(zip(stat_rolls, modifiers))
    hero.apply_stats(stats)
    set_ancestry(hero)
    print(hero.__dict__)


if __name__ == "__main__":
    main()
