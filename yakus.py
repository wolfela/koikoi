def get_worth(cards):
    return kasu(cards) + tane_ino_shika_cho(cards) + tane_ino_shika_cho(cards) + aka_ao_tan(cards)

def kasu(cards):
    score = 0
    for card in cards:
        if card.family == 'Plain':
            score = score + 1
    if score >= 10:
        return score - 9
    else:
        return 0

def tane_ino_shika_cho(cards):
    boardeerbutterfly = 0
    ani = 0
    for card in cards:
        if card.family == 'Boar' or card.family == 'Butterfly' or card.family == 'Deer':
            boardeerbutterfly = boardeerbutterfly + 1
        elif card.family == 'Animal':
            ani = ani + 1
    if boardeerbutterfly == 3:
        return 5 + ani
    else:
        if ani + boardeerbutterfly >= 5:
            return ani + boardeerbutterfly - 4 
        else:
            return 0
        
def ame_shiko_goko_sanko(cards):
    rainman = 0
    brights = 0
    for card in cards:
        if card.family == 'Rainman':
            rainman = rainman + 1
        elif card.family == 'Bright':
            brights = brights + 1
    if rainman == 1:
        if rainman + brights == 5:
            return 10
        elif brights == 3:
            return 7
        else:
            return 0
    else:
        if brights == 4:
            return 8
        elif brights == 3:
            return 6
        else:
            return 0

def aka_ao_tan(cards):
    poetry = 0
    blue = 0
    red = 0
    for card in cards:
        if card.family == 'Poetry Ribbon':
            poetry = poetry + 1
        elif card.family == 'Blue Ribbon':
            blue = blue + 1
        elif card.family == 'Red Ribbon':
            red = red + 1
    if poetry == 3 and blue == 3:
        return 10 + red
    elif poetry == 3:
        return 5 + blue + red
    elif blue == 3:
        return 5 + red + poetry
    elif blue + poetry + red >= 5:
        return blue + poetry + red - 4
    else: 
        return 0



