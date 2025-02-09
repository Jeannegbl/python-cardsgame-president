from tkinter import *
import random
import names

COLORS = ['♡', '♤', '♧', '♢']
VALUES = {
    '2': 15,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'V': 11,
    'D': 12,
    'R': 13,
    'A': 14
}


class Deck:
    """ Deck du jeu de société du Président. """
    def __init__(self):
        self.__cards: list = []
        """ Génération d'un deck de 52 cartes"""
        for (symbol, val) in VALUES.items():
            for color in COLORS:
                new_card = Card(symbol, color)
                self.__cards.append(new_card)

    def shuffle(self) -> None:
        """ Mélanger les cartes de mon deck. """
        random.shuffle(self.__cards)

    def pick_card(self):
        return self.cards.pop(0)

    def __str__(self) -> str:
        return str(self.__cards)

    @property
    def cards(self):
        return self.__cards


class Card:
    __symbol: str
    __value: int
    __color: str

    def __init__(self, symbol: str, color: str):
        """
            Card Constructor.
            attrs:
                symbol: One of the VALUES keys.
                color:  One of the  COLORS values.
        """

        self.__symbol = symbol
        self.__value = VALUES[symbol]
        self.__color = color

    def __lt__(self, other):
        return self.__value < other.value

    def __gt__(self, other):
        return self.__value > other.value

    def __eq__(self, other):
        return self.__value == other.value

    def __ne__(self, other):
        return self.__value != other.value

    @property
    def value(self):
        return self.__value

    @property
    def symbol(self):
        return self.__symbol

    #Permet de récupérer la couleur de la carte
    def color(self):
        return self.__color

    def __repr__(self):
        return f"{self.__symbol} {self.__color}"


class Player:
    def __init__(self, player_name=None):
        #Pour nous, le nom est You
        self._name: str = player_name if player_name is not None else "You"
        self._hand: list = []
        #Correspond respectivement à l'ordre pour jouer, un booléen si fini ou no, le nom du role et le score
        self._ordre = 0
        self._finish = 0
        self._role = ""
        self._score = 0

    def add_to_hand(self, card: Card):
        self._hand.append(card)
        self._hand.sort()

    def remove_from_hand(self, cards: list):
        for c in cards:
            self._hand.remove(c)

    #Enleve la carte qui est donné lors du trouduc/président
    def remove_give(self, cards):
        self._hand.remove(cards)

    #Enleve la carte qui est donné lorsque nous sommes le président (car il y a un choix)
    def remove_give_president(self, cards, card_list: list):
        if cards == "3":
            cards = 3
        elif cards == "4":
            cards = 4
        elif cards == "5":
            cards = 5
        elif cards == "6":
            cards = 6
        elif cards == "7":
            cards = 7
        elif cards == "8":
            cards = 8
        elif cards == "9":
            cards = 9
        elif cards == "10":
            cards = 10
        elif cards == "2":
            cards = 2
        for c in card_list:
            if cards == c.value:
                self._hand.remove(c)
                return

    #Donne une carte au joueur préciser lors du trouduc/président
    def give(self, card ,other_player):
        give_card = other_player.add_to_hand(card)
        return give_card

    #Donne une carte au joueur préciser lorsque nous sommes le président (car il y a un choix)
    def give_president(self, cards ,other_player, card_list: list):
        if cards == "3":
            cards = 3
        elif cards == "4":
            cards = 4
        elif cards == "5":
            cards = 5
        elif cards == "6":
            cards = 6
        elif cards == "7":
            cards = 7
        elif cards == "8":
            cards = 8
        elif cards == "9":
            cards = 9
        elif cards == "10":
            cards = 10
        elif cards == "2":
            cards = 2
        for c in card_list:
            if cards == c.value:
                give_card = other_player.add_to_hand(c)
                return give_card

    #Réinitialise la main à zéro carte lorqu'on rejoue, permet surtout d'enlever les cartes qui reste au trouduc
    @property
    def start_hand(self):
        self._hand = []

    @property
    def hand(self):
        return self._hand

    @property
    def name(self):
        return self._name

    def play(self, symbol) -> list:
        """
        Remove from the hand of the player, all cards having a corresponding symbol.
        Args:
            symbol: The symbol to look for.

        Returns: The cards removed from the hand of the player. It will return an empty array if
        nothing is found.

        """
        cards_played = [card for card in self._hand if card.symbol ==
                        symbol]
        self.remove_from_hand(cards_played)
        return cards_played

    def __repr__(self):
        return f"{self.name}\t: {self.hand}"

    def has_symbol(self, card_symbol) -> int:
        nb_cards = 0
        for card in self._hand:
            if card.symbol == card_symbol:
                nb_cards += 1
        return nb_cards


