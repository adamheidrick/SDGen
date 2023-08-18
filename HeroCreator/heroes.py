from character import Character
from background import Titles, Deities
from weapons import Weapons
from armor import Armor
from spells import Priest_Spells, Tier_1_Spells
from magic_item_gen import magical_item
import random
import logging

logger = logging.getLogger(__name__)


class Fighter(Character):
    def __init__(self):
        self.hero_class = "Fighter"
        self.talents = [self.weapon_mastery_talent, self.extra_weapon_dmg, self.stat_boost, self.armor_boost,
                        self.stat_distribute]
        super().__init__()
        self.fighter_specs()
        self.set_title()
        self.random_weapon()
        self.set_armor()
        self.weapon_mastery()
        self.grit()
        self.talent_roll(self.talents)

    def __repr__(self):
        return "This is the Fighter Class Object."

    def set_title(self):
        title = Titles[self.hero_class][list(self.alignment)[0]]
        logger.info("Generating Title.")
        logger.info(f"\t{title}")
        self.title = title

    def fighter_specs(self):
        logger.info("Generating Fighter Class Attributes.")
        self.fighter_hp()
        self.fighter_ac()
        self.fighter_bonus_carry()

    def fighter_hp(self):
        logger.info("Rolling for Fighter HP 1d8.")
        result = self.roll_dice(8, 1)
        total = sum(result)
        logger.info(f"\tResult of Roll: {result} for a Total of {total}.")
        self.set_hp(total)

    def fighter_ac(self):
        ac = 11 + self.get_dex_mod()
        logger.info(f"\tSetting AC 11 + DEX Modifier: {self.get_dex_mod()} = {ac}.")
        self.set_ac(ac)

    def fighter_bonus_carry(self):
        logger.info("Checking Fighter Hauler Perk.")
        con_mod = self.get_con_mod()
        if con_mod > 0:
            logger.info(f"\tCon Modifier: {con_mod} > 0")
            self.set_notes({"Hauler": f"Gear Slot increased by {con_mod}"})
            self.set_gear_slot(con_mod)
        else:
            logger.info(f"\tCon Modifier: {con_mod} < 0. Hauler perk not applied.")

    def random_weapon(self):
        logger.info("Choosing Random Weapon.")
        weapon = random.choice(list(Weapons))
        logger.info(f"\t{weapon} chosen.")
        self.weapon = weapon
        note = {weapon: Weapons[weapon]}
        self.set_weapon_notes(note)

    def weapon_mastery(self):
        self.weapon_notes[self.weapon].append("Weapon Mastery: +1 Attack and Damage + Half your level rounding down.")

    def weapon_mastery_talent(self):
        note = {"Weapon Mastery": "+1 Attack and Damage + Half your level rounding down."}
        logger.info("\tTalent: Weapon Mastery Chosen: Weapon Mastery with One Additional Weapon.")
        self.set_learned_talents(note)
        self.set_weapon_notes(note)

    def set_armor(self, armor=None):
        if armor is None:
            logger.info(f"Equipping Leather Armor.")
            note = {"Armor Properties": Armor["Leather"]["Properties"]}
            self.set_armor_notes(note)
            self.armor = Armor["Leather"]
        else:
            logger.info(f"Equipping {armor}.")
            self.armor = Armor[armor]

    def grit(self):
        logger.info("Flipping a Coin for Grit.")
        choices = ["Strength", "Dexterity"]
        chosen = random.choice(choices)
        logger.info(f"\tGrit Result: {chosen} chosen.")
        note = {chosen: f"True Grit: Advantage on {chosen} checks."}
        self.set_notes(note)

    def extra_weapon_dmg(self):
        note = {"Fighter Talent": "+1 Attack to Melee and Ranged."}
        logger.info("\tTalent +1 Melee and Ranged Attacks Being Applied.")
        self.set_learned_talents(note)
        logger.info("\tAdding Weapon Boost to Weapon Notes.")
        self.weapon_notes[self.weapon].append("Fighter Talent +1 to attack")

    def stat_boost(self):
        logger.info("\tTalent Strength, Dexterity, or Constitution Boost Being Applied")
        logger.info("\tRandomly Choosing Stat Boost.")
        random_stat = ["Strength", "Dexterity", "Constitution"]
        ran_choice = random.randint(0, 2)
        logger.info(f"\t{random_stat[ran_choice]} Chosen.")
        logger.info(f"\tAdjusting {random_stat[ran_choice]} by + 2.")
        logger.info("\tChecking if Modifier Needs Adjusting.")
        self.set_learned_talents({f"Talent Str, Dex, or Con boost": f"{random_stat[ran_choice]} chosen."})
        choice = None
        match ran_choice:
            case 0:
                choice = "Strength"
                self.set_str(2)
                logger.info(f"\tStrength now = {self.str}")
                mod = self.modifier_check([self.str], ["Str"])
                if mod[0] > self.str_mod:
                    logger.info("\tAdjusting Strength Modifier.")
                    self.set_str_mod(mod[0])
            case 1:
                choice = "Dexterity"
                self.set_dex(2)
                logger.info(f"\tDexterity now = {self.dex}")
                mod = self.modifier_check([self.dex], ["Dex"])
                if mod[0] > self.dex_mod:
                    logger.info("\tAdjusting Dexterity Modifier.")
                    self.set_dex_mod(mod[0])
            case 2:
                choice = "Constitution"
                self.set_con(2)
                logger.info(f"\tConstitution now = {self.con}")
                mod = self.modifier_check([self.con], ["Con"])
                if mod[0] > self.con_mod:
                    logger.info("\tAdjusting Constitution Modifier.")
                    self.set_con_mod(mod[0])
        self.set_notes({"Fighter Talent": f"+2 Added to {choice} and Modifier Adjusted."})

    def armor_boost(self):
        logger.info("\tTalent: Armor Choice +1 to AC Boost Being Applied.")
        self.set_learned_talents({"Armor Boost Talent": {"Armor Choice +1 to AC Boost Applied."}})
        ac = self.ac
        gear_slots = self.gear_slots

        logger.info("\tRolling for Armor.")
        choice = random.choice(list(Armor))
        choice = 'Shield'
        self.set_armor(choice)
        note = {"Armor Properties": Armor[choice]["Properties"] + " +1 to AC is already applied."}
        self.set_armor_notes(note)

        logger.info(f"\tAdjusting AC and Gear Slots Based on {choice}.")
        match choice:
            case "Leather":
                logger.info(f"\tLeather armor was already equipped."
                            f"\n\tAC of {ac} and Gear Slot of {gear_slots} remains the same.")
            case "Chainmail":
                logger.info(f"\tChainmail Chosen Adjusting AC {ac} to {ac + 2}")
                self.ac += 2
                logger.info(f"\tAdjusting Gear Slots {gear_slots} to {gear_slots - 1} ")
                self.set_gear_slot(gear_slots - 1)

            case "Plate Mail":
                adjusted_ac = Armor["Plate Mail"]["AC"]
                logger.info(f"\tPlate Mail Chosen: Adjusting AC {ac} to {adjusted_ac}")
                self.ac += 3
                logger.info(f"\tAdjusting Gear Slots {gear_slots} to {gear_slots - 2} ")
                self.set_gear_slot(gear_slots - 2)

            case "Shield":
                logger.info(f"\tShield Chosen: Adjusting AC {ac} to + 2.")
                self.ac += 2
                logger.info(f"\tGear Slot of  {gear_slots} does not need to be adjusted.")

            case "Mithral CM":
                logger.info(f"\tMithral Chain Mail Chosen: Adjusting AC {ac} to {ac + 2}")
                self.ac += 2
                logger.info(f"\tAdjusting Gear Slots {gear_slots} to {gear_slots - 1} ")
                self.set_gear_slot(gear_slots - 1)

            case "Mithral PM":
                logger.info(f"\tMithral Plate Mail Chosen: Adjusting AC {ac} to 15")
                self.ac = 15
                logger.info(f"\tAdjusting Gear Slots {gear_slots} to {gear_slots - 1} ")
                self.set_gear_slot(gear_slots - 1)

        logger.info("\tApplying Talent +1 to AC bonus")
        self.ac += 1
        logger.info(f"\tFinal AC = {self.ac}")


