import random
from background import Background, Alignment, Deities
from ancestry import *


class Character:
    def __init__(self):
        self.name = ""
        self.ancestry = ""
        self.background = ""
        self.deity = None
        self.alignment = {}
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
        self.gear_slots = 10
        self.notes = {}
        self.stats = ["Str", "Int", "Dex", "Wis", "Con", "Cha"]
        self.roll_stats()
        self.set_background()
        self.roll_alignment()
        self.roll_religion()

    def set_hp(self, num):
        print(f"Increasing HP from {self.hp} + {num} = {self.hp + num}.")
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

    def set_notes(self, note):
        print(f"Adding to notes {note}")
        self.notes.update(note)

    def get_dex_mod(self):
        return self.dex_mod


    def set_gear_slot(self, num):
        self.gear_slots += num

    def get_con_mod(self):
        return self.con_mod

    def apply_stats(self, stats):
        print("Applying Base Stats to Character.")
        self.str, self.str_mod = stats[0]
        self.int, self.int_mod = stats[1]
        self.dex, self.dex_mod = stats[2]
        self.wis, self.wis_mod = stats[3]
        self.con, self.con_mod = stats[4]
        self.cha, self.cha_mod = stats[5]

    def calculate_modifiers(self, rolls):
        print("Calculating Modifiers.")
        modifiers = []
        mod_dict = {3: -4, 5: -3, 7: -2, 9: -1, 11: 0, 13: 1, 15: 2, 17: 3}
        for index, num in enumerate(rolls):
            for check in range(3, 18, 2):
                if num <= check:
                    modifiers.append(mod_dict[check])
                    print(f"Applying {self.stats[index]} : {num} a modifier of {mod_dict[check]}.")
                    break
                elif num >= 18:
                    modifiers.append(4)
                    print(f"Applying {self.stats[index]} : {num} a modifier of {mod_dict[check]}.")
                    break
        stats = list(zip(rolls, modifiers))
        self.apply_stats(stats)

    def roll_stats(self):
        print("Rolling for stats.")
        rolls = self.stat_builder()
        while max(rolls) < 14:
            max_rolled = max(rolls)
            print(f"Stats were insufficient. Max roll was {max_rolled}. Need 14 or higher. Re-rolling.")
            rolls = self.stat_builder()

        self.calculate_modifiers(rolls)

    def stat_builder(self):
        rolls = []
        for num in range(len(self.stats)):
            results = self.roll_dice(6, 3)
            total = sum(results)
            print(f"Rolling 3d6 for {self.stats[num]}: Dice Results = {results} Total = {total}.")
            rolls.append(total)
        return rolls

    @staticmethod
    def roll_dice(sided, times):
        return [random.randint(1, sided) for num in range(times)]

    def roll_alignment(self):
        print("Rolling for Alignment.")
        self.alignment = random.choice(Alignment)
        print(f"Alignment = {list(self.alignment)[0]}")

    def roll_religion(self):
        print("Rolling for Religion.")
        coin_toss = random.randint(0, 1)
        if coin_toss == 1:
            self.deity = random.choice(list(Deities[0].items()))
            print(f"Deity = {list(self.deity)[0]}")
        else:
            print("This character as of now does not believe in God.")

    def set_background(self):
        result = random.choice(Background)
        title = result.split(':')[0]
        body = result.split(':')[1]
        self.background = title
        self.notes.update({title: body})


