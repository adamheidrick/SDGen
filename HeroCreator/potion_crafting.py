import random
from magic_item_functions import choosing_qualities

feature_1 = ["Spicy", "Clear as water", "Deep Blue", "Citrus Smell", "Sulfurous", "Fizzy", "Chilly", "Blood red"]
feature_2 = [" a pickled spider inside", "green fumes", "tiny stars and a moon", "gold flakes in liquid",
             "a swirling vortex", "a quiet whistling noise", "a rattling and shaking noise", "an eyeball inside"]
feature_3 = ["is bubbling.", "purple streaks.", "flames on the surface.", "a floral smell.",
             "a skull on the bottle.", "emanates warmth.", "a large molar inside.", "a pink starburst."]

dice = ["1d4", "2d6", "3d8", "4d10"]
elements = ["fire", "cold", "electricity", "poison"]
limbs = ["arms", "legs"]

potion_benefit = [f"Immune 5 rounds to {random.choice(elements)}.",
                  f"Heals {random.choice(dice)}",
                  "Read the minds of all creatures within near for 1 hour.",
                  "Fly a near distance for 5 rounds.",
                  "For 5 rounds, move far on your turn and still take an action.",
                  "Become invisible for 5 rounds",
                  "Breathe underwater and know Merran language for 1 hour.",
                  "A stat becomes 18(+4) for 5 rounds.",
                  "Turn into purple, flying gas for 5 rounds",
                  "Cures any disease or affliction affecting drinker.",
                  "Speak to and understand animals for 1 hour.",
                  "You are immune to all damage for 5 rounds."]
potion_curse = ["DC 15 WIS check or attack nearest creature for 3 rounds.",
                "Turn into a 1 HP newt for 3 rounds.",
                "A stat becomes 3(-4) for 1 hour.",
                "DC 15 CON check or take 2d10 damage.",
                "Forget all languages you know for 1 hour.",
                "Shrink to half size and disadvantage on attacks for 5 rounds.",
                "Sing at the top of your lungs for 3 rounds.",
                "You become magnetic to all metal near to you for 1 hour.",
                "You are compelled to jump into any pits you see for 1 hour.",
                "DC 15 CON check or go blind for 5 rounds.",
                "You are the source of an ati-magic shell spell for 1 hour.",
                f"Your {random.choice(limbs)} are petrified for 5 rounds."]


def make_potion(quality, name):
    description = make_potion_description()
    qualities = choosing_qualities(quality, potion_curse, potion_benefit)
    return {'Name': name, 'Description': description, 'Qualities': qualities}


def make_potion_description():
    prefix = random.choice(feature_1)
    mid = random.choice(feature_2)
    suffix = random.choice(feature_3)
    return prefix + " with " + mid + " and " + suffix

