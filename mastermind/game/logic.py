import random
from game.player import Player

class Logic():
    """This class will choose a random four digit
    number. Receive a guess, compare the two numbers
    and output whether the numbers in each position
    match or are in the right spot.
    """
    def __init__(self):
        self.masterNum = []
        self.result = []
        self._prepare_number()
        

    def _prepare_number(self):
        """This method will run on instantion and will 
        generate a random four digit number.

        Args:
            Self: an instance of Logic
        """
        #creates random four digit number to be guessed
        for _ in range(4):
            x = random.randint(0, 9)
            self.masterNum.append(x)

    def check_number(self, guess, player):
        """This method will compare the number to the users guess and
        create a hint using "x's", "o's", and "*".

        Args:
            Self: an instance of Logic
        """
        self.result = []
        for i in range(4):
            #first loop will iterate through each location of the masterNum
            inList = False # used for checking if each number guessed is in the masterNum list
            for x in range(4):
                # second loop compares the digit i in masterNum with each digit in the guess
                if self.masterNum[i] == int(guess[x]):
                    inList = True
                    if i == x:
                        self.result.append("x") # right number & location
                    else:
                        self.result.append("o") # right number & wrong location
            if inList == False:
                    self.result.append("*") # not in the list

        s = [str(i) for i in self.masterNum]
        singleInt = int("".join(s))
        if singleInt == int(guess):
            player.win = True
