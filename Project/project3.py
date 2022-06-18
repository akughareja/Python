# Project 3

import random

suits = ["clubs","diamonds","hearts","spades"]
ranks = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}

playing = True

# Card class
class Card():

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# Deck class
class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank,suit))

    def __str__(self):
        deck_info = " "
        for card in self.deck:
            deck_info += "\n" + card.__str__()
        return "The deck has: " + deck_info

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)


# Hand class
class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_ace_value(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        cards_in_hand = " "
        for card in self.cards:
            cards_in_hand += "\n" + card.__str__()
        return "The cards in hand: " + cards_in_hand


# Chip class
class Chip():

    def __init__(self,balance=100):
        self.balance = balance
        self.bet = 0

    def won_chips_balance(self):
        self.balance += self.bet

    def lost_chips_balance(self):
        self.balance -= self.bet

    def __str__(self):
        return "Total balance: {}".format(self.balance)


# Write taking bet function
def taking_bet(chip):

    while True:
        try:
            chip.bet = int(input("Please enter the bet amount: "))
        except:
            print("It's not number!, Enter bet amount:")
        else:
            if chip.bet > chip.balance:
                print("Bet can not be exceeds the total balance",chip.balance)
            else:
                break


# Write taking hit function
def taking_hit(deck,hand):

    dealt_card = deck.deal()
    hand.add_card(dealt_card)
    hand.adjust_ace_value()


# Write hit or stand function
def hit_or_stand(deck,hand):

    global playing

    h_o_s = input(" Are you going to hit or stand? h or s...?: ")

    while True:
        if h_o_s[0].lower() == "h":
            taking_hit(deck,hand)

        elif h_o_s[0].lower() == "s":
            print(" Dealear's turn: ")
            playing = False

        else:
            print("Please try again...!!")
            continue
        break


# Write display function
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print(" ",dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)


# Write wins and busts function
def player_busts(player,dealer,chips):
    print("player bust....!!")
    chips.lost_chips_balance()

def player_wins(player,dealer,chips):
    print("player win....!!")
    chips.won_chips_balance()

def dealer_busts(player,dealer,chips):
    print("dealer bust....!!")
    chips.won_chips_balance()

def dealer_wins(player,dealer,chips):
    print("dealer win....!!")
    chips.lost_chips_balance()

def push(player,dealer):
    print("dealer and player tie....!!")


##################################################################
#   Let's start black jack ---------------------------->>>>>>>>>>>
##################################################################

while True:

    print(" Welcome to BLACK JACK .......!!!!")

    created_deck = Deck()
    created_deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(created_deck.deal())
    player_hand.add_card(created_deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(created_deck.deal())
    dealer_hand.add_card(created_deck.deal())

    player_chips = Chip()

    taking_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:

        hit_or_stand(created_deck,player_hand)
        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit_or_stand(created_deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)

    print("\n player's total balance: ",player_chips.balance)

    play_again = input(" Would you like to play again...??? y or n...?: ")

    if play_again[0].lower() == "y":
        playing = True
        continue
    else:
        print("Thanks for playing!!!!")
        break
