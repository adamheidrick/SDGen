def equip_kit():
    crawling_kit = {
        "Backpack": {"Quantity": 1, "Slots Taken": 0},
        "Flint and Steel": {"Quantity": 1, "Slots Taken": 1},
        "Torch": {"Quantity": 2, "Gear Slot": 2},
        "Rations": {"Quantity": 3, "Gear Slot": 1},
        "Iron Spikes": {"Quantity": 10, "Gear Slot": 1},
        "Grappling Hook": {"Quantity": 1, "Gear Slot": 1},
        "Rope 60'": {"Quantity": 1, "Gear Slot": 1},
    }

    return crawling_kit

kit = equip_kit()
for key, value in kit.items():
    print(key, value)