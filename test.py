import random
import yakus
from card import Card
from deck import Deck

deck = Deck().deck
player_one = []
player_two = []
player_three = []
table = []

# for i in range(0, 4):
#     player_one.append(deck.pop())
#     player_one.append(deck.pop())
#     player_two.append(deck.pop())
#     player_two.append(deck.pop())
#     table.append(deck.pop())
#     table.append(deck.pop())

# Testing Plains Yakku
for i in range(0, 10):
    player_one.append(Card('January', 'Plain'))

if yakus.kasu(player_one) > 0:
    print('1: True')

player_one.pop()

if yakus.kasu(player_one) == 0:
    print('2: True')

for i in range(0, 3):
    player_one.append(Card('January', 'Plain'))

if yakus.kasu(player_one) == 3:
    print('3: True')

player_one.append(Card('January', 'NotPlain'))

if yakus.kasu(player_one) == 3:
    print('4: True')

# Testing Tane Yakus

for i in range(0, 5):
    player_two.append(Card('January', 'Animal'))

if yakus.tane_ino_shika_cho(player_two) == 1:
    print('5: True')

player_two.append(Card('January', 'Boar'))
player_two.append(Card('January', 'Deer'))
player_two.append(Card('January', 'Butterfly'))

if yakus.tane_ino_shika_cho(player_two) == 10:
    print('6: True')

player_two.pop()

if yakus.tane_ino_shika_cho(player_two) == 3:
    print('7: True')

# Testing Ame Shiko Goko Sanko 

for i in range(0, 4):
    player_three.append(Card('January', 'Bright'))

if yakus.ame_shiko_goko_sanko(player_three) == 8:
    print('8: True')

player_three.pop()

if yakus.ame_shiko_goko_sanko(player_three) == 6:
    print('9: True')

player_three.pop()

if yakus.ame_shiko_goko_sanko(player_three) == 0:
    print('10: True')

player_three.append(Card('January', 'Rainman'))
player_three.append(Card('January', 'Bright'))

if yakus.ame_shiko_goko_sanko(player_three) == 7:
    print('11: True')

player_three.append(Card('January', 'Bright'))

if yakus.ame_shiko_goko_sanko(player_three) == 10:
    print('12: True')

