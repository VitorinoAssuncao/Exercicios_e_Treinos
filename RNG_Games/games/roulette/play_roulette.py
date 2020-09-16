from games.roulette.roulette import Roulette

class Play_Roulette(Roulette):


    def bet_options(self):
        option = 0
        number = 0
        color = 0
        odd_even = 0

        while option == 0 or option < 5:
            number_sorted = self.roll_roulette()
            option = int(input('Chose how you whant to bet:\n 1 - Number;\n 2 - Color ;\n 3 - Odd or Even ; \n 4 - Range. \n'))
            if option == 1:
                number = int(input('What number you gonna bet?\n'))
                self.eval_bet_number(number,number_sorted)
            elif option == 2:
                color = int(input('What color you gonna bet?\n 1 - Red. \n 2 - Black.\n 3 - Green. \n'))
                self.eval_bet_color(color,number_sorted)
            elif option == 3:
                odd_even = int(input('Whant to bet in Odd Numbers or Even Numbers?\n 1 - Odd. \n 2 - Even'))
                self.eval_bet_odd_even(odd_even,number_sorted)
            elif option == 4:
                range_n = int(input('What the range you gonna bet? \n 1 - 1 to 12 \n 2 - 13 to 24 \n 3 - 25 to 36'))
                self.eval_range_number(range_n,number_sorted)
            else:
                print('Chose one option from above.')

    def eval_bet_number(self,bet_number,number_sorted):
        print(f'The number sorted is '+str({number_sorted}))
        if bet_number == number_sorted:
            print('You is the winner!')
        else:
            print('Sorry, not this time.')

    def eval_bet_color(self,color,number_sorted):
        print(f'The number sorted is '+str({number_sorted}))
        if color == 1 and self.isred(number_sorted) == 'red':
            print('You is the winner!')
        elif color == 2 and self.isred(number_sorted) == 'black':
            print('You is the Winner!')
        elif color == 3 and self.isred(number_sorted) == 'green':
            print('You is the Winner!')
        else:
            print('Sorry we have a bug, not this time.')
    
    def eval_bet_odd_even(self,odd_even,number_sorted):
        print(f'The number sorted is '+str({number_sorted}))
        if odd_even == 1 and self.iseven(number_sorted) == 'odd':
            print('Great Day champs, the prize is yours.')
        elif odd_even == 2 and self.iseven(number_sorted) == 'even':
            print('And the prize go, tooooo you!')
        else:
            print('Sorry, not a good day for you.')
    
    def eval_range_number(self,range_n,number_sorted):
        print(f'The number sorted is '+str({number_sorted}))
        if range_n == 1 and (number_sorted >= 1 and number_sorted <= 12):
            print('Hey Buddy, the prize is yours.')
        elif range_n == 2 and (number_sorted >= 13 and number_sorted <= 24):
            print('The prize go, to the lady in black. Yes, is you.')
        elif range_n == 3 and (number_sorted >= 25 and number_sorted <= 36):
            print('Yes, take the money.')
        else:
            print('Sorry.') 

