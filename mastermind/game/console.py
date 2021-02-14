import random
from game.move import Move
class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.


    Attributes:
        prompt (string): The prompt to display on each line.
    """
    
     
    def read(self, prompt):
        """Prints out the name of each Players

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        
        return input(prompt)
    
    def player_board(self, prompt):
      #Takes print statement from director and displays the game board.
      
      print(prompt)
      
      
    def blank_turn(self, prompt):
      """ Prints out blank terminal for each player at the
      beginning of game.
      
      Get's blank terminal from player
      """
      
      print(prompt)

    def read_number(self, prompt):
        """Gets numerical input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            integer: The user's input as an integer.
        """
        their_input = input(prompt)
        if len(their_input) == 4:
            try:
                int(their_input)
                return their_input
            except ValueError:
                print("Must be a four digit number.")
                return self.read_number(prompt)
        else:
            print("Must be a four digit number.")
            return self.read_number(prompt)


    def write(self, text):
        """Displays the winner text on the screen from director.

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(text)


    def _print_board(self,player_one,player_two):
    
        print(f"--------------------\n\
Player {player_one.player_name}: {player_one.guess}, {player_one.hint}\n\
Player {player_two.player_name}: {player_two.guess}, {player_two.hint}\n\
--------------------")

    def _print_history(self,past_moves):
        for i in range(len(past_moves)):
            numm = i + 1
            print(past_moves[i],past_moves[numm])