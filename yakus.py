def card_in_yaku(card):
    if card.family == 'Plain':
        return 'Kasu'
    elif card.family == 'Boar' or card.family == 'Butterfly' or card.family == 'Deer':
        return 'Tane,Ino-shika-cho'
    elif card.family == 'Rainman' or card.family == 'Bright':
        return 'Ame-Shiko,Shiko,Goko,Sanko'
    elif card.family == 'Poetry Ribbon' or card.family == 'Blue Ribbon' or card.family == 'Red Ribbon':
        return 'Aka-tan,Ao-tan,Tan'

def get_worth(cards):
    return kasu(cards)[0] + tane_ino_shika_cho(cards)[0] + ame_shiko_goko_sanko(cards)[0] + aka_ao_tan(cards)[0]

def get_distance(cards):
    return (kasu(cards), tane_ino_shika_cho(cards), ame_shiko_goko_sanko(cards), aka_ao_tan(cards))

def kasu(cards):
    score = 0
    for card in cards:
        if card.family == 'Plain':
            score = score + 1
    if score >= 10:
        return (score - 9, (0), 'Kasu')
    else:
        return (0, (score,), 'Kasu')

def tane_ino_shika_cho(cards):
    boardeerbutterfly = 0
    ani = 0
    for card in cards:
        if card.family == 'Boar' or card.family == 'Butterfly' or card.family == 'Deer':
            boardeerbutterfly = boardeerbutterfly + 1
        elif card.family == 'Animal':
            ani = ani + 1
    if boardeerbutterfly == 3:
        return (5 + ani, (0,), 'Ino-shika-cho')
    else:
        if ani + boardeerbutterfly >= 5:
            return (ani + boardeerbutterfly - 4, (0), 'Tane') 
        else:
            return (0, (boardeerbutterfly, ani), 'Tane,Ino-shika-cho')
        
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
            return (10 , (0,), 'Goko')
        elif brights == 3:
            return (7, (0,), 'Ame-Shiko')
        else:
            return (0, (rainman, brights), 'Ame-Shiko,Shiko,Goko,Sanko')
    else:
        if brights == 4:
            return (8, (0,), 'Shiko')
        elif brights == 3:
            return (6, (0,), 'Sanko')
        else:
            return (0, (rainman, brights), 'Ame-Shiko,Shiko,Goko,Sanko')

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
        return (10 + red, (0,), 'Aka-tan Ao-tan')
    elif poetry == 3:
        return (5 + blue + red, (0,), 'Aka-tan')
    elif blue == 3:
        return (5 + red + poetry, (0,), 'Ao-tan')
    elif blue + poetry + red >= 5:
        return (blue + poetry + red - 4, (0,), 'Tan')
    else: 
        return (0, (poetry, red, blue), 'Aka-tan,Ao-tan,Tan')



