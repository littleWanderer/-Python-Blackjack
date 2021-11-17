# to-do: sum of dealer


#-------Global Variables-------
# list of players
players_list = []

# hand index for splitted hands
hands = 0
    

#imports
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
                    self.cards.append(Card(suit, face, face))

    def show_deck(self):
        for c in self.cards:
            c.show_card()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()

class Dealer():
    def __init__(self):
        self.name = 'Dealer'
        self.hand = []

    # only needs to be called once to give first 2 cards to the dealer
    def hit(self, deck, hidden_card = False):
        self.hidden_dict = {}
        if hidden_card == True:
            card = deck.draw()
            self.hand.append(card)
            hidden_card = False
        if hidden_card == False:
            card = deck.draw()
            self.hand.append(card)

    # prints dealer's hand
    def show_hand(self):
        print(f'{self.name}\'s hand:')
        for c in self.hand:
            c.show_card()
        print('')

    # gives/ takes players' money
    def handle_players_money(player, amount): #gives and takes players money
        if amount > 0:
            player.wallet += amount
        elif amound < 0:
            player.wallet -= amount

    # start new round
    def clear_everything(self):
        pass


class Player():
    def __init__(self, name, wallet=1000):
        self.name = name
        self.wallet = wallet
        self.hand = [[]]
        self.bet = 0

    def my_wallet(self):
        print(f'You have R${self.wallet}')

    def to_bet(self):
        self.bet = int(input(f'{self.name}, how much do you wanna bet? (W = {self.wallet}) '))

    def show_hand(self, index=0):
        if len(self.hand) == 1:
            print(f'{self.name}\'s hand:') 
            for c in self.hand[index]:
                c.show_card()
            print('')
        else:
            print(f'All hands of {self.name}:')
            i = 1
            for h in self.hand:
                print(f'Hand #{i}')
                i += 1
                for c in h:
                    c.show_card()
                print('')

    def stay(self):
        global hands
        if len(self.hand) > 1 and hands <= len(self.hand) - 1:
            print(f'You stayed on your Hand #{hands+1}\n')
            self.show_hand()
        else:
            print(f'{self.name} chose to stay\n\n')
            return False

    def hit(self, deck, hand):
        card = deck.draw()
        self.hand[hand].append(card)

    def double_down(self):
        global hands
        # Adds to bet
        self.bet += int(input(f'How much do you wanna add? (W = {self.wallet}) '))
        print('')
        
        # hit
        self.hit(deck, hands)
##        hands += 1
        self.show_hand()

        # stay
        self.stay()

    def split(self, hands):
##        if self.hand[hands][0].face == self.hand[hands][1].face and len(self.hand[hands]) == 2:
##            self.hand.append([self.hand[hands].pop()])
##            self.bet *= 2
##            return True
        if True:
            self.hand.append([self.hand[hands].pop()])
            self.bet *= 2
            return True
        else:
            print('You can\'t split.\n')
            return False


# initializes the instances
def initializer():
    # Adds players to the game
    n = int(input('What\'s the number of players? '))
    for i in range(n):
        players_list.append(Player(input(f'Name of player #{i+1}: ')))
    print('')

    # Each player places their first bet
    for player in players_list:
        player.to_bet()
    print('')

    # Gives cards to players and dealer and prints their hands
    print('\n//////////////////\n')
    for person in [dealer] + players_list:
        for i in range(2):
            person.hit(deck, 0)
        person.show_hand()
    print('//////////////////\n\n')


    start_game()


def start_game():
    give_options()

    # comparing dearler's and players' cards looking for winners
    win = check_for_winners()

    # if losers: take money
    if win == False:
        pass
    
    # if winners: give money
    else:
        pass

    # new round
    
    
    print('\nacabou')


def give_options():
    # 1 - stay
    # 2 - hit
    # 3 - split
    # 4 - double down

    global hands
    busted = []

    for player in players_list:
        # prints player's hand
        player.show_hand()

        #  variable for splitted hands
        splitting = False

        # makes sure the player does a valid action
        current_player = True
        while current_player:            
            # gives options to player
            if splitting:
                print(f'{player.name}, what do you want to do with your Hand #{hands+1}? (W = {player.wallet})')
            else:
                print(f'{player.name}, what do you want to do? (W = {player.wallet})')

            print(f'1: stay\n2: hit\n3: split [Your bet: R${player.bet} -> R${player.bet * 2}]\n4: double down [Your bet: R${player.bet} -> R${player.bet} + X]\n--> Your choice: ', end='')
            num = int(input())
            print('')

            # stay
            if num == 1:
                player.stay()

                if len(player.hand) > 1 and hands != len(player.hand) - 1:
                    hands += 1
                    continue
                elif hands == len(player.hand) - 1:
                    break

            # hit
            elif num == 2:
                # adds the card the hand
                player.hit(deck, hands)

                # looks for busting
                if check_sum(player) > 21:
                    player.show_hand()

                    if not splitting:
                        print(f'You busted. You\'re out of this round.\n')
                        busted.append(player)
                        current_player = False                    
                        break
                    else:
                        print(f'Your Hand #{hands+1} busted.\n\n')

                        if hands != len(player.hand) - 1:
                            hands += 1
                        else:
                            break
                    
                else:
                    player.show_hand()

                    
                continue

            # split
            elif num == 3:
                if player.split(hands):
                    splitting = True
                player.show_hand()

                continue

            # double down
            elif num == 4:
                player.double_down()

                # for splitting
                if hands != len(player.hand):
                    hands += 1
                    continue
                else:
                    break

    # removes people who busted from current round
    for person in busted:
        game_over(person)

    # prints all hands
    print('\n//////////////////\n')
    for person in [dealer] + players_list:
        person.show_hand()
    print('//////////////////\n\n')
                
# calculates the sum of player's cards
def check_sum(player):
    hand_sum = 0
    for c in player.hand[hands]:
        if c.face == 'Ás':
            player.show_hand()
            one_or_eleven = int(input('How much do you wanna the Ás to be worth of? (1 or 11) '))
            if one_or_eleven not in [1, 11]:
                check_sum(player)
            else:
                hand_sum += one_or_eleven
        else:
            hand_sum += c.value
    return hand_sum


def game_over(player):
    players_list.remove(player)


def check_for_winners():
    global hands
    
    dearler_sum = 0
    players_sum = dict()
    for p in players_list:
        players_sum[p] = []

    # sum of dealer
    for c in dealer.hand:
        pass



    current_sum = 0
    # sum of players
    for p in players_list:
        # not splitted
        if not len(p.hand) > 1:
            for c in p.hand[hands]:
                if c.face == 'Ás':
                    player.show_hand()
                    one_or_eleven = int(input('How much do you wanna the Ás to be worth of? (1 or 11) '))
                    current_sum += one_or_eleven
                else:
                    current_sum += c.value
            players_sum[p].append(current_sum)
            current_sum = 0
            
        # splitted
        else:
            for h in p.hand:
                for c in h:
                    if c.face == 'Ás':
                        player.show_hand()
                        one_or_eleven = int(input('How much do you wanna the Ás to be worth of? (1 or 11) '))
                        current_sum += one_or_eleven
                    else:
                        current_sum += c.value
                players_sum[p].append(current_sum)
                current_sum = 0
    
            
    
    #if it's higher than the dealer's cards


    #black jacks

    
    pass
    





if __name__ == '__main__':
    # setting deck
    deck = Deck()
    deck.shuffle()

    # dealer
    dealer = Dealer()

    # driver
    initializer()














