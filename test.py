import random
import yakus
from card import Card
from deck import Deck
import unittest

class YakuTests(unittest.TestCase):

    def test(self):
        player_one = []
        player_two = []
        player_three = []

        # Testing Plains Yakku
        for i in range(0, 10):
            player_one.append(Card('January', 'Plain', 'assets/cards/july_boar.jpg', 0))

        self.assertEqual(yakus.kasu(player_one)[0], 1)

        player_one.pop()

        self.assertEqual(yakus.kasu(player_one)[0], 0)

        for i in range(0, 3):
            player_one.append(Card('January', 'Plain', 'assets/cards/july_boar.jpg', 0))

        self.assertEqual(yakus.kasu(player_one)[0], 3)

        player_one.append(Card('January', 'NotPlain', 'assets/cards/july_boar.jpg', 0))

        self.assertEqual(yakus.kasu(player_one)[0], 3) 

        # Testing Tane Yakus

        for i in range(0, 5):
            player_two.append(Card('January', 'Animal', 'assets/cards/july_boar.jpg', 0))

        self.assertEqual(yakus.tane_ino_shika_cho(player_two)[0], 1)

        player_two.append(Card('January', 'Boar', 'assets/cards/july_boar.jpg', 0))
        player_two.append(Card('January', 'Deer', 'assets/cards/july_boar.jpg', 0))
        player_two.append(Card('January', 'Butterfly', 'assets/cards/july_boar.jpg', 0))

        self.assertEqual(yakus.tane_ino_shika_cho(player_two)[0], 10)

        player_two.pop()

        self.assertEqual(yakus.tane_ino_shika_cho(player_two)[0], 3)

        # Testing Ame Shiko Goko Sanko 

        for i in range(0, 4):
            player_three.append(Card('January', 'Bright', 'assets/cards/july_boar.jpg', 0))

        self.assertEqual(yakus.ame_shiko_goko_sanko(player_three)[0], 8)

        player_three.pop()

        self.assertEqual(yakus.ame_shiko_goko_sanko(player_three)[0], 6)
        
        player_three.pop()

        self.assertEqual(yakus.ame_shiko_goko_sanko(player_three)[0], 0)

        player_three.append(Card('January', 'Rainman', 'assets/cards/july_boar.jpg', 0))
        player_three.append(Card('January', 'Bright', 'assets/cards/july_boar.jpg', 0))

        self.assertEqual(yakus.ame_shiko_goko_sanko(player_three)[0], 7)

        player_three.append(Card('January', 'Bright', 'assets/cards/july_boar.jpg', 0))

        self.assertEqual(yakus.ame_shiko_goko_sanko(player_three)[0], 10)

test = YakuTests()
test.test()

