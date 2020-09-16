from random import randint

class DoubleDice():

    def roll(self):
        roll_value = []
        roll_value.append(randint(1,6))
        roll_value.append(randint(1,6))
        return roll_value   
    
    def eval_points(self,value_1,value_2):
        result = 0
        if (value_1 == value_2):
            result = (value_1 + value_2) * 2
        elif (value_1 == 1 and value_2 == 1):
            result = 0
        else:
            result = value_1 + value_2
        
        return result