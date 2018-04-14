from card import Card
import yakus

class Player:
  def __init__(self, name, cards):
    self.name = name
    self.cards = cards
    self.pickedup = []
    self.score = 0
    self.oldscore = 0

  def add_card(self, card):
    card.set_owner(self)
    self.cards.append(card)

  def pick_up(self, card):
    self.pickedup.append(card)

  def put_down(self, card):
    card.set_owner(None)
    self.cards.remove(card)

  def check_yakus(self):
    self.score = yakus.get_worth(self.pickedup)
    return self.score

  def get_yakus(self):
    return yakus.get_distance(self.pickedup)

  
