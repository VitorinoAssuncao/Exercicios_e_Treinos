from random import randint

class Blackjack():

    def take_card(self):
        card_value = randint(1,13)
        card = []

        card.append(card_value)  

        card_tipe = randint(1,4)

        if card_tipe == 1:
            card.append(' ♥')
        elif card_tipe == 2:
            card.append(' ♦')
        elif card_tipe == 3:
            card.append(' ♣')
        else:
            card.append(' ♠')
        return card

    def print_card(self,card):

        if card[0] == 1:
            temp_card = 'A'
        elif card[0] == 11:
            temp_card = 'J'
        elif card[0] == 12:
            temp_card = 'Q'
        elif card[0] == 13:
            temp_card = 'K'
        else:
            temp_card = str(card[0]) 
               
        card_print = (temp_card+card[1])
        return card_print
