'''
This is a simple blackjack game.
'''
import random
from time import sleep
from CardStock import deck

class BankRoll():
    '''
    This class is the user's bank account.
    '''
    def __init__(self):
        self.balance = 100
        print('A complimentary account has been created with the casino.  \
You have a balance of: {}'.format(self.balance))
    def wager(self,wager):
        '''
        This manages the wager set by the user.
        '''
        if wager > self.balance:
            print('You have overdrafted your account.  Your bank charges you $30.')
            self.balance -= 30
        self.balance -= wager
    def wager_win(self,wager):
        '''
        This handles it when the user manages to win.
        '''
        print()
        print('Your winnings have been deposited to your account.')
        self.balance += wager * 2
    def wager_tie(self,wager):
        '''
        This handles wagers when there is a tie.
        '''
        print()
        print('Your wager has been returned to your account.')
        self.balance += wager

def hand_total(hand):
    '''
    This function determines how aces function.
    '''

    aces_in_hand = 0
    hand_value = 0

    for _ in hand:
        if _.value != 'ace':
            hand_value += _.value
        elif _.value == 'ace':
            aces_in_hand += 1

    hand_value += aces_in_hand
    for _ in range(0,aces_in_hand):
        if hand_value < 51:
            hand_value += 10
        else:
            pass
    return hand_value

def populate_deck():
    '''
    This function populates the deck of cards.
    '''
    print('Unpacking fresh deck:')

    cardlist = ['Two','Three','Four','Five','Six','Seven','Eight',\
'Nine','Ten','Jack','Queen','King','Ace']
    suitlist = ['Hearts','Spades','Diamonds','Clubs']
    allcards = []

    value = 2
    nalue = 1


    for suit in suitlist:
        for card in cardlist:
            if value == 1:
                value = 'ace'
            name = ('{}_{}'.format(card.lower(),suit.lower()))
            allcards.append(deck.Card(suit,card,value,name))
            if value == 'ace':
                value = 1
            value += 1
            if value == 11:
                nalue += 1
                value = 10
            if nalue == 5:
                value = 1
                nalue = 1
    return allcards


def player_turn_fun(allcards,player_hand,dealer_hand):
    '''
    This defines the player's turn, showing that one can pass variables all over the place.
    '''
    while True:


        p_hand_value = hand_total(player_hand)
#       print ('\n'*100)
#        print(p_hand_value)
        d_hand_value = hand_total(dealer_hand)
#        print(d_hand_value)

        print('Dealer Hand:')
        deck.c_spool(dealer_hand,False)
        print('\n'*10)
        print('Player Hand:')
        deck.c_spool(player_hand,True)

        if p_hand_value > 21:
            print('Bust!  You have more than 21.')
            break

        hit_me = input('Would you like to (h)it or (s)tay?  ')
        if hit_me.lower() == 'h' or hit_me.lower() == 'hit':
            player_hand.append(allcards.pop())
        elif hit_me.lower() == 's' or hit_me.lower() == 'stay':
            break

    return (allcards,player_hand,p_hand_value)




def dealer_turn_fun(allcards,player_hand,dealer_hand):
    '''
    This defines the dealer's turn.
    '''
    while True:
        p_hand_value = hand_total(player_hand)
#       print ('\n'*100)
        print(p_hand_value)
        d_hand_value = hand_total(dealer_hand)
        print(d_hand_value)

        print('Dealer Hand:')
        deck.c_spool(dealer_hand,True)
        print('\n'*10)
        print('Player Hand:')
        deck.c_spool(player_hand,True)

        if p_hand_value > 21:
            break
        if d_hand_value > 21:
            break

        if d_hand_value < p_hand_value and d_hand_value < 22:
            hit_me = 'hit'
        elif d_hand_value > p_hand_value or d_hand_value == 21:
            hit_me = 'stay'
        elif d_hand_value == p_hand_value and d_hand_value < 21:
            hit_me = 'hit'

        if hit_me.lower() == 'h' or hit_me.lower() == 'hit':
            dealer_hand.append(allcards.pop())
        elif hit_me.lower() == 's' or hit_me.lower() == 'stay':
            break
        sleep(1)
    return (allcards,dealer_hand,d_hand_value)



def primary_function():
    '''
    This is the function that spawns all functions.
    '''
    # print('\n' * 100)
    player_account = BankRoll()
    game_number = 0
    games_lost = 0
    while True:
        begin_var = input('Would you like to play BlackJack?  (Y/n):  ')
        if begin_var.lower() != "y" and begin_var.lower() != "yes":
            if game_number < 1:
                print('You haven\'t played a single game, yet!  You obviously meant to type "y".')
                continue
            print('Maybe you will be luckier next time...  But probably not.')
            break
        print('Your current balance is:  {}'.format(player_account.balance))
        requested_wager = int(input('How much would you like to wager?  '))
        player_account.wager(requested_wager)
        games_tally = games_lost
        games_lost,tie = begin_game(games_lost)
        if tie is True:
            player_account.wager_tie(requested_wager)
        elif tie is False and games_tally == games_lost:
            player_account.wager_win(requested_wager)
        print()
    #    print('\n' * 100)
        game_number += 1
        print('You have played:  {} games.  You have won: \
{} and lost {}.'.format(game_number,game_number - games_lost,games_lost))




def begin_game(_games_lost):
    '''
    This begins the game, sets the stage for hands, etc.
    '''
    _tie = False
    allcards = populate_deck()
    print('Game initializing.')
    # Everyday I'm shuffling.
    random.shuffle(allcards)

    print('The deck has been unpacked and shuffled.')
#    for _ in allcards:
#        print(_.name)

    # Sets initial hands:

    dealer_hand = []
    dealer_hand.append(allcards.pop())
    dealer_hand.append(allcards.pop())

    player_hand = []
    player_hand.append(allcards.pop())
    player_hand.append(allcards.pop())

    allcards,player_hand,p_hand_value = player_turn_fun(allcards,player_hand,dealer_hand)
    allcards,dealer_hand,d_hand_value = dealer_turn_fun(allcards,player_hand,dealer_hand)
    if p_hand_value > 21:
        print('You lose.')
        _games_lost += 1
    elif d_hand_value > 21:
        print('You win.  Somehow.')
    elif d_hand_value < p_hand_value < 22 and d_hand_value < 22:
        print('You win.  Somehow.')
    elif 22 > d_hand_value > p_hand_value < 22 and d_hand_value:
        print('You lose.')
        _games_lost += 1
    elif p_hand_value < 22 and d_hand_value < 22 and p_hand_value == d_hand_value:
        print('There is a tie.')
        _tie = True



    sleep(1)
    print('Destroying deck:')
    return _games_lost,_tie






primary_function()
