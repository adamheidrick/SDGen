import json

from HeroCreator.hero_main import create_hero
from HeroCreator.magic_item_gen import generate_magical_item

hero = create_hero()
hero.pop('talents')
hero.pop('stats')
cleaned = json.dumps(hero, indent=4)
print(cleaned)

# magic_weapon = generate_magical_item()
# print(json.dumps(magic_weapon, indent=4))


