from heroes import random_class
from ancestry import set_ancestry


def main():
    # Testing Mac setup for the road.
    hero = random_class()
    set_ancestry(hero)
    hero.set_name(hero.ancestry)
    print("Packing Backpack.")
    for key, value in hero.gear.items():
        if key == "Backpack":
            continue
        print(f"\tPacking {key}, {value[0]}")
    print("... Generating Name ... ")
    print(f"From the depths emerges {hero.name}")
    print(hero.__dict__)


if __name__ == "__main__":
    main()
