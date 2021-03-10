'''
This module object creates a deck, shuffles the deck and also handles the hands.
'''
class Card:
    '''
    This creates a card.
    '''
    card_type = 'Playing'
    def __init__(self,card_suit,card_card,card_value,card_name):
        self.suit = card_suit
        self.card = card_card
        self.value = card_value
        self.name = card_name
    def __del__(self):
        #print('{} DESTROYED!'.format(self.name),end=' ')
        print('.',end='')

def spaces(entry,totallen=12):
    '''
    Adds spaces to the variables to attain proper formatting.
    '''
    if ((totallen-len(entry))%2) == 0:
        empty_spaces = ((totallen-len(entry))/2)
        for _ in range(0,int(empty_spaces)):
            entry = (' {} '.format(entry))
    else:
        entry = ('{} '.format(entry))
        empty_spaces = ((1+totallen-len(entry))/2)
        for _ in range(0,int(empty_spaces)):
            entry = (' {} '.format(entry))
    return entry



def c_spool(current_cards,visible):
    '''
    Prints cards in a recognizeable format to stdout.
    '''
    cards_in_row = 10

    card_box_end = '+------------+'
    card_box_fill = '|            |'
    card_box_of = '|     of     |'

    cards_left = len(current_cards)
    card_position = 0

    while cards_left > 0:
        if cards_left/cards_in_row >= 1:
            cards_in_batch = cards_in_row - 1
        else:
            cards_in_batch = cards_left - 1
        print('{}  '.format(card_box_end) * cards_in_batch,end='')
        print(card_box_end,end='\n')
        print('{}  '.format(card_box_fill) * cards_in_batch,end='')
        print(card_box_fill,end='\n')
        print('{}  '.format(card_box_fill) * cards_in_batch,end='')
        print(card_box_fill,end='\n')
        print('{}  '.format(card_box_fill) * cards_in_batch,end='')
        print(card_box_fill,end='\n')


        for _ in range(0,cards_in_batch):
            card_box_card = ('|{}|'.format(spaces(current_cards[card_position].card)))
            print('{}  '.format(card_box_card),end='')
            card_position = card_position + 1
        card_box_card = ('|{}|'.format(spaces(current_cards[card_position].card)))

        if (cards_left - cards_in_batch - 1) < cards_in_row and visible is False:
            card_box_card = ('|{}|'.format(spaces(' ')))

        print(card_box_card,end='\n')
        card_position = card_position - cards_in_batch



        for _ in range(0,cards_in_batch):
            card_box_of = '|     of     |'
            print('{}  '.format(card_box_of),end='')
            card_position = card_position + 1
        card_box_of = '|     of     |'
        if (cards_left - cards_in_batch - 1) < cards_in_row and visible is False:
#           card_box_of = '|    ???     |'
            card_box_of = ('|{}|'.format(spaces('???')))

        print(card_box_of,end='\n')
        card_position = card_position - cards_in_batch


        for _ in range(0,cards_in_batch):
            card_box_suit = ('|{}|'.format(spaces(current_cards[card_position].suit)))
            print('{}  '.format(card_box_suit),end='')
            card_position = card_position + 1
        card_box_suit = ('|{}|'.format(spaces(current_cards[card_position].suit)))
        if (cards_left - cards_in_batch - 1) < cards_in_row and visible is False:
            card_box_suit = ('|{}|'.format(spaces(' ')))
        print(card_box_suit,end='\n')


        print('{}  '.format(card_box_fill) * cards_in_batch,end='')
        print(card_box_fill,end='\n')
        print('{}  '.format(card_box_fill) * cards_in_batch,end='')
        print(card_box_fill,end='\n')
        print('{}  '.format(card_box_fill) * cards_in_batch,end='')
        print(card_box_fill,end='\n')
        print('{}  '.format(card_box_end) * cards_in_batch,end='')
        print(card_box_end,end='\n')

        card_position = card_position + 1
        cards_left = cards_left - cards_in_batch - 1
