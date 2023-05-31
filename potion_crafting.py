import random

feature_1 = ["Spicy", "Clear as water", "Deep Blue", "Citrus Smell", "Sulfurous", "Fizzy", "Chilly", "Blood red"]
feature_2 = [" a pickled spider inside", "green fumes", "tiny stars and a moon", "gold flakes in liquid",
             "a swirling vortex", "a quiet whistling noise", "a rattling and shaking noise", "an eyeball inside"]
feature_3 = ["that is bubbling.", "purple streaks.", "flames on the surface.", "a floral smell.", "a skull on bottle.",
             "emanates warmth.", "a large molar inside.", "a pink starburst."]

dice = []
elements = []
limbs = []

potion_benefit = []
potion_curse = []


def make_potion():
    name = make_name()
    print(name)


def make_name():
    prefix = random.choice(feature_1)
    mid = random.choice(feature_2)
    suffix = random.choice(feature_3)
    return prefix + " with " + mid + " and " + suffix


make_potion()
