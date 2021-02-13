class Player:
    """This class will create the players used to interact with the game

    Methods:
        player_name: an instance of the player's name
        guess: a string used to store guesses made by the user
        hint: a string used to help the user make correct guesses
        win: a boolean to determine if the player has won the game

    Arguments:
    self: the constructor
    name: the name of the player"""
        
    def __init__(self,name):
        """ Creates an instance of self and
        stores the name of the player"""
        
        self.player_name = name
        self.guess = '----'
        self.hint = '****'
        self.win = False