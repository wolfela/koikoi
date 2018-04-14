import pygame
from deck import Deck
from player import Player
from card import Card
from ai import RandomAi, PointsAi, HeuristicAi, PHeuristicAi, WHeuristicAi

pygame.init()

# Variables used for GUI
background = pygame.image.load('assets/background.jpeg')
backgroundRect = background.get_rect()
board = pygame.image.load('assets/board.png')
boardRect = board.get_rect()
size = (width, height) = background.get_size()
boardsize = (width, height) = board.get_size()
gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption('Koi Koi')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 25)
lastmoves = ['', '', '', '']
pvpbutton = pygame.Rect(50, 200, 50, 50)
randomAiButton = pygame.Rect(200, 200, 50, 50)
pointsAiButton = pygame.Rect(200, 300, 50, 50)
heuristicAiButton = pygame.Rect(200, 400, 50, 50)
PheuristicAiButton = pygame.Rect(200, 500, 50, 50)
WheuristicAiButton = pygame.Rect(200, 600, 50, 50)
randomAiButtonvAi = pygame.Rect(350, 200, 50, 50)
pointsAiButtonvAi = pygame.Rect(350, 300, 50, 50)
heuristicAiButtonvAi = pygame.Rect(350, 400, 50, 50)
PheuristicAiButtonvAi = pygame.Rect(350, 500, 50, 50)
WheuristicAiButtonvAi = pygame.Rect(350, 600, 50, 50)
yesbutton = pygame.Rect(1000, 420, 50, 50)
nobutton = pygame.Rect(1100, 420, 50, 50)

# Flags for Controlling Game Flow
duringturn = False
crashed = False
started = False
finished = False
kk = False
turn = True
winningplayer = None
ai = False
aivsai = False
deckcard = None
secondchoice = False
evaluationwins = []
evaluationcounter = 0

# Create Player Variables 
player_one = Player('player_one', [])
player_two = Player('player_two', [])
table = Player('table', [])
deck = Deck().deck
selected = []

# Decide on AI type
randomAi = RandomAi(player_one)
pointsAi = PointsAi(player_one)
heuristicAi = HeuristicAi(player_one)
PheuristicAi = PHeuristicAi(player_one)
WheuristicAi = WHeuristicAi(player_one)
randomAi2 = RandomAi(player_two)
pointsAi2 = PointsAi(player_two)
heuristicAi2 = HeuristicAi(player_two)
PheuristicAi2 = PHeuristicAi(player_two)
WheuristicAi2 = WHeuristicAi(player_two)
aiplayer = None
aiplayer2 = None
aiplayertype = None
aiplayer2type = None

def evaluate():
    file = open('evaulationdata.csv', 'w')
    file.write('Player 1 is ')
    file.write(str(aiplayertype) + '\n')
    file.write('Player 2 is ') 
    file.write(str(aiplayer2type) + '\n')
    for result in evaluationwins:
        for i, ele in enumerate(result):
            if i == 0:
                file.write(str(ele) + ',')
            else:
                file.write(str(ele) + '\n') 
    file.close()


# Deal Cards to Players
def deal_cards():
    global deck, player_one, player_two
    for i in range(0, 4):
        card = deck.pop()
        card.set_owner(player_one)
        player_one.add_card(card)
        card = deck.pop()
        card.set_owner(player_one)
        player_one.add_card(card)
        card = deck.pop()
        card.set_owner(player_two)
        player_two.add_card(card)
        card = deck.pop()
        card.set_owner(player_two)
        player_two.add_card(card)
        card = deck.pop()
        card.set_owner(table)
        table.add_card(card)
        card = deck.pop()
        card.set_owner(table)
        table.add_card(card)
    # Add extra blank card so that players can put down cards 
    table.add_card(Card('blank', 'blank', 'assets/cards/blank.png', 0))


