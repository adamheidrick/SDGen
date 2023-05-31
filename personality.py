import random
from background import Deities

owes_favor = ["Unicorn", "Dragon", "Noble"]
animals = ["dogs", "horses", "cats", "birds"]
undo = ["evil", "lie", "spell", "alliance"]
fears = ["The Dark", "Vermin", "Heights", "Water"]
dislikes = ["Elves", "Dwarves", "Humans", "Goblins"]
Objections = ["Gambling", "Carousing", "Stealth", "Theft"]
Wont_harm = ["Lawful", "Neutral", "Chaotic"]
Objects_More = ["Negotiating", "Fighting", "Planning"]
Gods = list(Deities[0].keys())

item_virtue = ["Insists on protecting people and creatures it likes.",
               "Warns its wielder if it senses impending danger.",
               "Gladly translates Primordial for its wielder.",
               "Senses hiding creatures within near, but not exact place.",
               f"Owed a favor by {random.choice(owes_favor)}.",
               "Commands the respect of the followers of a God.",
               "Occasionally remembers useful ancient history.",
               "Imparts pleasant dreams and good sleep to its wielder.",
               "Coaches its wielder on the right things to say in a situation.",
               "Sometimes provides helpful strategic advice.",
               "Occasionally notices important details others have missed.",
               "Tries to mediate disagreements between conscious items.",
               f"Calming Presence to {random.choice(animals)}.",
               "Has an extremely acute sense of smell.",
               "Knows the direction of the nearest running water.",
               "Lawful, intimidating to chaotic creatures.",
               "Neutral, intimidating to lawful and chaotic creatures.",
               "Chaotic, intimidating to lawful creatures.",
               "Has legitimate prophecies but isn't sure of their meaning.",
               f"Can undo a great {random.choice(undo)} alliance"]

item_flaw = [f"Afraid of {random.choice(fears)}.",
             "Preferred a past owner and always draws comparisons.",
             "Chatters while wielder is trying to concentrate.",
             f"Dislikes{random.choice(dislikes)}.",
             "Tried to get wielder into fights so it has 'something to do.'",
             "Does not want to be separated from wielder for any reason.",
             f"Objects to{Objections}.",
             "Accuses everyone of lying; is correct once in a while.",
             f"Won't harm {random.choice(Wont_harm)}.",
             "Believes its wielder is a pawn in its apocalyptic scheme.",
             "Constantly tries to escape its wielder",
             f"Demands its wielder observe its god's strict rituals. Tries to convert wielder to {random.choice(Gods)}"
             f" if wielder does not believe in god.",
             f"Insists on being reunited with its {random.choice(['Living', 'Dead'])} creator.",
             "Can't stand other conscious magic items.",
             "Refuses to be used for 'unimportant' or 'boring' tasks.",
             "Purposefully goes magically inert when mad at its wielder.",
             "Insists on being meticulously cleaned every day.",
             "Loves the color purple and despises all other colors.",
             f"Objects to {random.choice(Objects_More)}.",
             "Pretends to know information it doesn't know."
             ]

personality_trait = ["Imperious", "Polite", "Puritanical", "Charming", "Anxious", "Righteous", "Critical", "Theatrical",
                     "Bossy", "Noble", "Greedy", "Protective", "Impulsive", "Brave", "Vicious", "Loyal"]


