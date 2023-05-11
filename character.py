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
        self.gear_slots = 10
        self.notes = {}
        self.roll_stats()
        self.set_background()
        self.roll_alignment()
        self.roll_religion()

    def set_hp(self, num):
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
        self.notes.update(note)

    def get_dex_mod(self):
        return self.dex_mod

    def set_gear_slot(self, num):
        self.gear_slots += num

    def get_con_mod(self):
        return self.con_mod

    def apply_stats(self, stats):
        self.str, self.str_mod = stats[0]
        self.int, self.int_mod = stats[1]
        self.dex, self.dex_mod = stats[2]
        self.wis, self.wis_mod = stats[3]
        self.con, self.con_mod = stats[4]
        self.cha, self.cha_mod = stats[5]

    def calculate_modifiers(self, rolls):
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
        stats = list(zip(rolls, modifiers))
        self.apply_stats(stats)

    def roll_stats(self):
        rolls = [0]
        max_num = 0
        while max(rolls) < 14:
            rolls = [self.roll_dice(6, 3) for num in range(8)]

        self.calculate_modifiers(rolls)

    @staticmethod
    def roll_dice(sided, times):
        return sum([random.randint(1, sided) for num in range(times)])

    def roll_alignment(self):
        self.alignment = random.choice(Alignment)

    def roll_religion(self):
        coin_toss = random.randint(0, 1)
        if coin_toss == 1:
            self.deity = random.choice(list(Deities[0].items()))

    def set_background(self):
        result = random.choice(Background)
        title = result.split(':')[0]
        body = result.split(':')[1]
        self.background = title
        self.notes.update({title: body})


