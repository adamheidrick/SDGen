import logging

from hero_logger import start_logger
from heroes import random_class
from ancestry import set_ancestry
from backpack import pack_backpack
from hero_parser import parse_hero

logger = logging.getLogger(__name__)


def main():
    start_logger()
    hero = random_class()
    set_ancestry(hero)
    pack_backpack(hero)
    parse_hero(hero)


if __name__ == "__main__":
    main()
