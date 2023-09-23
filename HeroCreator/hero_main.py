import logging
import json


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
    parsed_hero = parse_hero(hero)
    json_hero = jsonify_hero(parsed_hero)
    return json_hero


def jsonify_hero(hero):
    hero.pop('talents')
    hero.pop('stats')
    hero.pop('learned_talents')
    hero = json.dumps(hero)
    return hero
