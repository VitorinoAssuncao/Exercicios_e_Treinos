from core import Core_Rules
from player import Player
from random import randint

def begin_game():
# Inicia o jogo, definindo os jogadores.
    game = Core_Rules()
    name_player = input('Seja bem vindo, qual o nome que deseja usar nessa partida? \n')
    player = Player(name_player)
    computer = Player('Computer')

    print('='*70)
    print('Bem vindo ao jogo, definindo os mapas dos jogadores como uma grade com 5x5.')
    print('='*70)

    print('Este é seu mapa.')
    player.set_map(game.create_map(5))
    player.set_map_of_actions(game.create_map(5))

    computer.set_map(game.create_map(5))
    computer.set_map_of_actions(game.create_map(5))
    
    game.print_map(player.get_map())
    print('Agora, você deve colocar 5 submarinos em posições diferentes.')
    
    for count_sub in range(0,5):
        x = 0
        y = 0
        x = int(input(f'Digite a  latitude (horizontal) de seu {count_sub+1}º submarino)? '))
        y = int(input(f'Digite a  longitude (vertical) de seu {count_sub+1}º submarino)'))
        print('='*100)
        player.set_map(game.define_submarine(player.get_map(),x,y))

    print('='*70)
    print('Assim ficou seu mapa:')
    game.print_map(player.get_map())


    for count_sub in range(0,5):
        x = randint(1,5)
        print(x)
        y = randint(1,5)
        print(y)
        computer.set_map(game.define_submarine(computer.get_map(),x,y))

    print('='*70)
    print('Assim ficou o mapa do computador:')
    game.print_map(computer.get_map())

    turn = 0
    print(game.count_submarines_alive(computer.get_map()))
    while game.count_submarines_alive(computer.get_map()) > 0:
        shot_x = int(input(f'Digite a  latitude (horizontal) de seu {turn+1}º tiro)? '))
        shot_y = int(input(f'Digite a  longitude (vertical) de seu {turn+1}º tiro)'))
        computer.set_map(game.try_to_shot(computer.get_map(),player.get_map_of_actions(),shot_x,shot_y))
        turn += 1

begin_game()