class Priest(Character):
    def __init__(self):
        self.hero_class = "Priest"
        self.spells = {}
        self.talents = [self.advantage_on_spell, self.attack_bonus, self.cast_bonus, self.str_wis_boost,
                        self.stat_distribute]
        super().__init__()
        self.priest_specs()
        self.set_title()
        self.random_weapon()
        self.set_armor()
        self.set_spells()
        self.check_religion()
        self.talent_roll(self.talents)

    def __repr__(self):
        return "This is the Priest Class Object."

    def priest_specs(self):
        logger.info("Generating Priest Class Attributes.")
        self.priest_hp()
        self.priest_ac()

    def priest_hp(self):
        logger.info("Rolling for Priest HP 1d6.")
        result = self.roll_dice(6, 1)
        total = sum(result)
        logger.info(f"\tResult of Roll: {result} for a Total of {total}.")
        self.set_hp(total)

    def priest_ac(self):
        ac = 11 + self.get_dex_mod()
        logger.info(f"\tSetting AC 11 + DEX Modifier: {self.get_dex_mod()} = {ac}.")
        self.set_ac(ac)

    def set_title(self):
        title = Titles[self.hero_class][list(self.alignment)[0]]
        logger.info("Generating Title.")
        logger.info(f"\t{title}")
        self.title = title

    def random_weapon(self):
        logger.info("Choosing Random Weapon.")
        priest_weapons = ["Club", "Crossbow", "Dagger", "Mace", "Longsword", "Staff", "Warhammer"]
        random_weapon = random.choice(priest_weapons)
        logger.info(f"\t{random_weapon} chosen.")
        self.weapon = random_weapon
        note = {random_weapon: Weapons[random_weapon]}
        self.set_weapon_notes(note)

    def set_armor(self, armor=None):
        if armor is None:
            logger.info(f"Equipping Leather Armor.")
            note = {"Armor Properties": Armor["Leather"]["Properties"]}
            self.set_armor_notes(note)
            self.armor = Armor["Leather"]
        else:
            logger.info(f"Equipping {armor}.")
            self.armor = Armor[armor]

    def set_spells(self):
        default = "Turn Undead"
        logger.info(f"Priest is Learning two Random Spells and {default}.")
        spells = [item for item in Priest_Spells.keys() if item != default]
        choices = random.sample(set(spells), 2)
        choices.append(default)
        for spell in choices:
            self.spells.update({spell: Priest_Spells[spell]})
            logger.info(f"\tPriest learned {spell}")
            logger.info(f"\t\tAdding {spell} to Notes")

    def check_religion(self):
        logger.info("Checking Religion.")
        if self.deity is None:
            self.deity = random.choice(list(Deities[0].items()))

        deity = list(self.deity)[0]
        logger.info(f"\tPriest found {deity}.")
        logger.info(f"\tAdding {deity} Symbol to Gear.")
        self.gear.update({deity + "symbol": [{"Quantity": 1}, {"Gear Slot": 0}]})

    def advantage_on_spell(self):
        spell_key = list(self.spells)
        choice = random.choice(spell_key)
        logger.info(f"\tTalent: Advantage on casting spell {choice}.")
        self.set_learned_talents({"Spell Casting Talent": "Advantage on Casting Spells"})
        self.spells[choice].append('Priest Talent: Advantage')
        logger.info("\tUpdating Spell Book.")

    def attack_bonus(self):
        logger.info(f"\tTalent: +1 Attack to {self.weapon}")
        self.set_learned_talents({"Attack Bonus Talent": "+1 to Attack."})
        self.weapon_notes[self.weapon].append("Priest Talent: +1 to attack.")
        logger.info(f"\tAdding {self.weapon} boost to weapon notes.")

    def cast_bonus(self):
        logger.info(f"\tTalent: +1 to spell-casting checks.")
        self.set_learned_talents({"Spell Check Talent": "+1 to spell-casting checks."})

    def str_wis_boost(self):
        logger.info("\tTalent Strength or Wisdom Boost Being Applied")
        logger.info("\tRandomly Choosing Stat Boost.")
        random_stat = ["Strength", "Wisdom"]
        ran_choice = random.randint(0, 1)
        logger.info(f"\t{random_stat[ran_choice]} Chosen.")
        logger.info(f"\tAdjusting {random_stat[ran_choice]} by + 2.")
        logger.info("\tChecking if Modifier Needs Adjusting.")
        self.set_learned_talents({"Str or Wis Boost Talent": f"+2 to {random_stat[ran_choice]}"})
        choice = None
        match ran_choice:
            case 0:
                choice = "Strength"
                self.set_str(2)
                logger.info(f"\tStrength now = {self.str}")
                mod = self.modifier_check([self.str], ["Str"])
                if mod[0] > self.str_mod:
                    logger.info("\tAdjusting Strength Modifier.")
                    self.set_str_mod(mod[0])
            case 1:
                choice = "Wisdom"
                self.set_wis(2)
                logger.info(f"\tWisdom now = {self.wis}")
                mod = self.modifier_check([self.wis], ["Wis"])
                if mod[0] > self.dex_mod:
                    logger.info("\tAdjusting Wisdom Modifier.")
                    self.set_wis_mod(mod[0])

        self.set_notes({"Priest Talent": f"+2 Added to {choice} and Modifier Adjusted."})


