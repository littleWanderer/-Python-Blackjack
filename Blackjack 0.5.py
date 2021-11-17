#-------Imports-------
import random


class Card():
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value

    def show_card(self):
        print(f'{self.face} de {self.suit}')


class Deck():
    cartas_figuradas = {1: 'Ás', 11: 'Valete', 12: 'Dama', 13: 'Rei'}
    cartas_figuradas_valor = {'Ás': [1, 11], 'Valete': 10, 'Dama': 10, 'Rei': 10}

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ['copas', 'espadas', 'ouro', 'paus']:
            for face in range(1,14):
                if face in [1, 11, 12, 13]:
                    face = Deck.cartas_figuradas[face]
                    value = Deck.cartas_figuradas_valor[face]
                    self.cards.append(Card(suit, face,value))
                else:
                    self.cards.append(Card(suit, face, face)) #face is the same as the value

    def show_deck(self):
        for c in self.cards:
            c.show_card()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop() # the end of the list is the top


class Dealer():
    def __init__(self):
        self.hand = []
        for player in Player.players_list:
            self.hand_cards(deck, player)
        p1.show_hand(0)
        
    def hand_cards(self, deck, player):
        drew = deck.draw()
        drew.show_card()
        player.hand[0].append(drew)

    def give_money(self, player, amount):
        player.current_money(amount)

    #when round ends, clear all hands and rebuild deck


class Player():
    players_list = []
    def __init__(self, name, wallet=1000):
        self.name = name
        self.wallet = wallet
        self.bet = 0
        self.hand = [[]]

    def bet(self):
        self.bet = int(input('How much do you wanna bet?')) * (-1)
        self.current_money(self.bet)

    def current_money(self, amount=0):
        self.wallet = self.wallet + amount
        print(f'You have: R${self.wallet}')

    def actions(self):
        #double down, split
        pass
    
    def ask_for_card(self):
        pass

    def show_hand(self, index):
        for c in self.hand[index]:
            c.show_card()


# stater function
def main():
    global deck
    global p1
    
    print('Let\'s play Blackjack!!!')
##    n = int(input('How many players? (not including the dealer)'))

    deck = Deck()
    deck.shuffle()
    
    p1 = Player('un')
##    p2 = Player('deux')
##    p3 = Player('trois')
    Player.players_list.append(p1)
##    Player.players_list.append(p2)
##    Player.players_list.append(p3)

    dealer = Dealer()
    p1.show_hand(0)
##    for player in Player.players_list:
##        player.show_hand(0)





##sergio = Player('Serjão')
##deck = Deck()
##deck.shuffle()
##d.show_deck()

main()








