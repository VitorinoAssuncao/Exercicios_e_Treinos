from games.dice.double_dice import DoubleDice
# Declaration of all class instances
dd = DoubleDice()

class PlayDoubleDice():
    def __init__(self,number_players):
        self._number_players = number_players
        self._players_score = []

    def roll_for_turn(self):
        player_rolls = []
        for i in range(0,self._number_players):
            player_rolls.append(dd.roll())
            self._players_score.append(dd.eval_points(player_rolls[i][0],player_rolls[i][1]))
            print(f'O jogador Nº {i+1} rolou {player_rolls[i]}, marcando um total de {self._players_score[i]} pontos.\n')
 #       return player_rolls



    def eval_turn(self):
        player_score = self._players_score
        winner = []
        for i in range(0,len(player_score) ):
            for x in range (i+1,len(player_score)):
                if player_score[i] == player_score[x] and player_score[i] == max(player_score) :
                    winner.append(i+1)
                    winner.append(x+1)
                    return winner

        winner.append(player_score.index(max(player_score))+1)
        return winner 

