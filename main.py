import logging

from hero_logger import start_logger
from heroes import random_class
from ancestry import set_ancestry
from backpack import pack_backpack

logger = logging.getLogger(__name__)


def main():
    start_logger()
    hero = random_class()
    set_ancestry(hero)
    pack_backpack(hero)
    print(hero.__dict__)


if __name__ == "__main__":
    main()
