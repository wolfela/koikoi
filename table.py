from card import Card

class Table:
    cards = []

    def __init__(self, cards):
        self.cards = cards

    def pick_up(self, played, pickup, hand):
        if played.can_pick_up(pickup):
            self.cards.remove(pickup)
            hand.append(pickup)