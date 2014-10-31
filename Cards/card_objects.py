__author__ = 'drew bailey'

'''
This is a more abstract look at card objects that can be used for more complex
games.
I wrote these objects with magic the gathering in mind.


The idea here is that we construct a set of objects that do things to themselves
and other objects.

This is what I was thinking...

The "World" holds "Players",
"Players" hold "Decks" (groups of cards),
"Decks" hold "Cards",
and "Cards" cause "Events".

'''


### ROOT EVENT OBJECT ###
class Effect(object):
    def __init__(self):
        pass

    def effect(self):
        pass
    
    def end(self):
        pass


### BASE CARD OBJECT ###
class Card(object):
    '''
    A root card type that all cards can inherit from.
    What properties and functions are shared by all cards.
    '''

    def __init__(self, name, priority=0):
        """ Establish an object's properties. """
        self.name = None
        self.priority = None
        self.allowed_phases = []
        self.cost = None
        self.color = None
        
        self.permanent = True
        self.is_tapped = False

    def destory(self):
        """ Move self to graveyard..? """
        pass

    def exile(self):
        """ Move self to exiled list..? """
        pass
    
    def play(self, conditions):
        """ If conditions are met activate effect and move to field..? """
        if self._check_conditions(conditions=conditions):
            # do something
            self.play_effect()
        if not self.permanent:
            self.destroy()

    def _check_conditions(self, conditions):
        pass
    
    def play_effect(self):
        """ Do something. """
        pass

    def tap_effect(self, target=None):
        pass

    def persistant_effect(self, target=None):
        pass
    
    def tap(self, for_effect=True, target=None):
        self.is_tapped = True
        if for_effect:
            self.tap_effect()

    def untap(self):
        self.is_tapped = False
        

### CARD TYPES ###
class Land(Card):
    def __init__(self, name, color=None):
        """
        :param name:
        :param color: 
        """
        super(self.__class__, self).__init__(name=name)
        self.color = []


class Creature(Card):
    def __init__(self, name, color, cost, power, toughness, tap, effect):
        pass


class Enchantment(Card):
    def __init__(self, name, color, cost, effect):
        pass


class Artifact(Card):
    def __init__(self, name, color, cost, effect):
        pass


class Sorcery(Card):
    def __init__(self, name, color, cost, effect):
        pass


class Instant(Card):
    def __init__(self, name, color, cost, effect):
        pass


### ROOT DECK OBJECT ###
class Deck(object):
    """
    Any grouping of cards...? Graveyards, player decks, other...?
    
    Library
    Graveyard
    Hand
    Board
    """
    pass


### PLAYERS "OWN" OBJECTS AND OBJECT GROUPS ###
class Player(object):
    """
    Players "own" objects and object groups?
    """
    
    def __init__(self, deck):
        self.library = deck
        self.hand = Deck()
        self.graveyard = Deck()
        self.board = Deck()

    def draw(self):
        self.hand.append(self.libary.draw(n=7))

## COLOR OBJECTS ##
class Color(object):
    def __init__(self, name=None):
        self.name = name

# instantiate primary colors
black = Color(name='Black')
white = Color(name='White')
green = Color(name='Green')
red = Color(name='Red')
blue = Color(name='Blue')
colorless = Color(name='Colorless')


## MANA OBJECTS ##
class Mana(object):
    ''' '''
    def __init__(self, color=colorless):
        self.color = color


### THE BOARD ###
class World(object):
    """
    The board holds players, highest level object.
    """

    def __init__(self, *players):
        pass

    def change_phase(self):
        pass


'''
Notes and thoughts:

priority:
most things have priority 0
instants have priority 1
things that resolve before other instants are 2+
each event is resolved in priority/stack order


'''

# lets make some cards
swamp = Land(name='Swamp', generator='Black')
test_1 = Creature(name='Imp', color='Black', cost=[], power, toughness, tap, effect):
