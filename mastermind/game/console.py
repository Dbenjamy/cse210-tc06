import random

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
        return input(prompt)
        
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
