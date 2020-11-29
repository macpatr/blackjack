import random
global playing


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


# SINGULAR CARD DEFINING
class Card:

    # if you have suit and rank defined in the init method, you will have to establish them when you use this object
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


# DECK DEFINING
class Deck:

    # just self argument, so there will be no option for changing the base deck
    def __init__(self):
        self.deck = []  # so you start with an empty list

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        all_cards = ''
        for card in self.deck:
            all_cards += card.__str__() + '\n'
        return "The deck consists of: " + all_cards

    def shuffle(self):
        return random.shuffle(self.deck)

    # could as well take one line
    def dealing_one(self):
        dealing = self.deck.pop()
        return dealing


# HAND DEFINING
class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add(self, card):
        # Deck.dealing_one() -> single card(suit, rank)!!!!!!!
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def check_for_aces(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# ACCOUNT STATE
class Chips:

    def __init__(self, total = 100):
        self.total = total
        self.bet = 0

    def __str__(self):
        return self.total

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        print('\nYou have ${} now'.format(player_chips.__str__()))

        try:
            #THATS SUPER IMPORTANT STEP TO PUT CHIPS.BET!!!
            chips.bet = int(input("Place your bet amount: "))

        except:
            print("Sorry, that is incorrect")
            continue

        else:
            if chips.bet > chips.total:
                print("Sorry, you have only {} ".format(player_chips))
            else:
                break


def hit(deck, hand):
    hand.add(deck.dealing_one())
    hand.check_for_aces()


# GAMEPLAY OPTIONS
def hit_or_stand(deck, hand):

    while player.value < 21:
        x = input('Do you want to Hit or Stand? Enter h or s: ')

        if x[0].lower() == 'h':
            hit(deck, hand)
            print("\n")
            print('DEALER: ' + str(dealer.value))
            print('PLAYER: ' + str(player.value))
            print(player.cards.__str__())

        elif x[0].lower() == 's':
            print("Dealer's turn now...")
            break
        else:
            print("Sorry, didn't get that")




# DISPLAYING HANDS:
def show_some(player, dealer):
    print('DEALERS HAND')
    print("One card is hidden")
    print(dealer.cards[1])
    print('\n')
    print('PLAYERS HAND: ')
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    print("DEALER'S HAND: ")
    for card in dealer.cards:
        print(card)
    print('\n')
    print("PLAYER'S HAND: ")
    for card in player.cards:
        print(card)
    print("\n")


# GAME OUTCOMES NOW:

def player_busts(player, dealer, chips):
    print("PLAYER BUSTS!")
    print("DEALER: {}".format(dealer.value.__str__()))
    print("PLAYER: {}".format(player.value.__str__()))
    chips.lose_bet()


def dealer_busts(player, dealer, chips):
    print("DEALER BUSTS!")
    print("DEALER: {}".format(dealer.value.__str__()))
    print("PLAYER: {}".format(player.value.__str__()))
    chips.win_bet()


def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    print("DEALER: {}".format(dealer.value.__str__()))
    print("PLAYER: {}".format(player.value.__str__()))
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("PLAYER LOSES!")
    print("DEALER: {}".format(dealer.value.__str__()))
    print("PLAYER: {}".format(player.value.__str__()))
    chips.lose_bet()


def push(player, dealer):
    print('You both have the same amount of points! TIE')
    print("DEALER: {}".format(dealer.value.__str__()))
    print("PLAYER: {}".format(player.value.__str__()))


# GAME IS ON:

deck = Deck()
deck.shuffle()
player_chips = Chips()

print("WELCOME TO BLACKJACK!")

while True:
    player = Hand()
    dealer = Hand()
    print("The first round's outcome is: \n")

    for round in range(2):
        pulled_card = deck.dealing_one()
        player.add(pulled_card)
        pulled_card = deck.dealing_one()
        dealer.add(pulled_card)

    show_some(player, dealer)
    take_bet(player_chips)


    print('\nDEALER: ' + str(dealer.value))
    print('PLAYER: ' + str(player.value))

    hit_or_stand(deck, player)


    show_some(player, dealer)

    if player.value > 21:
        player_busts(player, dealer, player_chips)


    try:
        if player.value < 22:
            while dealer.value < 17:
                hit(deck, dealer)
                continue
    finally:
        print("\n")

    show_all(player, dealer)

    if player.value > 21:
        dealer_wins(player, dealer, player_chips)
    elif dealer.value > 21:
        player_wins(player, dealer, player_chips)
    elif player.value < dealer.value:
        dealer_wins(player, dealer, player_chips)
    elif player.value > dealer.value:
        player_wins(player, dealer, player_chips)
    elif player.value == dealer.value:
        push(player, dealer)

    print("\nPlayer chips are at: {}".format(player_chips.__str__()))

    new_game = input("Would you like to play another hand? y/n: ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing!")
        break

