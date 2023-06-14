
def parse_hero(hero):
    hero_dict = hero.__dict__
    hero_attributes = list(hero.__dict__)
    print(hero_attributes)
    print(f"{'Name:':<15} {hero_dict['name']}")
    print(f"{'Ancestry:':<15} {hero_dict['ancestry']}")
    print(f"{'Class:':<15} {hero_dict['hero_class']}")
    print(f"{'Title:':<15} {hero_dict['title']}")
    print(f"{'Alignment:':<15} {list(hero_dict['alignment'])[0]}")
    print(f"{'Background:':<15} {hero_dict['background']}")
    print(f"{'Deity:':<15} {'Does not believe in God.' if hero_dict['deity'] is None else list(hero_dict['deity'])[0]}")


    print("\n")
    print("Stats")
    print(f"{'Level:':<15} {1}")
    print(f"{'HP & AC:':<15} {hero_dict['hp']} / {hero_dict['ac']}")
    print(f"{'Strength:':<15} {hero_dict['str']} / {hero_dict['str_mod']}")
    print(f"{'Intelligence:':<15} {hero_dict['int']} / {hero_dict['int_mod']}")
    print(f"{'Dexterity:':<15} {hero_dict['dex']} / {hero_dict['dex_mod']}")
    print(f"{'Wisdom:':<15} {hero_dict['wis']} / {hero_dict['wis_mod']}")
    print(f"{'Constitution:':<15} {hero_dict['con']} / {hero_dict['con_mod']}")
    print(f"{'Charisma:':<15} {hero_dict['cha']} / {hero_dict['cha_mod']}")

    print("\n")
    if hero_dict['hero_class'] == 'Wizard' or hero_dict['hero_class'] == 'Priest':
        spells = list(hero_dict['spells'])
        print("Spells")
        for index, spell in enumerate(spells):
            print(f"{'spell ' + str(index +1) +':':<15}{spell}")


    print("Talents")
    print(''.join("{}: {}".format(k, v) for k, v in hero_dict['learned_talents'].items()))

    print("\n")
    weapon = hero_dict['weapon']
    print("Weapons")
    print(f"{hero_dict['weapon']:<15}{', '.join(hero_dict['weapon_notes'][weapon])}")

    print("\n")
    print('Armor')
    if hero_dict['armor'] is not None:
        print(hero_dict['armor']['type'].capitalize())

    else:
        print("Glass Cannon's Can't Wear Armor.")

    print("\n")
    print("Additional Notes")
    print('\n'.join("{}: {}".format(k, v) for k, v in hero_dict['notes'].items()))



