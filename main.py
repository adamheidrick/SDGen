from heroes import random_class
from ancestry import set_ancestry


def main():
    hero = random_class()
    set_ancestry(hero)
    print("Packing Backpack.")
    for key, value in hero.gear.items():
        if key == "Backpack":
            continue
        print(f"\tPacking {key}, {value[0]}")
    print(hero.__dict__)


if __name__ == "__main__":
        main()
