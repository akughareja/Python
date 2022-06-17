# This is project 2

# Global variables
suits = ["clubs","diamonds","hearts","spades"]
ranks = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}

# This class will create card object.
class Card():

    def __init__(self,suit,rank):

        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):

        return "{} of {}".format(self.rank,self.suit)


# This class will create deck object and shuffle it randomly.
class Deck():

    def __init__(self):

        self.the_deck = []

        for suit in suits:
            for rank in ranks:
                create_card = Card(suit,rank)
                self.the_deck.append(create_card)

    def shuffle(self):

        import random

        random.shuffle(self.the_deck)

    def deal_one(self):

        return self.the_deck.pop()


# This class will create player object.
class Player():

    def __init__(self,name):

        self.name = name
        self.my_cards = []

    def add_card(self,new_card):

        if type(new_card) == type([]):
            self.my_cards.extend(new_card)
        else:
            self.my_cards.append(new_card)

    def remove_card(self):

        return self.my_cards.pop(0)

    def __str__(self):

        return "{} has {}".format(self.name,len(self.my_cards))


#--------------------------------------------------------------------
# Game - Let's start
#--------------------------------------------------------------------
# Game setup

player1_name = input("Please enter the player1_name: ")
player2_name = input("Please enter the player2_name: ")

player1 = Player(player1_name)
player2 = Player(player2_name)

create_the_deck = Deck()
create_the_deck.shuffle()

# Divide deck equally among two players.
for i in range(26):
    player1.add_card(create_the_deck.deal_one())
    player2.add_card(create_the_deck.deal_one())

no_of_round = 0

game_start = True

while game_start:

    no_of_round = no_of_round + 1
    print("No of round: {}".format(no_of_round))

    if len(player1.my_cards) == 0:
        print("{} out of cards!, Game over!".format(player1.name))
        game_start = False
        break

    if len(player2.my_cards) == 0:
        print("{} out of cards!, Game over!!".format(player2.name))
        game_start = False
        break

    player1_card = []
    player1_card.append(player1.remove_card())
    player2_card = []
    player2_card.append(player2.remove_card())

    game_war = True

    while game_war:

        if player1_card[-1].value > player2_card[-1].value:
            player1.add_card(player1_card)
            player1.add_card(player2_card)
            game_war = False

        elif player2_card[-1].value > player1_card[-1].value:
            player2.add_card(player2_card)
            player2.add_card(player1_card)
            game_war = False

        else:

            print("WAR!!!!")

            if len(player1.my_cards) < 5:
                print("{} has less than 5 cards! {} has won!".format(player1.name,player2.name))
                game_start = False
                break

            elif len(player2.my_cards) < 5:
                print("{} has less than 5 cards! {} has won!".format(player2.name,player1.name))
                game_start = False
                break

            else:
                for i in range(5):
                    player1_card.append(player1.remove_card())
                    player2_card.append(player2.remove_card())
