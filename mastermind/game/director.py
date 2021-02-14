from game.logic import Logic
from game.console import Console
from game.move import Move
from game.player import Player
from game.roster import Roster

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
  
    Attributes:
        console (Console): An instance of the class of objects known as Console.
        roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._console = Console()
        self._keep_playing = True
        self._move = Move()
        self._roster = Roster()
        self._logic = Logic()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._get_name()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            

    def _get_name(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)
            
            

    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        # display the game board
        self._console._print_board(self._roster._the_roster[0],self._roster._the_roster[1])
        # get next player's move
        player = self._roster.get_current()
        self._console.write(f"{player.player_name}'s turn:")

        guess = self._console.read_number("What is your next guess? ")
        #could send to player or logic. Who controls the numbers?
        self._roster.get_current().guess = guess

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the logic/roster with the current move.

        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        self._logic.check_number(str(player.guess), player)
        self._roster.get_current().hint = "".join(self._logic.result)
        self._move.as_string(str(self._roster.get_current().guess),str(self._roster.get_current().hint))
 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring the winner.

        Args:
            self (Director): An instance of Director.
        """
        if self._roster.get_current().win:
            winner = self._roster.get_current().player_name
            print(f"\n{winner} won!")
            self._keep_playing = False
        self._roster.next_player()
