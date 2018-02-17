from card import Card
import random

class Deck:
    deck = []

    def __init__(self):
        self.initialise_deck()
        random.shuffle(self.deck)

    def get_card(self):
        return self.deck.pop()
    
    def initialise_deck(self):
        self.deck.append(Card('January', 'Plain'))
        self.deck.append(Card('January', 'Plain'))
        self.deck.append(Card('January', 'Poetry Ribbon'))
        self.deck.append(Card('January', 'Bright'))
        self.deck.append(Card('February', 'Plain'))
        self.deck.append(Card('February', 'Plain'))
        self.deck.append(Card('February', 'Poetry Ribbon'))
        self.deck.append(Card('February', 'Animal'))
        self.deck.append(Card('March', 'Plain'))
        self.deck.append(Card('March', 'Plain'))
        self.deck.append(Card('March', 'Poetry Ribbon'))
        self.deck.append(Card('March', 'Bright'))
        self.deck.append(Card('April', 'Plain'))
        self.deck.append(Card('April', 'Plain'))
        self.deck.append(Card('April', 'Red Ribbon'))
        self.deck.append(Card('April', 'Animal'))
        self.deck.append(Card('May', 'Plain'))
        self.deck.append(Card('May', 'Plain'))
        self.deck.append(Card('May', 'Red Ribbon'))
        self.deck.append(Card('May', 'Animal'))
        self.deck.append(Card('June', 'Plain'))
        self.deck.append(Card('June', 'Plain'))
        self.deck.append(Card('June', 'Blue Ribbon'))
        self.deck.append(Card('June', 'Butterfly'))
        self.deck.append(Card('July', 'Plain'))
        self.deck.append(Card('July', 'Plain'))
        self.deck.append(Card('July', 'Red Ribbon'))
        self.deck.append(Card('July', 'Boar'))
        self.deck.append(Card('August', 'Plain'))
        self.deck.append(Card('August', 'Plain'))
        self.deck.append(Card('August', 'Animal'))
        self.deck.append(Card('August', 'Bright'))
        self.deck.append(Card('September', 'Plain'))
        self.deck.append(Card('September', 'Plain'))
        self.deck.append(Card('September', 'Blue Ribbon'))
        self.deck.append(Card('September', 'Bright'))
        self.deck.append(Card('October', 'Plain'))
        self.deck.append(Card('October', 'Plain'))
        self.deck.append(Card('October', 'Blue Ribbon'))
        self.deck.append(Card('October', 'Deer'))
        self.deck.append(Card('November', 'Plain'))
        self.deck.append(Card('November', 'Red Ribbon'))
        self.deck.append(Card('November', 'Animal'))
        self.deck.append(Card('November', 'Rain Man'))
        self.deck.append(Card('December', 'Plain'))
        self.deck.append(Card('December', 'Plain'))
        self.deck.append(Card('December', 'Plain'))
        self.deck.append(Card('December', 'Bright'))

