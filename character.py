import random


class Character:
    def __init__(self):
        self.name = ""
        self.ancestry = ""
        self.hero_clas = ""
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
        self.hp = 0
        self.ac = 0
        self.notes = {}

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

    def set_hp(self, num):
        self.hp += num

    def set_ac(self, num):
        self.ac += num

    def set_notes(self, note):
        self.notes.update(note)

    def apply_stats(self, stats):
        self.str, self.str_mod = stats[0]
        self.int, self.int_mod = stats[1]
        self.dex, self.dex_mod = stats[2]
        self.wis, self.wis_mod = stats[3]
        self.con, self.con_mod = stats[4]
        self.cha, self.cha_mod = stats[5]
        self.hp = stats[6][0]
        self.ac = stats[7][0]

    @classmethod
    def roll_stats(cls):
        rolls = [0]
        max_num = 0
        while max(rolls) < 14:
            rolls = [cls.roll_dice(6, 3) for num in range(8)]
        return rolls

    @staticmethod
    def roll_dice(sided, times):
        return sum([random.randint(1, sided) for num in range(times)])
