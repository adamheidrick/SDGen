import random


def roll_dice(sided, times):
    results = [random.randint(1, sided) for num in range(times)]
    return results, sum(results)


def calculate_modifiers(num):
    pass


def get_ancestry(index):
    ancestry = ['DWARF', 'GOBLIN', 'ELF', 'HALF-ORC', 'HALFLING', 'HUMAN']
    return ancestry[random.randint(0, 5)]


def main():
    print(roll_dice(12, 3))


if __name__ == "__main__":
    main()
