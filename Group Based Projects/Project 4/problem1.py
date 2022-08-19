#/usr/bin/python
# -*- coding: utf-8 -*-

#Partners: Perry Flamer, Lance Wong, Luke Zerrer

import random

#create a card class which will allow instances of each card to be used by the make_deck function. Each card contains a suit and a rank.
class Card(object):  
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank        

    def __str__(self):
        return str(self.suit) + str(self.rank)  

    def value(self, total):
        
        self.total = total
        if self.rank in ['2','3','4','5','6','7','8','9','10']:
            return int(self.rank)
        elif self.rank in "JQK":
            return 10
        elif self.rank == "A" and int(self.total) <= 10:
            return 11
        elif self.rank == "A" and int(self.total) > 10:
            return 1
        
        
                  
    def __repr__(self):
        return str(self)

#define a function capable of making a deck of card objects and shuffling it
def make_deck():

    suits = ['♠','♣','♦','♥']
    
    ranks = ['2','3','4','5','6','7','8','9','10', 'J', 'Q', 'K', 'A']
    
    li = []
    for i in suits:
        for j in ranks:
            li.append(Card(i,j))
            
    
    random.shuffle(li) 
    return li  # replace this line 

#run the make a deck function to create a deck. Main method runs the game storing 3 variables to keep track of game state. 
def main():
    deck = make_deck()
    player_sum = 0
    my_sum = 0
    answer = "y"
    while True:
        
        
        draw = deck[0]
        deck.pop(0)
        
        if answer == "y":
            player_sum += draw.value(player_sum)
            print("You drew ", draw, "\n", "sum:", player_sum)
        elif answer == "n":
            my_sum += draw.value(my_sum)
            print("I drew ", draw, "\n", "my sum:", my_sum)
  
        #checks if a player has won/lost
        if player_sum > 21:
            print("you lose.")
            break
        elif player_sum == 21:
            print("you win.")
            break
        elif my_sum >= 17:
            if my_sum == 21:
                print("you lose.")
                break
            elif my_sum > 21:
                print("you win.")
                break
            elif my_sum == player_sum:
                print("tie")
                break
            elif my_sum > player_sum:
                print("you lose.")
                break
        if answer == "y":
            answer = input("Do you want to draw another card? (y/n)")
        if answer == "y":
            continue
        elif answer == "n":
            print("my turn.") 
            continue
        
if __name__ == "__main__":
    main()
