import random


def choosing_qualities(qualities, curses, benefits):
    quality_1, quality_2 = qualities
    curse = random.choice(curses)
    benefit = random.choice(benefits)

    if quality_1 is None and quality_2 == "curse":
        return 'Curse: ' + curse

    if quality_1 == "benefit" and quality_2 == 'curse':
        qualities = 'Benefit: ' + benefit + ' Curse: ' + curse
        return qualities

    if quality_1 == "benefit" and quality_2 is None:
        return 'Benefit: ' + benefit

    return "Benefits: " + str(random.sample(benefits, 2))

