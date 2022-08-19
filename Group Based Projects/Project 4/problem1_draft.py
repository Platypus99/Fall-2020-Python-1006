# Group Exercises 4

# Teammates: Perry Flamer, Luke Zerrer, Lance Wong

import random

class Card(object):  
    int_set = {'♠2','♣2','♦2','♥2',
               '♠3','♣3','♦3','♥3',
               '♠4','♣4','♦4','♥4',
               '♠5','♣5','♦5','♥5',
               '♠6','♣6','♦6','♥6',
               '♠7','♣7','♦7','♥7',
               '♠8','♣8','♦8','♥8',
               '♠9','♣9','♦9','♥9',
               '♠10','♣10','♦10','♥10'}
    face_card_set = {'J', 'Q', 'K'}
    
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
        pass # replace this        

    def __str__(self):
        # first char is always suit ie: __str__()[0]
        # remaining chars are the rank ie: __str__()[1:]
        return str(self.suit) + str(self.rank)
        # return '' # replace this line

    def value(self, total):
        if self in self.int_set:
            return int(self.__str__()[1:])
        elif self.__str__()[1] in self.face_card_set:
            return 10
        else:   #for the ace
            if total > 10:
                return 1
            else:
                return 11
        

        
        # return 0 # replace this line


def make_deck():

    suits = ['♠','♣','♦','♥']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    cards_li = []
    for suit in suits:
        for rank in ranks:
            temp_card = Card(suit, rank)
            cards_li.append(temp_card)
    random.shuffle(cards_li)
            
            
        

    # use random.shuffle(some_list) to shuffle the deck of cards.
    # return [] # replace this line 
    return cards_li


def main():
    deck = make_deck()


if __name__ == "__main__":
    main()
