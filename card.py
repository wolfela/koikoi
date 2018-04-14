import pygame

class Card:

    def __init__(self, month, family, image, points):
        self.month = month
        self.family = family
        self.image = pygame.image.load(image)
        self.selectedimage = pygame.image.load('assets/cards/selected.png')
        self.unselectedimage = self.image
        self.pos = (0, 0)
        self.owner = None
        self.points = points

    def set_owner(self, owner):
        self.owner = owner

    def is_equal(self, month, family):
        if month == self.month and family == self.family:
            return True
        return False

    def can_pick_up(self, card):
        if card.month == self.month:
            return True
        return False

    def selected(self, board):
        self.image = self.selectedimage 
        board.blit(self.image, self.pos)

    def unselected(self, board):
        self.image = self.unselectedimage
        board.blit(self.image, self.pos)    
