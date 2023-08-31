"""
Design the data structure for a generic deck of cards. Explain how you would subclass the data structure to implement blackjack

Notes:
52 cards in total
4 suits,  Hearts (♥),Diamonds (♦),Clubs (♣),Spades (♠)
Each suit contains 13 cards, ranks from 2 to 10 and then jack queen and king and ace. 
"""
import random
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank 

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self):
        suits = ["Hearts","Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = [Card(suit,rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        if not self.is_empty():
            return self.cards.pop()
    def is_empty(self):
        return len(self.cards) == 0
"""
Code to Test the Deck


deck = Deck()

# Shuffle the deck
deck.shuffle()

# Deal and print the first 5 cards
for _ in range(5):
    card = deck.deal()
    if card:
        print(card)
    else:
        print("No more cards in the deck.")

"""  
"""Subclass the data strucures to implement Blackjack."""

import random
class Card:
    def __init__(self,suit,rank,value):
        self.suit = suit
        self.rank = rank 
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self):
        suits = ["Hearts","Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = [Card(suit, rank, min(idx + 2, 10)) for idx, rank in enumerate(ranks) for suit in suits]
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        if not self.is_empty():
            return self.cards.pop()
    #def is_empty(self):
       # return len(self.cards) == 0

class BlackJackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = []
        self.dealer_hand = []

    def deal_initial_hands(self):
        self.deck.shuffle()
        self.player_hand = [self.deck.deal(), self.deck.deal()]
        self.dealer_hand = [self.deck.deal(),self.deck.deal()]

    def calculate_hand_value(self,hand):
        total_value = sum(card.value for card in hand)
        num_aces = sum(1 for card in hand if card.rank == 'Ace')
        while total_value>21 and num_aces:
            total_value -= 10
            num_aces -=1
        return total_value
    
    def play(self):
        self.deal_initial_hands()
        while True:
            print(f"Player's Hand: {[str(card) for card in self.player_hand]}")
            player_value = self.calculate_hand_value(self.player_hand)
            print(f"Player's Total Value: {player_value}")

            if player_value == 21:
                print("BLACKJACK! Player Wins!")
                break
            if player_value > 21:
                print("Player busts. Dealer wins")
                break
            

            action = input("Do you want to hit or stand").lower()
            if action == "hit":
                self.player_hand.append(self.deck.deal())
            elif action == "stand":
                while self.calculate_hand_value(self.dealer_hand) < 17:
                    self.calculate_hand_value(self.deck.deal())

                print(f"Dealer's Hand: {[str(card) for card in self.self.dealer_hand]}")
                dealer_value = self.calculate_hand_value(self.dealer_hand)
                print(f"Dealer's Total Value: {dealer_value}")

                if dealer_value > 21:
                    print("Dealer busts. Player wins!")
                elif dealer_value >= player_value:
                    print("Dealer wins.")
                else:
                    print("Player wins!")

                break

if __name__ == "__main__":
    game = BlackJackGame()
    game.play()

            