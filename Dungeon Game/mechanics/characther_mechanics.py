from templates.characthers.characther_classes.knight_class import Knight
from templates.characthers.characther_classes.rogue_class import Rogue
from templates.characthers.characther_classes.warrior_class import Warrior
class Characther_Mechanics():

    def characther_creation(self):
        flag_begin = 0 
        while flag_begin == 0:
            menu_creation = input('Selecione a classe de seu personagem, conforme a opção abaixo: \n 1 - Guerreiro \n 2 - Cavaleiro \n 3 - Assassino \n')
            nome = input('Digite o nome que deseja para seu personagem:')
            if menu_creation == '1':
                characther = Warrior(nome)
                break
            elif menu_creation == '2':
                characther = Knight(nome)
                break
            elif menu_creation == '3':
                characther = Rogue(nome)
                break
            else:
                print('Favor selecionar uma das opções acima.')
        return characther
