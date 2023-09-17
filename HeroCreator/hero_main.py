import logging

from HeroCreator.ancestry import set_ancestry
from HeroCreator.backpack import pack_backpack
from HeroCreator.heroes import random_class
from HeroCreator.hero_logger import start_logger
from HeroCreator.hero_parser import parse_hero

logger = logging.getLogger(__name__)


def create_hero():
    start_logger()
    hero = random_class()
    set_ancestry(hero)
    pack_backpack(hero)
    finished_hero = parse_hero(hero)
    return finished_hero
