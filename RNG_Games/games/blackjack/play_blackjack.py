from games.blackjack.blackjack_game import Blackjack

class Play_Blackjack():
    def __init__(self):
        self.bj = Blackjack()

    def begin_game(self):
        cards = []
        for i in range(0,2):
            c = self.bj.take_card()
#            print(c)
            cards.append(c)
        return cards 

    def msg_cards(self, list_cards):
        for i in range(0,len(list_cards)):
            print(f'Your {i+1}º card is {self.bj.print_card(list_cards[i])}')

    def eval_points (self,list_cards):
        points = 0
        for i in range(0,len(list_cards)):
            if list_cards[i][0] >= 10 and list_cards[i][0] <= 13:
                points += 10
            else:
                points += list_cards[i][0]
        return points

    def add_card(self,list_cards):
        verify = 0
        while verify == 0:
            new_card = self.bj.take_card()
            verify = self.verify_card(new_card,list_cards)

        list_cards.append(new_card)
        print(f'Your new card is {self.bj.print_card(list_cards[-1])}')

        return list_cards

    def verify_card(self,card,list_cards):
        for i in range(0,len(list_cards)):
            if self.bj.print_card(card) == self.bj.print_card(list_cards[i]):
                return 0
        return 1