deal_cards()
# Updates the board to reflect the current state of the players and table
def get_cards():
    # Clears the board
    gameDisplay.blit(background, backgroundRect)
    gameDisplay.blit(board, ((size[0] - boardsize[0])/2, (size[1] - boardsize[1])/2))

    # Renders the last four moves made
    gameDisplay.blit(font.render(lastmoves[len(lastmoves)-1], True, (255,0,0)), (800, 400))
    gameDisplay.blit(font.render(lastmoves[len(lastmoves)-2], True, (255,0,0)), (800, 420))
    gameDisplay.blit(font.render(lastmoves[len(lastmoves)-3], True, (255,0,0)), (800, 440))
    gameDisplay.blit(font.render(lastmoves[len(lastmoves)-4], True, (255,0,0)), (800, 460))

    # Renders each players and the tables cards
    offsetx = 150
    for card in player_one.cards:
        cardimage = card.image
        gameDisplay.blit(cardimage, (offsetx, 130))
        card.pos = (offsetx, 130)
        offsetx = offsetx + cardimage.get_size()[0]

    offsetx = 150
    i = 0
    for card in table.cards:
        if (i % 2 == 0):
            cardimage = card.image
            gameDisplay.blit(cardimage, (offsetx, 280))
            card.pos = (offsetx, 280)
            offsetx = offsetx + cardimage.get_size()[0]
            i = i + 1
            offsetx = offsetx - cardimage.get_size()[0]
        else:
            cardimage = card.image
            gameDisplay.blit(cardimage, (offsetx, 380))
            card.pos = (offsetx, 380)
            offsetx = offsetx + cardimage.get_size()[0]
            i = i + 1

    offsetx = 150
    for card in player_two.cards:
        cardimage = card.image
        gameDisplay.blit(cardimage, (offsetx, 540))
        card.pos = (offsetx, 540)
        offsetx = offsetx + cardimage.get_size()[0]

    # Renders cards already picked up by the players
    offsetx = 50
    for card in player_one.pickedup:
        cardimage = card.image
        gameDisplay.blit(cardimage, (offsetx, 20))
        card.pos = (offsetx, 20)
        offsetx = offsetx + cardimage.get_size()[0]

    offsetx = 50
    for card in player_two.pickedup:
        cardimage = card.image
        gameDisplay.blit(cardimage, (offsetx, 660))
        card.pos = (offsetx, 660)
        offsetx = offsetx + cardimage.get_size()[0]

    # Renders blank card back for the deck 
    gameDisplay.blit(pygame.image.load('assets/cards/back.png'), (50, 130))

    # Tells us whos turn it is 
    if turn: 
        gameDisplay.blit(font.render('Player One Turn!', True, (255,0,0)), (800, 600))
    else:
        gameDisplay.blit(font.render('Player Two Turn!', True, (255,0,0)), (800, 600))

# Gets a random card from the deck
def get_deck_card():
    card = deck.pop(0)
    cardimage = card.image
    render_deck_card(cardimage)
    return card

# Renders the deck card in the right position
def render_deck_card(cardimage):
    gameDisplay.blit(cardimage, (50, 130))

# Selects a card in the current players hand
def player_select(card):
    global selected
    movedrec = card.image.get_rect().move(card.pos)
    if movedrec.collidepoint(mouse_pos):
        if len(selected) == 0:
            card.selected(gameDisplay)
            selected.append(card)
        elif len(selected) >= 1:
            for old in selected:
                old.unselected(gameDisplay)
            selected = []
            card.selected(gameDisplay)
            selected.append(card)

# Handles a player getting a yaku
def koikoi(player, during):
    # Ensure we are using the global versions of these variables
    global kk 
    global duringturn
    global winningplayer
    global finished
    global evaluationwins, evaluationcounter, player_one, player_two, deck, selected, table, turn, aiplayer, aiplayer2
    finished = True
    kk = True
    duringturn = during
    winningplayer = player

    # Clear the board before the text is displayed
    gameDisplay.blit(background, backgroundRect)
    gameDisplay.blit(board, ((size[0] - boardsize[0])/2, (size[1] - boardsize[1])/2))

    # If a human player got a yaku ask them what they wish to do 
    if (not ai and not aivsai) or (ai and winningplayer.name is 'player_one'):
        finished = False
        gameDisplay.blit(font.render(player.name + ' you have a yaku! Do you want to Koi Koi?', True, (255,0,0)), (800, 400))
        gameDisplay.blit(font.render('You got: ', True, (255, 0, 0)), (800, 426))
        yoffset = 26
        for result in winningplayer.get_yakus():
            if result[0] > 0:
                gameDisplay.blit(font.render(result[2], True, (255, 0, 0)), (800, 426 + yoffset))
                yoffset = yoffset + 26
        pygame.draw.rect(gameDisplay, [0, 255, 0], yesbutton)
        pygame.draw.rect(gameDisplay, [255, 0, 0], nobutton)

    # If ai got a yaku, call their internal decision logic
    elif ai:
        end_game()

    elif aivsai and evaluationcounter < 1000:
        evaluationwins.append((winningplayer.name, winningplayer.score))
        evaluationcounter = evaluationcounter + 1
        print(evaluationcounter)
        player_one = Player('player_one', [])
        player_two = Player('player_two', [])
        aiplayer = aiplayertype(player_one)
        aiplayer2 = aiplayer2type(player_two)
        table = Player('table', [])
        deck = Deck().deck
        selected = []
        finished = False
        turn = True
        duringturn = False
        deal_cards()
        start_game()
    
    elif aivsai and evaluationcounter == 1000:
        end_game()
        evaluate()

