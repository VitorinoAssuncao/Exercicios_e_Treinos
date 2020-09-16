from app.hangman.data import Data
from app.hangman.mechanics import Hangman

class Bootstrap():

    def execute(self):
        data = Data()
        word = data.sort_word()            
        hangman_game = Hangman(word)

        print(hangman_game.masked_word())

        while hangman_game.win_condition() == False:
            letter = input('Digite a letra desejada. \n')
            print(hangman_game.find_letter(letter))
            print(f'Número de Erros:{hangman_game.errors_icons()}')
            print(hangman_game.selected_letters)

        if hangman_game.letters_wrong >= 5:
            print('Não foi dessa vez.')
        else:
            print("Parabens, você venceu!")