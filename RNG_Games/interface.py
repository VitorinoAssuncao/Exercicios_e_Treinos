from games.blackjack.play_blackjack import Play_Blackjack
from games.dice.play_dices import PlayDoubleDice
from games.roulette.play_roulette import Play_Roulette

menu = 0

while menu != 9:
    menu= int(input(f'Hello, whant to play a game? Choose one from the list above: \n 1 - Blackjack; \n 2 - Double Dice; \n 3 - Roulette; \n 9 - Exit \n'))

    # Inicia-se o código para o jogo de Blackjack

    if menu == 1:
        # Inicializada a classe, e após inicializamos o jogo, e exibimos a mensagem na tela.
        blackjack = Play_Blackjack()
        list_cards_player = blackjack.begin_game()
        blackjack.msg_cards(list_cards_player)

        # Avalia se o jogador já tem os 21 pontos, ou quantos pontos possui
        points = blackjack.eval_points(list_cards_player)

        #Criação do menu, para mostrar o resultado, ou oferecer mais uma nova carta
        options = 1
        while options == 1 and points < 21:
            if points > 21:
                print(f'You lose, with {points}')
            elif points == 21:
                print(f'Blackjack!!!')
            else:
                options=int(input(f'You have {points} points, press 1 to take one more card, or 2 to end the game.'))
                if options == 1:
                    blackjack.add_card(list_cards_player)
                    points = blackjack.eval_points(list_cards_player)

        if points > 21:
            print(f'You lose, with {points} points.')
        elif points == 21:
            print(f'Blackjack!!!')
        else:
            print(f'You win with {points} points.')
        
        # Inicia-se o código do jogo de dados
    elif menu == 2:
        # Declaration of all list's variables
        player_rolls = []
        player_score = []
        flag = 0

        while flag == 0:
            players = int(input("How many players you whant:\n"))
            print('='*143)
            if players < 2:
                print('The number minimum of players is 2.\n')
            else:
                flag = 1

        play_turn = PlayDoubleDice(players)
        play_turn.roll_for_turn()
            
        msg = play_turn.eval_turn()
        print('='*144)
        if len(msg) > 1:
            print(f'The winners (it drawn) is:')
            for i in msg:
                print(f'{i}º Player')
        else:
            print(f'The winner is:{msg[0]}º Player')
        
    elif menu == 3:
        roulette = Play_Roulette()

        roulette.bet_options()

                        


