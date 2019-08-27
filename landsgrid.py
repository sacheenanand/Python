__author__ = 'sanand'
#Imagine you just started working at a gaming software company.

#The company is building many card based games (e.g. solitaire, hearts, blackjack, poker, etc.) You notice that every game has it's own implementation of Card and Deck classes - complete mayham! You quickly get to work designing a single set of Card and Deck classes that can be shared across most (if not all) games.  Some points to consider:

#Many games allow a card to be either face up or face down
#Some cards have a face (Jack, Queen, King)
#All cards have a numeric value, sometimes they have more than one value (i.e. an Ace can be a 1 or a 11 in blackjack), and different games might assign different values to different cards (i.e. in blackjack, the face cards are all worth 10, but in other games they are worth 11, 12, and 13 for Jack, Queen, and King, respectively.
#Many games have separate "piles" of cards, such as a "draw" pile and a "discard" pile
#Some games allow for more than one player


#Given the above, it's likely that more than just the two aforementioned classes would be useful. Design these classes here. When it comes to methods, just include the signature; do not mind the implementation. Also think about what methods would be useful to have on your classes that would otherwise have to get re-implemented in all the different games.  And do not copy from online sources.  We want to see your code, not someone else's.

#Finally, don't worry too much about the syntax as what we are looking for high-level design here, so whatever communicates the basic contract most easily is fine. Include comments where appropriate.


'''
class deck:
    def __init__(self, name):
        self.name = name

    def faceup(self):
        return
    def facedown(self):
        return
    def draw(self):
        return
    def pile(self):
        return
    def discard(self):
        return

r1 = deck("Jack", )
r2 = deck("Queen", )
r3 = deck("king", )

class Card:
    def __init__(self, name):
        self.name= name




class AbstractCard(object):

    _suit = None
    _value +None
    _open = None

def __init__(self, suit, value, open = False):
    self._suit = suit
    self._value = value
    self._open = open

def get_value(self):
    return self._value
    def set_value(self):


class GameCard(AbstractCard):
    _value_choices = set()

def __init__(self, suit, value, value_choices, open = False):

    self._suit = suit
    self._value = value
    self._value_choices = value_choices
    self._open = open

def set_value(values):



#change values
class AbstractCard(object):
    _suite = None
    _value = None
    _open = False

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self):

    def get_suite(self):

    def is_card_faceup(self):
        return _open == True

    def open_card(self, value):
        self._open = value

    def get_faceup_down(self):
        return self._open


class GameCard(AbstractCard):
    _value_choices = set()

def __init__(self, suit, value, value_choices, open = False):
    self._suit = suit
    self._value = value
    self._value_choices = value_choices
    self._open = open

def get_value_choices(self):

def set_value(values):
#change values

'''





