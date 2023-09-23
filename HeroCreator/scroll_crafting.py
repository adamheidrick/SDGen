import random

from HeroCreator.magic_item_functions import choosing_qualities
from HeroCreator.magic_ulitity import utility_benefit, utility_curse
from HeroCreator.potion_crafting import potion_benefit, potion_curse
from HeroCreator.armor import magical_armor_benefits, magical_armor_curse
from HeroCreator.weapons import Weapon_benefits, Weapon_curses
from HeroCreator.character import Character
from HeroCreator.spells import (
    Tier_1_Spells,
    Tier_2_Spells,
    Tier_3_Spells,
    Tier_4_Spells,
    Tier_5_Spells,
)

scroll_features = [
    "Branded on Leather.",
    "Etched on Copper Leaf.," "Faded Papyrus.",
    "Stained Parchment Roll.",
    "Carved into Bone.",
    "Chiseled on Stone Slats.",
    "Etched into Glass.",
    "Tattooed on Dragon Skin.",
]

wand_features = [
    "Carved from Bone.",
    "Blinking eye in Handle.",
    "Sleep Starmetal.",
    "Polished Wood.",
    "Obsidian with Ivory Tips.",
    "Electrical Sparks.",
    "Jagged Crystal.",
    "Made of Tiny Skulls.",
]


def benefit_curse(qualities):
    r_benefit = random.choice(
        [utility_benefit, potion_benefit, magical_armor_benefits, Weapon_benefits]
    )
    r_curse = random.choice(
        [utility_curse, potion_curse, magical_armor_curse, Weapon_curses]
    )
    return choosing_qualities(qualities, r_curse, r_benefit)


def feature(item_type):
    if item_type == "Wand":
        return random.choice(wand_features)
    return random.choice(scroll_features)


def spell_tier():
    roll = sum(Character.roll_dice(6, 2))
    upper_limit = 5
    for num in range(0, 5):
        if roll <= upper_limit:
            return num
        upper_limit += 2


def random_spell(sp_tier):
    all_spells = [
        Tier_1_Spells,
        Tier_2_Spells,
        Tier_3_Spells,
        Tier_4_Spells,
        Tier_5_Spells,
    ]
    spell_list = list(all_spells[sp_tier])
    r_spell = random.choice(spell_list)
    spell_details = all_spells[sp_tier][r_spell]
    return {r_spell: spell_details}


def make_magic_scroll_wand(qualities, name, item_type):
    r_feature = feature(item_type)
    qualities = benefit_curse(qualities)
    s_tier = spell_tier()
    spell = random_spell(s_tier)

    magic_item = {
        "Magical Item": name,
        "Type": item_type,
        "Features": r_feature,
        "Qualities": qualities,
        "Spell Tier": s_tier + 1,
        "Spell": spell,
    }

    return magic_item