class AIPlayer(Player):
    #Le init de l'ordinateur à un nom aléatoire
    def __init__(self, player_name=None):
        self._name: str = player_name if player_name is not None else \
            names.get_first_name()
        self._hand: list = []

    def play(self, choice, nb_cards: int) -> list:
        """
        Play a card correspondig to what has been played on the table.
        TODO: Implement an AI
        Args:
            choice: The minimum card value to play.
            nb_cards: The number of cards to play.

        Returns: An array of cards to play.

        """
        #"oblige" l'ordi à jouer sa carte la plus faible si nous jouons rien ou si l'ordi commence
        if choice == "":
            choice = "3"
        # "oblige" l'ordi à jouer une simple si nous ne jouons rien ou si l'ordi commence
        if nb_cards == 0:
            nb_cards = 1
        best_choice = None
        for index, card in enumerate(self.hand):
            #redéfinition des puissances des cartes du joueur d'avant
            if choice == "3":
                comparatif = 3
            elif choice == "4":
                comparatif = 4
            elif choice == "5":
                comparatif = 5
            elif choice == "6":
                comparatif = 6
            elif choice == "7":
                comparatif = 7
            elif choice == "8":
                comparatif = 8
            elif choice == "9":
                comparatif = 9
            elif choice == "10":
                comparatif = 10
            elif choice == "V":
                comparatif = 11
            elif choice == "D":
                comparatif = 12
            elif choice == "R":
                comparatif = 13
            elif choice == "A":
                comparatif = 14
            elif choice == "2":
                comparatif = 15
            else:
                comparatif = choice

            if best_choice is None and card.value >= comparatif and \
                    self.has_symbol(card.symbol) >= \
                    nb_cards:
                cards_played = self._hand[index:index + nb_cards]
                self.card_valeur = card.value
                best_choice = card.symbol
                #enleve la carte jouer de l'ordi de sa main
                self.remove_from_hand(cards_played)

        return cards_played if best_choice is not None else []


class PresidentGame:
    def __init__(self, nb_players: int = 4):
        self.__generate_players(nb_players)
        self.generate_cards()
        #Fait la distribution des cartes lorsque l'on commence une partie et possède un compteur de nombre de partie jouer
        self.distribute_cards()
        self.nb_partie = 0

    def __generate_players(self, nb_players: int):
        self.__players = [Player()]
        for _ in range(nb_players-1):
            self.__players.append(AIPlayer())

    def generate_cards(self):
        self.__deck = Deck()
        self.__deck.shuffle()

    def distribute_cards(self):
        giving_card_to_player = 0
        nb_players = len(self.__players)
        while len(self.__deck.cards) > 0:
            card = self.__deck.pick_card()
            self.__players[giving_card_to_player].add_to_hand(card)
            giving_card_to_player = (giving_card_to_player+1) % nb_players

    @property
    def players(self):
        return self.__players

    @property
    def ai_players(self):
        return self.__players[1:]

    @property
    def main_player(self):
        """ Main player is player 0 """
        return self.__players[0]

class Affichage(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Le président')
        self.geometry("1680x1050")
        self.configure(bg='green')