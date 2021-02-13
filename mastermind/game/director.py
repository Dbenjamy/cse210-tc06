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
        self._move = None
        self._roster = Roster()
        self._logic = Logic()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._get_name()
        self._get_logic()
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
            
            
    def _get_logic(self):
      
      #either create a new object or ask logic to create a new number
      self._logic.choose_number()
    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        # display the game board
        board = self._logic.show_board()
        self._console.write(board)
        # get next player's move
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        guess = self._console.read_number("What is your next guess? ")
        move = Move(guess)
        #could send to player or logic. Who controls the numbers?
        player.set_move(move)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the logic/roster with the current move.

        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        move = player.get_move()
        self._logic.apply(move)
 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring the winner.

        Args:
            self (Director): An instance of Director.
        """
        if self._logic.game_over():
            winner = self._roster.get_current()
            name = winner.get_name()
            self._console.write(f"\n{name} won!")
            self._keep_playing = False
        self._roster.next_player()