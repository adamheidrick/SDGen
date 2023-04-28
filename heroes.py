from character import Character


class Fighter(Character):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "This is the Fighter Class Object."


class Priest(Character):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "This is the Priest Class Object."


class Thief(Character):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "This is the Thief Class Object."


class Wizard(Character):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "This is the Wizard Class Object."
