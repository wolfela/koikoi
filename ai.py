from yakus import *

class RandomAi:
  def __init__(self, player):
    self.player = player
  
  def make_move(self, table):
    for old in self.player.cards:
      for card in table.cards:
        if old.can_pick_up(card):
          return (old, card)
    return (self.player.cards[0], table.cards[len(table.cards)-1])

  def make_move_during(self, table, card):
    for tcard in table.cards:
        if card.can_pick_up(tcard):
          return tcard
    return table.cards[len(table.cards)-1]

  def koi_koi_decision(self, cards):
    return False

class PointsAi:
  def __init__(self, player):
    self.player = player
  
  def make_move(self, table):
    highestscore = 0
    highestpair = (self.player.cards[0], table.cards[len(table.cards)-1])
    for old in self.player.cards:
      for card in table.cards:
        if old.can_pick_up(card):
           if (old.points + card.points > highestscore):
             highestscore = old.points + card.points
             highestpair = (old, card)
    return highestpair

  def make_move_during(self, table, card):
    highestscore = 0
    highestcard = table.cards[len(table.cards)-1]
    for tcard in table.cards:
        if card.can_pick_up(tcard):
          if card.points > highestscore:
            highestscore = tcard.points
            highestcard = tcard
    return highestcard

  def koi_koi_decision(self, cards):
    return False

class HeuristicAi:
  def __init__(self, player):
    self.player = player

  def get_yaku(self, cards, yaku):
    if yaku == 'Kasu':
      return kasu(cards)
    elif yaku == 'Tane,Ino-shika-cho':
      return tane_ino_shika_cho(cards)
    elif yaku == 'Ame-Shiko,Shiko,Goko,Sanko':
      return ame_shiko_goko_sanko(cards)
    elif yaku == 'Aka-tan,Ao-tan,Tan':
      return aka_ao_tan(cards)

  def get_distance_score(self, cards, yaku):
    output = self.get_yaku(cards, yaku)
    if output[0] > 0:
      distanceweightedbyscore = (-100)*output[0]
    else:
      distance = sum(output[1])
      # these should take away from the number needed
      if yaku == 'Kasu':
        distanceweightedbyscore = (10-(distance))
      elif yaku == 'Tane,Ino-shika-cho':
        distanceweightedbyscore = (5-(distance))
      elif yaku == 'Ame-Shiko,Shiko,Goko,Sanko':
        distanceweightedbyscore = (5-(distance))
      elif yaku == 'Aka-tan,Ao-tan,Tan':
        distanceweightedbyscore = (5-(distance))
    return distanceweightedbyscore

  def make_move(self, table):
    bestdistanceweightedbyscore = 100
    bestcard = (self.player.cards[0], table.cards[len(table.cards)-1])
    for old in self.player.cards:
      distanceweightedbyscore = 0
      olddistanceweightedbyscore = 0
      for yaku in self.player.get_yakus():
        if yaku[0] == 0:
          if card_in_yaku(old) == yaku[2]:
            distanceweightedbyscore = self.get_distance_score(self.player.cards + [old], yaku[2])
            olddistanceweightedbyscore = distanceweightedbyscore
      for card in table.cards:
        distanceweightedbyscore = olddistanceweightedbyscore
        if old.can_pick_up(card):
          for yaku in self.player.get_yakus():
            if yaku[0] == 0:
              if card_in_yaku(card) == yaku[2]:
                distanceweightedbyscore = distanceweightedbyscore + self.get_distance_score(self.player.cards + [card], yaku[2])
          if (distanceweightedbyscore <  bestdistanceweightedbyscore):
            bestdistanceweightedbyscore = distanceweightedbyscore
            bestcard = (old, card)
    return bestcard

  def make_move_during(self, table, card):
    bestdistanceweightedbyscore = 100
    bestcard = table.cards[len(table.cards)-1]
    distanceweightedbyscore = 0
    olddistanceweightedbyscore = 0
    for yaku in self.player.get_yakus():
      if yaku[0] == 0:
        if card_in_yaku(card) == yaku[2]:
          distanceweightedbyscore = self.get_distance_score(self.player.cards + [card], yaku[2])
          olddistanceweightedbyscore = distanceweightedbyscore
    for tcard in table.cards:
        distanceweightedbyscore = olddistanceweightedbyscore
        if card.can_pick_up(tcard):
          for yaku in self.player.get_yakus():
            if yaku[0] == 0:
              if card_in_yaku(tcard) == yaku[2]:
                distanceweightedbyscore = distanceweightedbyscore + self.get_distance_score(self.player.cards + [tcard], yaku[2])
          if (distanceweightedbyscore <  bestdistanceweightedbyscore):
            bestdistanceweightedbyscore = distanceweightedbyscore
            bestcard = tcard
    return bestcard

  def koi_koi_decision(self, cards):
    return False

