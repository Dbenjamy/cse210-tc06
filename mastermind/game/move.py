class Move():
    """This class is responsible for storing the guesses
    and hints from each player in the game. This data will
    be called to console to be displayed on the board.

    Methods:
        as_string: stores the previous guesses and hints as a string
            to easily be passed to console to be displayed.

    Attributes:
        string_list: stores the list of guesses and hints in this form:
            ['last guess', 'last hint', .........]
    """
    def __init__(self):
        """Class constructor

        Args:
            Self: an instance of self
        """
        #initializes the attribute
        self.string_list = []


    def as_string(self, lastGuess, lastHint):
        """This method will build combine the guess and hints into a list
        of strings.
        
        Args:
            Self: an instane of move
            lastGuess: the data for the most recent guess
            lastHint: the data fro the most recent hint
        """
        # turns the lastGuess list into a single int four digits long
        s = [str(i) for i in lastGuess]
        singleInt = int("".join(s))

        # converts the lastHint list into a single string
        string_hint = str("".join(lastHint))

        # adds the most recent guess and hint to the end of the list
        self.string_list.append(str(singleInt))
        self.string_list.append(string_hint)
        print(self.string_list[0], self.string_list[1])