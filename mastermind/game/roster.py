from game.player import player

class Roster:
    """
    An object that keeps track of player information.

    Attributes:
    player_one and player_two: an instance of player used to keep track of
                               its current information.
    turn: keeps track of which player is being interacted with.
    """

    def __init__(self):
        self._turn = 0
        self._maxTurn = 0
        self._the_roster = []


    def add_player(self,the_player):
        """
        Adds a player to the roster
        Args:
            self: an instance of Roster.
            the_player: the player object being added.
        """
        self._the_roster.append(the_player)
        self._maxTurn += 1
        
    def get_current(self):
        """
        This is meant to be a refrence to whichever player's turn it is.

        Args:
            self: an instance of Roster.
        """
        return self._the_roster[self._turn]

    def next_player(self):
        """
        Purmutes turns.

        Args:
            self: an instance of Roster.
        """
        if self._turn != self._maxTurn:
            self._turn += 1
        else:
            self._turn = 0