class PHeuristicAi:
  def __init__(self, player):
    self.player = player

  def get_yaku(self, cards, yaku):
    if yaku == 'Kasu':
      return kasu(cards)
    elif yaku == 'Tane,Ino-shika-cho':
      return tane_ino_shika_cho(cards)
    elif yaku == 'Ame-Shiko,Shiko,Goko,Sanko':
      return ame_shiko_goko_sanko(cards)
    elif yaku == 'Aka-tan,Ao-tan,Tan':
      return aka_ao_tan(cards)

  def get_distance_score(self, cards, yaku):
    output = self.get_yaku(cards, yaku)
    if output[0] > 0:
      distanceweightedbyscore = (-100)*output[0]
    else:
      distance = sum(output[1])
      # these should take away from the number needed
      if yaku == 'Kasu':
        distanceweightedbyscore = (10-(distance*0.5))
      elif yaku == 'Tane,Ino-shika-cho':
        distanceweightedbyscore = (5-(distance*0.154))
      elif yaku == 'Ame-Shiko,Shiko,Goko,Sanko':
        distanceweightedbyscore = (5-(distance*0.1))
      elif yaku == 'Aka-tan,Ao-tan,Tan':
        distanceweightedbyscore = (5-(distance*0.2))
    return distanceweightedbyscore

  def make_move(self, table):
    bestdistanceweightedbyscore = 100
    bestcard = (self.player.cards[0], table.cards[len(table.cards)-1])
    for old in self.player.cards:
      distanceweightedbyscore = 0
      olddistanceweightedbyscore = 0
      for yaku in self.player.get_yakus():
        if yaku[0] == 0:
          if card_in_yaku(old) == yaku[2]:
            distanceweightedbyscore = self.get_distance_score(self.player.cards + [old], yaku[2])
            olddistanceweightedbyscore = distanceweightedbyscore
      for card in table.cards:
        distanceweightedbyscore = olddistanceweightedbyscore
        if old.can_pick_up(card):
          for yaku in self.player.get_yakus():
            if yaku[0] == 0:
              if card_in_yaku(card) == yaku[2]:
                distanceweightedbyscore = distanceweightedbyscore + self.get_distance_score(self.player.cards + [card], yaku[2])
          if (distanceweightedbyscore <  bestdistanceweightedbyscore):
            bestdistanceweightedbyscore = distanceweightedbyscore
            bestcard = (old, card)
    return bestcard

  def make_move_during(self, table, card):
    bestdistanceweightedbyscore = 100
    bestcard = table.cards[len(table.cards)-1]
    distanceweightedbyscore = 0
    olddistanceweightedbyscore = 0
    for yaku in self.player.get_yakus():
      if yaku[0] == 0:
        if card_in_yaku(card) == yaku[2]:
          distanceweightedbyscore = self.get_distance_score(self.player.cards + [card], yaku[2])
          olddistanceweightedbyscore = distanceweightedbyscore
    for tcard in table.cards:
        distanceweightedbyscore = olddistanceweightedbyscore
        if card.can_pick_up(tcard):
          for yaku in self.player.get_yakus():
            if yaku[0] == 0:
              if card_in_yaku(tcard) == yaku[2]:
                distanceweightedbyscore = distanceweightedbyscore + self.get_distance_score(self.player.cards + [tcard], yaku[2])
          if (distanceweightedbyscore <  bestdistanceweightedbyscore):
            bestdistanceweightedbyscore = distanceweightedbyscore
            bestcard = tcard
    return bestcard

  def koi_koi_decision(self, cards):
    return False