# Clears the board, displays the winner and renders the last four moves
def end_game():
    global finished
    global lastmoves
    global font
    finished = True
    gameDisplay.blit(background, backgroundRect)
    gameDisplay.blit(board, ((size[0] - boardsize[0])/2, (size[1] - boardsize[1])/2))
    gameDisplay.blit(font.render(lastmoves[len(lastmoves)-1], True, (255,0,0)), (800, 400))
    gameDisplay.blit(font.render(lastmoves[len(lastmoves)-2], True, (255,0,0)), (800, 420))
    gameDisplay.blit(font.render(lastmoves[len(lastmoves)-3], True, (255,0,0)), (800, 440))
    gameDisplay.blit(font.render(lastmoves[len(lastmoves)-4], True, (255,0,0)), (800, 460))
    gameDisplay.blit(font.render(winningplayer.name + ' you win with ' + str(winningplayer.score) + ' points!', True, (255,0,0)), (400, 400))
    gameDisplay.blit(font.render('You got: ', True, (255, 0, 0)), (400, 600))
    yoffset = 26
    for result in winningplayer.get_yakus():
        if result[0] > 0:
            gameDisplay.blit(font.render(result[2], True, (255, 0, 0)), (400, 600 + yoffset))
            yoffset = yoffset + 26
    
# Main logic of the game play.
def table_loop(card):
    global selected
    global duringturn
    global turn
    global table
    global deckcard
    global lastmoves
    if len(selected) >= 1:
        old = selected[0]
        old.unselected(gameDisplay)
        selected = []
        if (old.owner != None):
            if (old.owner != table):
                if (card.month == 'blank'):
                    table.put_down(card)
                    player = old.owner
                    old.owner.put_down(old)
                    table.add_card(old)
                    table.add_card(card)
                    lastmoves.append(player.name + ' put down ' + old.month + ' ' + old.family)
                    if (player.check_yakus() > player.oldscore):
                        player.score = player.oldscore
                        koikoi(player, True)
                        return 
                    duringturn = True
                    get_cards()
                    deckcard = get_deck_card()
                    selected = [deckcard]
                elif (old.can_pick_up(card)):
                    card.owner.put_down(card)
                    old.owner.pick_up(card)
                    old.owner.pick_up(old)
                    player = old.owner
                    old.owner.put_down(old)
                    lastmoves.append(player.name + ' picked up ' + old.month + ' ' + old.family + ' and ' + card.month + ' ' + card.family)
                    if (player.check_yakus() > player.oldscore):
                        player.oldscore = player.score
                        koikoi(player, True)
                        return
                    duringturn = True
                    get_cards()
                    deckcard = get_deck_card()
                    selected = [deckcard]
        else:
            selected = []
            if card.month == 'blank':
                table.put_down(card)
                table.add_card(old)
                table.add_card(card)
                if turn:
                    lastmoves.append(player_one.name + ' put down ' + old.month + ' ' + old.family)
                    if (player_one.check_yakus() > player_one.oldscore):
                        player_one.oldscore = player_one.score
                        koikoi(player_one, False)
                        return
                else:
                    lastmoves.append(player_two.name + ' put down ' + old.month + ' ' + old.family)
                    if (player_two.check_yakus() > player_two.oldscore):
                        player_two.oldscore = player_two.score
                        koikoi(player_two, False)
                        return
                duringturn = False
                turn = not turn
                get_cards()
            elif old.can_pick_up(card):
                if turn:
                    player_one.pick_up(card)
                    player_one.pick_up(old)
                    table.put_down(card)
                    lastmoves.append(player_one.name + ' picked up ' + old.month + ' ' + old.family + ' and ' + card.month + ' ' + card.family)
                    if (player_one.check_yakus() > player_one.oldscore):
                        player_one.oldscore = player_one.score
                        koikoi(player_one, False)
                        return
                else:
                    player_two.pick_up(card)
                    player_two.pick_up(old)
                    table.put_down(card)
                    lastmoves.append(player_two.name + ' picked up ' + old.month + ' ' + old.family + ' and ' + card.month + ' ' + card.family)
                    if (player_two.check_yakus() > player_two.oldscore):
                        player_two.oldscore = player_two.score
                        koikoi(player_two, False)
                        return
                duringturn = False
                turn = not turn
                get_cards()
            else:
                get_cards()
                selected = [deckcard]
                render_deck_card(deckcard.image)

