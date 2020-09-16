from random import randint

class Roulette():

    def roll_roulette(self): 
        number = 0
        number = randint(0,36)
        return number

    def iseven(self,number):
        if number % 2 == 1:
            return 'odd'
        else:
            return 'even'

    def isred(self,number):
        
        if number == 0:
            return 'green'
        elif (self.iseven(number) == 'odd' and ((number >= 1 and number <= 10) or (number >= 19 and number <= 28))) or (self.iseven(number) == 'even' and ((number >= 11 and number <= 18) or (number >= 29 and number <= 36))):
            return 'red'
        else:
            return 'black'   