class WHeuristicAi:
  def __init__(self, player):
    self.player = player

  def get_yaku(self, cards, yaku):
    if yaku == 'Kasu':
      return kasu(cards)
    elif yaku == 'Tane,Ino-shika-cho':
      return tane_ino_shika_cho(cards)
    elif yaku == 'Ame-Shiko,Shiko,Goko,Sanko':
      return ame_shiko_goko_sanko(cards)
    elif yaku == 'Aka-tan,Ao-tan,Tan':
      return aka_ao_tan(cards)

  def get_distance_score(self, cards, yaku):
    output = self.get_yaku(cards, yaku)
    if output[0] > 0:
      distanceweightedbyscore = (-100)*output[0]
    else:
      distance = sum(output[1])
      # these should take away from the number needed
      if yaku == 'Kasu':
        distanceweightedbyscore = (10-(distance*1))
      elif yaku == 'Tane,Ino-shika-cho':
        distanceweightedbyscore = (5-(distance*6))
      elif yaku == 'Ame-Shiko,Shiko,Goko,Sanko':
        distanceweightedbyscore = (5-(distance*32))
      elif yaku == 'Aka-tan,Ao-tan,Tan':
        distanceweightedbyscore = (5-(distance*20))
    return distanceweightedbyscore

  def make_move(self, table):
    bestdistanceweightedbyscore = 100
    bestcard = (self.player.cards[0], table.cards[len(table.cards)-1])
    for old in self.player.cards:
      distanceweightedbyscore = 0
      olddistanceweightedbyscore = 0
      for yaku in self.player.get_yakus():
        if yaku[0] == 0:
          if card_in_yaku(old) == yaku[2]:
            distanceweightedbyscore = self.get_distance_score(self.player.cards + [old], yaku[2])
            olddistanceweightedbyscore = distanceweightedbyscore
      for card in table.cards:
        distanceweightedbyscore = olddistanceweightedbyscore
        if old.can_pick_up(card):
          for yaku in self.player.get_yakus():
            if yaku[0] == 0:
              if card_in_yaku(card) == yaku[2]:
                distanceweightedbyscore = distanceweightedbyscore + self.get_distance_score(self.player.cards + [card], yaku[2])
          if (distanceweightedbyscore <  bestdistanceweightedbyscore):
            bestdistanceweightedbyscore = distanceweightedbyscore
            bestcard = (old, card)
    return bestcard

  def make_move_during(self, table, card):
    bestdistanceweightedbyscore = 100
    bestcard = table.cards[len(table.cards)-1]
    distanceweightedbyscore = 0
    olddistanceweightedbyscore = 0
    for yaku in self.player.get_yakus():
      if yaku[0] == 0:
        if card_in_yaku(card) == yaku[2]:
          distanceweightedbyscore = self.get_distance_score(self.player.cards + [card], yaku[2])
          olddistanceweightedbyscore = distanceweightedbyscore
    for tcard in table.cards:
        distanceweightedbyscore = olddistanceweightedbyscore
        if card.can_pick_up(tcard):
          for yaku in self.player.get_yakus():
            if yaku[0] == 0:
              if card_in_yaku(tcard) == yaku[2]:
                distanceweightedbyscore = distanceweightedbyscore + self.get_distance_score(self.player.cards + [tcard], yaku[2])
          if (distanceweightedbyscore <  bestdistanceweightedbyscore):
            bestdistanceweightedbyscore = distanceweightedbyscore
            bestcard = tcard
    return bestcard

  def koi_koi_decision(self, cards):
    return False