class Thief(Character):
    def __init__(self):
        self.hero_class = "Thief"
        self.talents = [self.initiative_adv, self.back_stab_bonus, self.str_dex_cha,
                        self.attack_bonus, self.stat_distribute]
        super().__init__()
        self.thief_specs()
        self.set_title()
        self.random_weapon()
        self.set_armor()
        self.set_back_stab()
        self.set_thievery()
        self.talent_roll(self.talents)

    def __repr__(self):
        return "This is the Thief Class Object."

    def thief_specs(self):
        logger.info("Generating Thief Class Attributes.")
        self.thief_hp()
        self.thief_ac()

    def thief_hp(self):
        logger.info("Rolling for Thief HP 1d4.")
        result = self.roll_dice(4, 1)
        total = sum(result)
        logger.info(f"\tResult of Roll: {result} for a Total of {total}.")
        self.set_hp(total)

    def thief_ac(self):
        ac = 11 + self.get_dex_mod()
        logger.info(f"\tSetting AC 11 + DEX Modifier: {self.get_dex_mod()} = {ac}.")
        self.set_ac(ac)

    def set_title(self):
        title = Titles[self.hero_class][list(self.alignment)[0]]
        logger.info("Generating Title.")
        logger.info(f"\t{title}")
        self.title = title

    def random_weapon(self):
        logger.info("Choosing Random Weapon.")
        thief_weapons = ["Club", "Crossbow", "Dagger", "Shortbow", "Shortsword"]
        random_weapon = random.choice(thief_weapons)
        logger.info(f"\t{random_weapon} chosen.")
        self.weapon = random_weapon
        note = {random_weapon: Weapons[random_weapon]}
        self.set_weapon_notes(note)

    def set_armor(self, armor=None):
        if armor is None:
            logger.info(f"Equipping Leather Armor.")
            note = {"Armor Properties": Armor["Leather"]["Properties"]}
            self.set_armor_notes(note)
            self.armor = Armor["Leather"]
        else:
            logger.info(f"Equipping {armor}.")
            self.armor = Armor[armor]

    def set_back_stab(self):
        logger.info("Applying Back Stab.")
        self.set_notes({'Backstab': 'If you hit a creature who is unaware of your attack, you deal'
                                    'an extra weapon die of damage. Add additional weapon dice of damage'
                                    'equal to half your level(round down).'})

    def set_thievery(self):
        logger.info('Applying Thievery Class Attributes')
        self.set_notes({'Thievery': 'You are adept at thieving skills and have the necessary tools of the trade'
                                    'secreted on your person (they take up no gear slots).'})

        logger.info("\tUpdating Gear.")
        self.gear.update({"Thief Tools": [{"Quantity": 'inf'}, {"Gear Slot": 0}]})
        self.set_notes({'Thievery Training': 'You have advantage on Climbing, Sneaking and Hiding, Applying Disguises,'
                                             'Finding and Disabling Traps, Delicate Tasks Such as Picking Pockets and '
                                             'Opening Locks.'})

    def initiative_adv(self):
        logger.info('\tThief Talent: Gain Initiative Advantage.')
        self.set_learned_talents({'Thief Talent': 'Gain Advantage on Initiative Rolls (re-roll if duplicate)'})

    def back_stab_bonus(self):
        logger.info("\t Adding Backstab Talent Bonus to notes.")
        self.set_learned_talents({"Backstab Talent Bonus": "+1 dice of damage to backstab."})
        self.notes['Backstab'] += ' (Thief Talent: +1 dice of damage)'

    def str_dex_cha(self):
        logger.info("\tTalent Strength, Dexterity, or Charisma Boost Being Applied")
        logger.info("\tRandomly Choosing Stat Boost.")
        random_stat = ["Strength", "Dexterity", "Charisma"]
        ran_choice = random.randint(0, 2)
        logger.info(f"\t{random_stat[ran_choice]} Chosen.")
        logger.info(f"\tAdjusting {random_stat[ran_choice]} by + 2.")
        logger.info("\tChecking if Modifier Needs Adjusting.")
        choice = None
        match ran_choice:
            case 0:
                choice = "Strength"
                self.set_str(2)
                logger.info(f"\tStrength now = {self.str}")
                mod = self.modifier_check([self.str], ["Str"])
                if mod[0] > self.str_mod:
                    logger.info("\tAdjusting Strength Modifier.")
                    self.set_str_mod(mod[0])
            case 1:
                choice = "Dexterity"
                self.set_dex(2)
                logger.info(f"\tDexterity now = {self.dex}")
                mod = self.modifier_check([self.dex], ["Dex"])
                if mod[0] > self.dex_mod:
                    logger.info("\tAdjusting Dexterity Modifier.")
                    self.set_dex_mod(mod[0])
            case 2:
                choice = "Charisma"
                self.set_cha(2)
                logger.info(f"\tCharisma now = {self.cha}")
                mod = self.modifier_check([self.cha], ["Cha"])
                if mod[0] > self.cha_mod:
                    logger.info("\tAdjusting Charisma Modifier.")
                    self.set_cha_mod(mod[0])
        self.set_learned_talents({"Fighter Talent": f"+2 Added to {choice} and Modifier Adjusted."})

    def attack_bonus(self):
        logger.info(f"\tTalent: +1 Attack to {self.weapon}")
        self.weapon_notes[self.weapon].append("Thief Talent: +1 to attack.")
        self.set_learned_talents({"Attack Talent": "+1 to attack"})
        logger.info(f"\tAdding {self.weapon} boost to weapon notes.")


