import uuid

class Card:

    def __init__(self, month, family):
        self.month = month
        self.family = family

    def is_equal(self, month, family):
        if month == self.month and family == self.family:
            return True
        return False

    def can_pick_up(self, month):
        if month == self.month:
            return True
        return False

