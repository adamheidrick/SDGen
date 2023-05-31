import random

Armor = {"Leather": {"type": "leather", "gear_slot": 1, "AC": 11,
                     "Properties": "Just a bit of leather."},
         "Chainmail": {"type": "chainmail", "gear_slot": 2, "AC": 13,
                       "Properties": "Disadvantage on Stealth and Swim."},
         "Plate Mail": {"type": "plate mail", "gear_slot:": 3, "AC": 15,
                        "Properties": "Disadvantage on Stealth. No Swim."},
         "Shield": {"type": "shield", "gear_slot": 1, "AC": 2,
                    "Properties": "Occupies one Hand."},
         "Mithral CM": {"type": "mithral chainmail", "gear_slot": -1, "AC": 13,
                        "Properties": "No Penalty on Stealth and Swim."},
         "Mithral PM": {"type": "mithral plate mail", "gear_slot": -1, "AC": 15,
                        "Properties": "No Penalty on Stealth and Swim."}}