class Wizard(Character):
    def __init__(self):
        self.hero_class = "Wizard"
        self.spells = {}
        self.talents = [self.magic_item, self.spell_check_bonus, self.spell_adv,
                        self.add_spell, self.stat_distribute]
        self.magic_item = None
        super().__init__()
        self.wizard_specs()
        self.set_title()
        self.random_weapon()
        self.set_armor()
        self.set_learn_spells()
        self.set_spell_casting()
        self.talent_roll(self.talents)

    def __repr__(self):
        return "This is the Wizard Class Object."

    def wizard_specs(self):
        logger.info("Generating Wizard Class Attributes.")
        self.wizard_hp()
        self.wizard_ac()

    def wizard_hp(self):
        logger.info("Rolling for Wizard HP 1d4.")
        result = self.roll_dice(4, 1)
        total = sum(result)
        logger.info(f"\tResult of Roll: {result} for a Total of {total}.")
        self.set_hp(total)

    def wizard_ac(self):
        ac = 10 + self.get_dex_mod()
        logger.info(f"\tSetting AC 10 + DEX Modifier: {self.get_dex_mod()} = {ac}.")
        self.set_ac(ac)

    def set_title(self):
        title = Titles[self.hero_class][list(self.alignment)[0]]
        logger.info("Generating Title.")
        logger.info(f"\t{title}")
        self.title = title

    def random_weapon(self):
        logger.info("Choosing Random Weapon.")
        thief_weapons = ["Dagger", "Staff"]
        random_weapon = random.choice(thief_weapons)
        logger.info(f"\t{random_weapon} chosen.")
        self.weapon = random_weapon
        note = {random_weapon: Weapons[random_weapon]}
        self.set_weapon_notes(note)

    def set_armor(self):
        logger.info('Setting Armor.')
        logger.info('\tWizards Cannot Wear Armor.')
        self.armor = None

    def set_learn_spells(self):
        logger.info("Adding Learning Spells Wizard Attribute.")
        self.set_notes({'Learning Spells': "You can permanently learn a wizard spell from a spell scroll "
                                           "by studying  it for a day and succeeding on a DC 15 Intelligence Check. "
                                           "Whether you succeed or fail, you expend the spell scroll. Spells you learn"
                                           " in this way don't count toward your known spells."})

    def set_spell_casting(self):
        logger.info("Wizard is Learning Three Spells.")
        spells = [item for item in Tier_1_Spells.keys()]
        choices = random.sample(set(spells), 3)
        for spell in choices:
            self.spells.update({spell: Tier_1_Spells[spell]})
            logger.info(f"\tWizard learned {spell}")
            logger.info(f"\t\tAdding {spell} to Notes")

        self.set_notes({"Spell-casting": "Each time you gain a level, you choose new wizard spells to learn according "
                                         "to the Wizard Spells Known table."})

    def magic_item(self):
        logger.info("Crafting Magic Item")
        m_item = magical_item()
        self.set_learned_talents({"Magical Item Talent": "See Magical Item Notes about magical item."})
        self.magic_item = m_item

    def spell_check_bonus(self):
        logger.info("\tApplying Wizard Talent Intelligence or Spell-casting Check Bonus")
        logger.info("\tRandomly Choosing Intelligence Stat Boost or Spell-casting Check Boost.")
        random_choice = random.choice(['I', 'C'])
        if random_choice == 'C':
            logger.info("\tWizard Spell-casting Check Boost Chosen.")
            note = {'Wizard Talent': '+1 on Spell-casting Check.'}
            self.set_learned_talents(note)
            return

        self.apply_int_boost()

    def apply_int_boost(self):
        logger.info("\tIntelligence Stat Boost Chosen.")
        logger.info("\tApplying +1 to Intelligence.")
        logger.info("\tChecking for Modifier Adjustment.")
        note = {'Wizard Talent': '+1 to Intelligence.'}
        self.set_learned_talents(note)
        self.set_int(1)
        logger.info(f"\tIntelligence now = {self.int}")
        mod = self.modifier_check([self.int], ["Int"])
        if mod[0] > self.int_mod:
            logger.info("\tAdjusting Intelligence Modifier.")
            self.set_int_mod(mod[0])

    def spell_adv(self):
        logger.info("Applying Wizard Talent Spellcast Advantage.")
        logger.info("\tRandomly Choosing Spell.")
        random_spell = random.choice(list(self.spells))
        logger.info(f"\t{random_spell} Chosen to Give Cast Check Boost")
        logger.info(f"\tApplying +1 to Spell-Casting Check to Spell Notes.")
        self.spells[random_spell].append('Wizard Talent: +1 on Spell-Casting Checks')
        self.set_learned_talents({'Wizard Talent': '+1 on Spell-Casting Checks'})

    def add_spell(self):
        logger.info("\tApplying Wizard Talent Learning Additional Spell.")
        logger.info("\tRandomly Choosing Available Spell to Learn.")
        wizard_spells = set(list(Tier_1_Spells))
        known_spells = set(list(self.spells))
        symmetric_difference = list(known_spells.symmetric_difference(wizard_spells))
        random_choice = random.choice(symmetric_difference)
        logger.info(f"\tWizard Learning {random_choice}.")
        self.set_learned_talents({"Wizard Talent Learning Additional Spell": f"{random_choice} Spell Added to Spells."})
        spell_notes = Tier_1_Spells[random_choice]
        self.spells.update({random_choice: spell_notes})


def random_class():
    num = random.randint(0, 3)
    logger.info(f"Rolling for Random Class = {num}")
    logger.info("Generating Random Class.")
    new_hero = None
    match num:
        case 0:
            logger.info("\tFighter Class Chosen")
            new_hero = Fighter()
        case 1:
            logger.info("Priest Class Chosen")
            new_hero = Priest()
        case 2:
            logger.info("Thief Class Chosen")
            new_hero = Thief()
        case 3:
            logger.info("Wizard Class Chosen")
            new_hero = Wizard()

    return new_hero
