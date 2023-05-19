import random
ANCESTRY = ["dwarf", "goblin", "elf", "half_orc", "halfling", "human"]
COMMON_LANGUAGES = ["Dwarvish", "Elvish", "Giant", "Goblin", "Merran", "Orcish", "Reptilian", "Sylvan", "Thanian"]
PRIEST_BONUS = ["Celestial", "Diabolic", "Primordial"]


def dwarf(hero: object):
    hero.set_ancestry("Dwarf")
    hero.set_notes({"Dwarf": "Brave, stalwart fok as sturdy as the stone kingdoms they carve inside mountains"})
    hero.set_notes({"Languages": "You know the Common and Dwarvish Languages"})
    hero.set_notes({"Stout": "Start with +2 HP Roll hit points per level with advantage"})
    print("\tApplying Dwarf Stout Modifier +2 to HP.")
    hero.set_hp(2)


def goblin(hero: object):
    hero.set_ancestry("Goblin")
    hero.set_notes({"Goblin": "Green, clever beings who thrive in dark, cramped places. As fierce as they are tiny."})
    hero.set_notes({"Languages": "You know the Common and Goblin languages."})
    hero.set_notes({"Keen Senses": "You can't be surprised"})


def elf(hero: object):
    # TODO: Dont forge the Farsight or Condition below. +1 or Spellcasting checks.
    hero.set_ancestry("Elf")
    hero.set_notes({"Elf: ": "Ethereal, graceful people whoever knowledge and beauty. Elves see far "
                                 "and live long."})
    hero.set_notes({"Languages": "You know the Common, Elvish, and Sylvan languages."})
    hero.set_notes({"Farsight: ": "You get a +1 bonus to attack rolls with ranged weapons or a +1 bonus to "
                                  "spell-casting checks."})


def half_orc(hero: object):
    hero.set_ancestry("Half Orc")
    hero.set_notes({"Half Orc": "Towering, tusked warriors who are as daring as humans and as relentless as orcs."})
    hero.set_notes({"Languages": "You know the Common and Orcish languages."})
    hero.set_notes({"Mighty:": "You have a +1 bonus to attack and damage rolls with melee weapons."})
    weapon = list(hero.weapon_notes)[0]
    hero.weapon_notes[weapon].append(" Half-Orc Boon Mighty: +1 attack and damage.")


def halfling(hero: object):
    hero.set_ancestry("Halfling")
    hero.set_notes({"Halfling: ": "Small, cheerful country folk with mischievous streaks. They enjoy "
                                  "life’s simple pleasures.."})
    hero.set_notes({"Languages": "You know the Common language."})
    hero.set_notes({"Stealthy: ": "Once per day, you can become invisible for 3 rounds."})


def human(hero: object):
    hero.set_ancestry("Human")
    additional_language = random.choice(COMMON_LANGUAGES)
    print(f"Additional Language Chosen as a Human Perk = {additional_language}.")
    hero.set_notes({"Human: ": "Bold, adaptable, and diverse people who learn quickly and accomplish mighty deeds."})
    hero.set_notes({"Languages": f"You know the Common language and {additional_language} languages."})
    hero.set_notes({"Ambitious: ": "You gain one additional talent roll at 1st level"})
    print("\tRolling for additional talent (Human Perk Ambition!).")
    hero.talent_roll()


def set_ancestry(hero):
    print("Choosing Ancestry.")
    ancestry = random.choice(ANCESTRY)
    print(f"\tAncestry Chosen = {ancestry}")
    set_ancestry_name(hero, ancestry)
    set_ancestry_details(hero, ancestry)


def set_ancestry_name(hero, ancestry):
    hero.set_ancestry(ancestry)


def set_ancestry_details(hero, ancestry):
    functions = [dwarf, goblin, elf, half_orc, halfling, human]
    for index, function in enumerate(functions):
        if ancestry == ANCESTRY[index]:
            function(hero)

    if hero.hero_class == "Priest":
        print("Priest is Learning an Additional Language.")
        add_language = random.choice(PRIEST_BONUS)
        print(f"\t{add_language} language added to notes.")
        hero.notes['Languages'] += f" ( Priest Bonus: {add_language})"