def select_second_ai():
    global secondchoice
    secondchoice = True
    gameDisplay.blit(background, backgroundRect)
    gameDisplay.blit(board, ((size[0] - boardsize[0])/2, (size[1] - boardsize[1])/2))
    gameDisplay.blit(font.render('Random Ai', True, (255,0,0)), (300, 180))
    pygame.draw.rect(gameDisplay, [0, 0, 255], randomAiButtonvAi)
    gameDisplay.blit(font.render('Points Ai', True, (255,0,0)), (300, 280))
    pygame.draw.rect(gameDisplay, [0, 0, 255], pointsAiButtonvAi)
    gameDisplay.blit(font.render('Unweighted Ai', True, (255,0,0)), (300, 380))
    pygame.draw.rect(gameDisplay, [0, 0, 255], heuristicAiButtonvAi)
    gameDisplay.blit(font.render('Probabilistic Ai', True, (255,0,0)), (300, 480))
    pygame.draw.rect(gameDisplay, [0, 0, 255], PheuristicAiButtonvAi)
    gameDisplay.blit(font.render('Strength Ai', True, (255,0,0)), (300, 580))
    pygame.draw.rect(gameDisplay, [0, 0, 255], WheuristicAiButtonvAi)

def start_game():
    global started
    gameDisplay.blit(background, backgroundRect)
    gameDisplay.blit(board, ((size[0] - boardsize[0])/2, (size[1] - boardsize[1])/2))
    get_cards()
    started = True

# Initialise the game state
gameDisplay.blit(background, backgroundRect)
gameDisplay.blit(board, ((size[0] - boardsize[0])/2, (size[1] - boardsize[1])/2))
gameDisplay.blit(font.render('Player Vs Player', True, (255,0,0)), (50, 180))
pygame.draw.rect(gameDisplay, [255, 0, 0], pvpbutton)

gameDisplay.blit(font.render('Player Vs Ai', True, (255,0,0)), (200, 120))
gameDisplay.blit(font.render('Random Ai', True, (255,0,0)), (200, 180))
pygame.draw.rect(gameDisplay, [0, 255, 0], randomAiButton)
gameDisplay.blit(font.render('Points Ai', True, (255,0,0)), (200, 280))
pygame.draw.rect(gameDisplay, [0, 255, 0], pointsAiButton)
gameDisplay.blit(font.render('Heuristic Ai', True, (255,0,0)), (200, 380))
pygame.draw.rect(gameDisplay, [0, 255, 0], heuristicAiButton)
gameDisplay.blit(font.render('Probabilistic Ai', True, (255,0,0)), (200, 480))
pygame.draw.rect(gameDisplay, [0, 255, 0], PheuristicAiButton)
gameDisplay.blit(font.render('Strength Ai', True, (255,0,0)), (200, 580))
pygame.draw.rect(gameDisplay, [0, 255, 0], WheuristicAiButton)

