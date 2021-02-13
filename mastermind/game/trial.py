from move import Move
"""
************************************
THIS IS FOR TESTING MOVE ONLY
IT WILL NEED TO BE DELETED AS THE PROGRAM IS COMPLETED.
************************************
"""
class Trial():

    def __init__(self):
        self.move = Move()
        self.guesses()
        

    def guesses(self):
        self.guess1 = [1, 2, 3, 4]
        self.hint1 = ["o**x"]
        self.guess2 = [9, 5, 6, 4]
        self.hint2 = ["x**x"]

        self.move.as_string(self.guess1, self.hint1)
        self.move.as_string(self.guess2, self.hint2)

run = Trial()