import random
from heroes import random_class
from ancestry import set_ancestry




def main():
    hero = random_class()
    set_ancestry(hero)
    print(hero.__dict__)


if __name__ == "__main__":
    main()