gameDisplay.blit(font.render('Ai Vs Ai', True, (255,0,0)), (350, 120))
gameDisplay.blit(font.render('Random Ai', True, (255,0,0)), (350, 180))
pygame.draw.rect(gameDisplay, [0, 0, 255], randomAiButtonvAi)
gameDisplay.blit(font.render('Points Ai', True, (255,0,0)), (350, 280))
pygame.draw.rect(gameDisplay, [0, 0, 255], pointsAiButtonvAi)
gameDisplay.blit(font.render('Unweighted Ai', True, (255,0,0)), (350, 380))
pygame.draw.rect(gameDisplay, [0, 0, 255], heuristicAiButtonvAi)
gameDisplay.blit(font.render('Probabilistic Ai', True, (255,0,0)), (350, 480))
pygame.draw.rect(gameDisplay, [0, 0, 255], PheuristicAiButtonvAi)
gameDisplay.blit(font.render('Strength Ai', True, (255,0,0)), (350, 580))
pygame.draw.rect(gameDisplay, [0, 0, 255], WheuristicAiButtonvAi)


# Main game loop 
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and not finished:
            mouse_pos = event.pos 

            # Checks which game state was selected, PvP or AI
            if not started:
                if pvpbutton.collidepoint(mouse_pos):
                    start_game()
                elif (randomAiButton.collidepoint(mouse_pos)):
                    aiplayer = randomAi2
                    ai = True
                    start_game()
                elif (pointsAiButton.collidepoint(mouse_pos)):
                    aiplayer = pointsAi2
                    ai = True   
                    start_game()      
                elif (heuristicAiButton.collidepoint(mouse_pos)):
                    aiplayer = heuristicAi2
                    ai = True   
                    start_game()
                elif (PheuristicAiButton.collidepoint(mouse_pos)):
                    aiplayer = PheuristicAi2
                    ai = True   
                    start_game()
                elif (WheuristicAiButton.collidepoint(mouse_pos)):
                    aiplayer = WheuristicAi2
                    ai = True   
                    start_game()
                if not secondchoice:   
                    if (randomAiButtonvAi.collidepoint(mouse_pos)):
                        aiplayer = randomAi
                        aiplayertype = RandomAi
                        select_second_ai()
                    elif (pointsAiButtonvAi.collidepoint(mouse_pos)):
                        aiplayer = pointsAi   
                        aiplayertype = PointsAi
                        select_second_ai()   
                    elif (heuristicAiButtonvAi.collidepoint(mouse_pos)):
                        aiplayer = heuristicAi
                        aiplayertype = HeuristicAi  
                        select_second_ai()
                    elif (PheuristicAiButtonvAi.collidepoint(mouse_pos)):
                        aiplayer = PheuristicAi
                        aiplayertype = PHeuristicAi  
                        select_second_ai()
                    elif (WheuristicAiButtonvAi.collidepoint(mouse_pos)):
                        aiplayer = WheuristicAi
                        aiplayertype = WHeuristicAi  
                        select_second_ai()
                elif secondchoice:
                    if (randomAiButtonvAi.collidepoint(mouse_pos)):
                        aiplayer2 = randomAi2
                        aiplayer2type = RandomAi
                        start_game() 
                        aivsai = True 
                    elif (pointsAiButtonvAi.collidepoint(mouse_pos)):
                        aiplayer2 = pointsAi2
                        aiplayer2type = PointsAi
                        start_game()
                        aivsai = True 
                    elif (heuristicAiButtonvAi.collidepoint(mouse_pos)):
                        aiplayer2 = heuristicAi2
                        aiplayer2type = HeuristicAi
                        start_game()      
                        aivsai = True  
                    elif (PheuristicAiButtonvAi.collidepoint(mouse_pos)):
                        aiplayer2 = PheuristicAi2
                        aiplayer2type = PHeuristicAi
                        start_game()      
                        aivsai = True  
                    elif (WheuristicAiButtonvAi.collidepoint(mouse_pos)):
                        aiplayer2 = WheuristicAi2
                        aiplayer2type = WHeuristicAi
                        start_game()      
                        aivsai = True  

            # Checks whether Koi Koi was called or not
            if yesbutton.collidepoint(mouse_pos) and kk:
                kk = False
                if not duringturn:
                    turn = not turn
                    get_cards()
                else:
                    get_cards()
                    deckcard = get_deck_card()
                    selected = [deckcard]

            if nobutton.collidepoint(mouse_pos) and kk:
                end_game()
            
            # Checks each card in the current players hand and sees if it has been clicked, then selects them
            # Since there will always only be two players, we can use a binary turn variable, True being player one and False player two
            # duringturn indicates whether the player is picking up with a card in their hand or the random deck card
            if turn and not duringturn:
                for card in player_one.cards:
                    movedrec = card.image.get_rect().move(card.pos)
                    if movedrec.collidepoint(mouse_pos):
                        player_select(card)
            
            # Checks if a card on the table has been selected; this is irrelevant of the turn
            for card in table.cards:
                movedrec = card.image.get_rect().move(card.pos)
                if movedrec.collidepoint(mouse_pos):
                    table_loop(card) 

            if not turn and not duringturn and not ai:
                for card in player_two.cards:
                    movedrec = card.image.get_rect().move(card.pos)
                    if movedrec.collidepoint(mouse_pos):
                        player_select(card)

        if event.type == pygame.QUIT:
            crashed = True

    # If both players have no cards, its a draw
    if not finished:
            if (len(player_one.cards) + len(player_two.cards) == 0) or len(table.cards) == 0:
                if not aivsai:
                    finished = True
                    gameDisplay.blit(background, backgroundRect)
                    gameDisplay.blit(board, ((size[0] - boardsize[0])/2, (size[1] - boardsize[1])/2))
                    gameDisplay.blit(font.render(lastmoves[len(lastmoves)-1], True, (255,0,0)), (800, 400))
                    gameDisplay.blit(font.render(lastmoves[len(lastmoves)-2], True, (255,0,0)), (800, 420))
                    gameDisplay.blit(font.render(lastmoves[len(lastmoves)-3], True, (255,0,0)), (800, 440))
                    gameDisplay.blit(font.render(lastmoves[len(lastmoves)-4], True, (255,0,0)), (800, 460))
                    gameDisplay.blit(font.render('Draw!', True, (255,0,0)), (600,600))
                else:
                    if aivsai and evaluationcounter < 1000:
                        evaluationwins.append(('Draw', 0))
                        evaluationcounter = evaluationcounter + 1
                        print(evaluationcounter)
                        player_one = Player('player_one', [])
                        player_two = Player('player_two', [])
                        aiplayer = aiplayertype(player_one)
                        aiplayer2 = aiplayer2type(player_two)
                        table = Player('table', [])
                        deck = Deck().deck
                        selected = []
                        finished = False
                        turn = True
                        duringturn = False
                        deal_cards()
                        start_game()
                    elif aivsai and evaluationcounter == 1000:
                        finished = True
                        gameDisplay.blit(background, backgroundRect)
                        gameDisplay.blit(board, ((size[0] - boardsize[0])/2, (size[1] - boardsize[1])/2))
                        gameDisplay.blit(font.render(lastmoves[len(lastmoves)-1], True, (255,0,0)), (800, 400))
                        gameDisplay.blit(font.render(lastmoves[len(lastmoves)-2], True, (255,0,0)), (800, 420))
                        gameDisplay.blit(font.render(lastmoves[len(lastmoves)-3], True, (255,0,0)), (800, 440))
                        gameDisplay.blit(font.render(lastmoves[len(lastmoves)-4], True, (255,0,0)), (800, 460))
                        gameDisplay.blit(font.render('Draw!', True, (255,0,0)), (600,600))
                        evaluate()

    # If its player twos turn and ai has been abled, call the aiplayer logic
    if not finished and ai:
        if not turn and not duringturn:
            move = aiplayer.make_move(table)
            selected = [move[0]]
            table_loop(move[1])

        if not turn and duringturn:
            move = aiplayer.make_move_during(table, deckcard)
            selected = [deckcard]
            table_loop(move)

    # If the game is aivsai, call ai logic for both turns
    if not finished and aivsai:
        if turn:
            if not duringturn:
                move = aiplayer.make_move(table)
                selected = [move[0]]
                table_loop(move[1])

            if duringturn:
                move = aiplayer.make_move_during(table, deckcard)
                selected = [deckcard]
                table_loop(move)

        elif not turn:
            if not duringturn:
                move = aiplayer2.make_move(table)
                selected = [move[0]]
                table_loop(move[1])

            if duringturn:
                move = aiplayer2.make_move_during(table, deckcard)
                selected = [deckcard]
                table_loop(move)

    pygame.display.update()
    clock.tick(60)