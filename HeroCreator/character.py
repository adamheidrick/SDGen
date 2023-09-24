from HeroCreator.background import Background, Alignment, Deities, Name
from HeroCreator.crawling_kit import equip_kit
from HeroCreator.ancestry import *
import logging

logger = logging.getLogger(__name__)


class Character:
    def __init__(self):
        self.name = ""
        self.title = ""
        self.armor = ""
        self.weapon = ""
        self.ancestry = ""
        self.background = ""
        self.languages = []
        self.deity = None
        self.alignment = {}
        self.learned_talents = {}
        self.hp = 0
        self.ac = 0
        self.str = 0
        self.str_mod = 0
        self.int = 0
        self.int_mod = 0
        self.dex = 0
        self.dex_mod = 0
        self.wis = 0
        self.wis_mod = 0
        self.con = 0
        self.con_mod = 0
        self.cha = 0
        self.cha_mod = 0
        self.gold = 5
        self.gear_slots = 3
        self.gear = equip_kit()
        self.notes = {}
        self.weapon_notes = {}
        self.armor_notes = {}
        self.stats = ["Str", "Int", "Dex", "Wis", "Con", "Cha"]
        self.roll_stats()
        self.set_background()
        self.roll_alignment()
        self.roll_religion()

    def set_name(self, ancestry):
        name = random.choice(Name[ancestry])
        self.name = name

    def set_hp(self, num):
        logger.info(f"\tIncreasing HP from {self.hp} + {num} = {self.hp + num}.")
        self.hp += num

    def set_ac(self, num):
        self.ac += num

    def set_ancestry(self, ancestry):
        self.ancestry = ancestry

    def set_str(self, num):
        self.str += num

    def set_int(self, num):
        self.int += num

    def set_dex(self, num):
        self.dex += num

    def set_wis(self, num):
        self.wis += num

    def set_con(self, num):
        self.con += num

    def set_cha(self, num):
        self.cha += num

    def set_str_mod(self, num):
        self.str_mod = num

    def set_int_mod(self, num):
        self.int_mod = num

    def set_wis_mod(self, num):
        self.wis_mod = num

    def set_cha_mod(self, num):
        self.cha_mod = num

    def set_dex_mod(self, num):
        self.dex_mod = num

    def set_con_mod(self, num):
        self.con_mod = num

    def set_notes(self, note):
        logger.info(f"\tAdding to Notes {note}")
        self.notes.update(note)

    def set_weapon_notes(self, note):
        logger.info(f"\tAdding {list(note)[0]} Details to Weapon Notes.")
        self.weapon_notes.update(note)

    def set_armor_notes(self, note):
        self.armor_notes = {}
        logger.info(f"\tAdding {list(note)[0]} Details to Armor Notes.")
        self.armor_notes.update(note)

    def get_dex_mod(self):
        return self.dex_mod

    def set_gear_slot(self, num):
        self.gear_slots += num

    def get_con_mod(self):
        return self.con_mod

    def set_learned_talents(self, talent):
        self.learned_talents.update(talent)

    def apply_stats(self, stats):
        logger.info("Applying Base Stats to Character.")
        self.str, self.str_mod = stats[0]
        logger.info(f"\tStr: {self.str} Str Mod {self.str_mod}")
        self.int, self.int_mod = stats[1]
        logger.info(f"\tInt: {self.int} Int Mod {self.int_mod}")
        self.dex, self.dex_mod = stats[2]
        logger.info(f"\tDex: {self.dex} Dex Mod {self.dex_mod}")
        self.wis, self.wis_mod = stats[3]
        logger.info(f"\tWis: {self.wis} Wis Mod {self.wis_mod}")
        self.con, self.con_mod = stats[4]
        logger.info(f"\tCon: {self.con} Con Mod {self.con_mod}")
        self.cha, self.cha_mod = stats[5]
        logger.info(f"\tCha: {self.cha} Cha Mod {self.cha_mod}")

    def calculate_modifiers(self, rolls):
        logger.info("Calculating Modifiers.")
        modifiers = self.modifier_check(rolls)
        stats = list(zip(rolls, modifiers))
        self.apply_stats(stats)

    def modifier_check(self, rolls, stats=None):
        if stats is None:
            stats = self.stats
        modifiers = []
        mod_dict = {3: -4, 5: -3, 7: -2, 9: -1, 11: 0, 13: 1, 15: 2, 17: 3}
        for index, num in enumerate(rolls):
            for check in range(3, 18, 2):
                if num <= check:
                    modifiers.append(mod_dict[check])
                    logger.info(
                        f"\tApplying {stats[index]} : {num} a modifier of {mod_dict[check]}."
                    )
                    break
                elif num >= 18:
                    modifiers.append(4)
                    logger.info(
                        f"\tApplying {stats[index]} : {num} a modifier of {mod_dict[check]}."
                    )
                    break
        return modifiers

    def stat_distribute(self):
        logger.info("\tStat Distribution Talent Being Applied.")
        self.set_learned_talents(
            {"Stat Distribution Talent": "Lowest Two Stats Received + 1"}
        )
        stat_names = ["Str", "Int", "Dex", "Wis", "Con", "Cha"]
        stats = [self.str, self.int, self.dex, self.wis, self.con, self.cha]
        mods = [
            self.str_mod,
            self.int_mod,
            self.dex_mod,
            self.wis_mod,
            self.con_mod,
            self.cha_mod,
        ]
        mod_funcs = [
            self.set_str_mod,
            self.set_int_mod,
            self.set_dex_mod,
            self.set_wis_mod,
            self.set_con_mod,
            self.set_cha_mod,
        ]
        funcs = [
            self.set_str,
            self.set_int,
            self.set_dex,
            self.set_wis,
            self.set_con,
            self.set_cha,
        ]
        for _ in range(2):
            minimum = min(stats)
            self.find_min(minimum, stats, funcs, mod_funcs, mods, stat_names)

    def find_min(self, minimum, stats, funcs, mod_funcs, mods, stat_names):
        for index, stat in enumerate(stats):
            if stat == minimum:
                logger.info(
                    f"\tIncreasing {stat_names[index]} {stats[index]} + 1 = {stats[index] + 1}"
                )
                funcs[index](1)
                mod = self.modifier_check([stats[index] + 1], [stat_names[index]])
                if mod[0] > mods[index]:
                    new_mod = mod[0]
                    old_mod = mods[index]
                    logger.info(f"\tAdjusting {stat_names[index]} Modifier")
                    mod_funcs[index](new_mod)
                    if index == 2:
                        difference = abs(new_mod - old_mod)
                        logger.info(
                            f"\tAdjusting AC based on difference between {new_mod} and {old_mod} = {difference}"
                        )
                        self.ac += difference
                note = {
                    "Talent Point Distribution": f"Increased {stat_names[index]} from {stats[index]}"
                    f" to {stats[index] + 1} and adjusted the {stat_names[index]}"
                    f" modifier accordingly."
                }
                self.set_notes(note)

                del mod_funcs[index]
                del mods[index]
                del stats[index]
                del funcs[index]
                del stat_names[index]
                break

    def roll_stats(self):
        logger.info("Rolling for stats.")
        rolls = self.stat_builder()
        while max(rolls) < 14:
            max_rolled = max(rolls)
            logger.info(
                f"Stats were insufficient. Max roll was {max_rolled}. Need 14 or higher. Re-rolling."
            )
            rolls = self.stat_builder()

        self.calculate_modifiers(rolls)

    def stat_builder(self):
        rolls = []
        for num in range(len(self.stats)):
            results = self.roll_dice(6, 3)
            total = sum(results)
            logger.info(
                f"\tRolling 3d6 for {self.stats[num]}: Dice Results = {results} Total = {total}."
            )
            rolls.append(total)
        return rolls

    @staticmethod
    def roll_dice(sided, times):
        return [random.randint(1, sided) for _ in range(times)]

    def roll_alignment(self):
        logger.info("Rolling for Alignment.")
        self.alignment = random.choice(Alignment)
        logger.info(f"\tAlignment = {list(self.alignment)[0]}")

    def roll_religion(self):
        logger.info("Rolling for Religion.")
        coin_toss = random.randint(0, 1)
        deity_dict = {}
        if coin_toss == 1:
            chosen_diety = random.choice(list(Deities[0].items()))
            key, value = chosen_diety
            deity_dict[key] = value
            self.deity = deity_dict
            logger.info(f"\tDeity = {list(self.deity)[0]}")
        else:
            deity_dict['None'] = f'{self.name} does not believe in God . . . yet.'
            self.deity = deity_dict
            logger.info("\tThis character as of now does not believe in God.")

    def set_background(self):
        logger.info("Rolling for Background.")
        result = random.choice(Background)
        title = result.split(":")[0]
        body = result.split(":")[1]
        self.background = title
        self.set_notes({title: body})

    def talent_index(self):
        logger.info("Rolling 2d6 for Talent.")
        roll = self.roll_dice(6, 2)
        total = sum(roll)
        logger.info(f"\tRoll Result: {roll} = {total}")
        upper_bound = 7

        if total == 2:
            return 0

        for index in range(1, 4):
            if total <= upper_bound:
                return index
            upper_bound += 2

        return 4

    def talent_roll(self, talents):
        index = self.talent_index()
        while index > len(talents) - 1:
            index = self.talent_index()
        self.choose_talent(index, talents)

    def choose_talent(self, index, talents):
        logger.info(f"\tChoosing Talent.")

        choice = talents[index]
        choice()
        talents.remove(choice)
