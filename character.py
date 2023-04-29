import random


class Character:
    def __init__(self):
        self.name = ""
        self.ancestry = ""
        self.str = 0
        self.int = 0
        self.dex = 0
        self.wis = 0
        self.con = 0
        self.cha = 0
        self.hp = 0
        self.ac = 0
        self.notes = {}

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
