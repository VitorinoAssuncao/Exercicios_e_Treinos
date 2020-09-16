from mechanics.characther_mechanics import Characther_Mechanics

main_flag = 0

while main_flag <= 1:
    option_creation = str(input('Bem vindo ao Dungeon Game, selecione a opção abaixo: \n 1 - Criar Personagem \n 2 - Sair do Jogo \n'))
    if option_creation == '1':
        characther_menu = Characther_Mechanics()
        jogador = characther_menu.characther_creation()
        print(f'{jogador._name}, {jogador._class} Lv. {jogador._lv}')
        print(f'Arma:  {jogador._weapon._name}, Dano:{jogador._weapon._min_dmg} - {jogador._weapon._max_dmg}' )
    else:
        print('Ok, até mais.')
        main_flag = 1

hp = 10
while hp > 0:
    attack_option = input('Deseja atacar?\n 1 - Sim \n 2 - Não \n')
    if attack_option == '1':
        dmg = jogador._weapon.roll_dmg() + jogador._attack
        hp -= dmg
        print(f'Ataque com {jogador._weapon._name} causou {dmg} de dano. HP restante {hp}.')
    else:
        print(f'Combate encerrado, o alvo ficou com {hp} de vida.')
print(f'Seu alvo foi derrotado, parabéns.')
