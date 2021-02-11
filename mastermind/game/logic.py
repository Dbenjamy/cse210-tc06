import random

class Logic():
    """This class will choose a random four digit
    number. Receive a guess, compare the two numbers
    and output whether the numbers in each position
    match or are in the right spot.
    """
    def __init__(self):
        self.guess = [1, 2, 3, 4]
        self.num = []
        self.result = []
        self.prepare_number()
        

    def prepare_number(self):
        """This method will run on instantion and will 
        generate a random four digit number.

        Args:
            Self: an instance of Logic
        """
        # import random
        for _ in range(4):
            x = random.randint(0, 9)
            self.num.append(x)
        print(self.num)

    def check_numbers(self):
        #compare numbers in the list
        #compare each number and find out if it is in the same location
        for i in range(4):
            inList = False
            for x in range(4):
                if self.num[i] == self.guess[x]:
                    inList = True
                    if i == x:
                        self.result.append("x")
                    else:
                        self.result.append("o")
            if inList == False:
                    self.result.append("*")
                    
        print(self.result)


run = Logic()
run.check_numbers()