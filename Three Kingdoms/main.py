import random
from card import Card
from player import Player
deck = []
dump = []

for i in range (30):
    deck.append(Card('ATT'))
for i in range (15):
    deck.append(Card('DOD'))
for i in range (8):
    deck.append(Card('PEA'))

players = [Player("TY", 0, False), Player("AI", 1, True)];

done = False
turn = 0
playerNum = 2

def gameOver():
    for i in range (playerNum):
        if players[i].curHealth <= 0:
            return True;
    return False;
def nextTurn():
    global turn
    turn = turn + 1 
    turn = turn % playerNum

def drawCards(player, num):
    for i in range (num):
        global deck, dump;
        if deck == []:
            deck = dump[:]
            dump = []
        c = random.choice(deck)
        player.hand.append(c)

def respondAttack(player):
    if not Card("DOD") in player.hand:
        print('No dodge. Health - 1')  
        return
    
    decision = input('You are under attack! Would you like to dodge?')
    if decision == 'y':
        print('Dodged')
        player.hands.remove(Card("Dodge"))
    else: 
        player.curHealth -= 1;

def displayCards(player):
    print(player.name, end='')
    print(', you have these cards:')
    for i in range (len(player.hand)):
        print (player.hand[i].full_name,end=' ')
    print()

def playCards(player):
    displayCards(player)
    done = False; 
    while not done:
        str = input('Which card would you like to play?\n')
        if str == "done":
            break

        curCard = player.hand[int(str)]
        if curCard.short_name == "PEA":
            if player.curHealth == player.maxHealth:
                print('You cannot use Peach when you are at max health!')
                continue
            else:
                player.curHealth = player.curHealth + 1;
        elif curCard.short_name == "ATT":
            player.hand.remove(curCard)
            respondAttack(players[(turn+1)%2])
        else:
            print('Please enter a valid card to play!')

def discardCards(player):
    if player.curHealth >= len(player.hand):
        return
    else:
        displayCards(player)
        
        while (player.curHealth < len(player.hand)):
            print('Please discard cards')
            c = int(input());
            player.hand.remove(player.hand[c])

def initGame():
    for i in range (playerNum):
        drawCards(players[i], 4)
        displayCards(players[i])

initGame()

while not gameOver():
    drawCards(players[turn], 2);
    displayCards(players[turn]);
    playCards(players[turn]);
    discardCards(players[turn]);
    nextTurn();
