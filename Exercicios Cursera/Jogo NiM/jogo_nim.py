n = 0
m = 0
rodadas = 0

def inicia_jogo():
    n = 0
    m = 0
    opcao = 0
    while ((opcao != 1) and (opcao != 2)):
        print('Seja bem vindo ao jogo NiM.! Escolha:')
        print('1 - Para jogar uma partida isolada')
        opcao = int(input('2 - Para jogar um campeonato '))
        if (opcao != 1) and (opcao != 2):
            print('Favor selecionar uma das opções apresentadas.')

    if opcao == 1:       
        partida()
    else:
        campeonato()


def partida():       
    n = set_n()
    m = set_m(n)
    rodada = 1
    computador_inicia = computador_decide_inicio(n,m)
    while n > 0:
        print(f'**** Rodada {rodada} *****')
        if rodada % 2 != 0:
            if computador_inicia:
                n_jogada = computador_escolhe_jogada(n,m)
                n = n - n_jogada
                jogada('computador',n,n_jogada)
            else:
                n_jogada = usuario_escolhe_jogada(n,m)
                n = n - n_jogada
                jogada('jogador',n,n_jogada)
        else:
            if computador_inicia:
                n_jogada = usuario_escolhe_jogada(n,m)
                n = n - n_jogada
                jogada('jogador',n,n_jogada)
            else:
                n_jogada = computador_escolhe_jogada(n,m)
                n = n - n_jogada
                jogada('computador',n,n_jogada)
        rodada += 1
    return verifica_vitoria(rodada-1,computador_inicia)

def campeonato():
    partidas = 1
    vitorias_jogador = 0
    vitorias_comp = 0
    while partidas <= 3:
        print(f"======= {partidas}º Partida =======")
        jogador_venceu = partida()
        if jogador_venceu:
            vitorias_jogador += 1
        else:
            vitorias_comp += 1
        partidas += 1
        print('====================================')
    print(f'Placar: Você {vitorias_jogador} X {vitorias_comp} Computador.')


def set_n():
    n_flag = 0
    while n_flag == 0:
        n_temp = input('Quantas peças? ')
        if not n_temp.isdigit():
            print('Você digitou um caracter, favor digitar apenas um valor númerico inteiro.')
        elif int(n_temp) <= 0:
            print('Você digitou um valor menor ou igual a zero, favor selecionar um número válido.')
        else:
            n_temp = int(n_temp)
            n_flag = 1
    return n_temp

def set_m(n):
    m_flag = 0
    while m_flag == 0:
        m_temp = input('Limite de peças por jogada? ')
        if not m_temp.isdigit():
            print('Você digitou um caracter, favor digitar apenas um valor númerico inteiro.')
        # elif int(m_temp) >= n:
        #     print('Você digitou um valor maior ou igual o número total de peças por jogada, por gentileza digitar um valor inferior.')
        elif int(m_temp) <= 0:
            print('Você digitou um valor menor ou igual a zero, favor selecionar um número válido.')
        else:
            m_temp = int(m_temp)
            m_flag = 1
    return m_temp

def computador_decide_inicio(n,m):
        if n % (m +1) == 0:
            print('Você começa a partida.')
            return False
        else:
            print('O computador inicia a jogada.')
            return True    

def usuario_escolhe_jogada(n,m):
    flag_jogada_incorreta = 0
    while flag_jogada_incorreta == 0:
        n_jogada = int(input('Quantas peças deseja retirar? '))
        if (n_jogada > m) or (n_jogada > n):
            print('Oops! Jogada inválida! Tente de novo.')
        else:
            flag_jogada_incorreta = 1

    return n_jogada

def computador_escolhe_jogada(n,m):
    flag_jogada_comp = 0
    n_temp = m
    while flag_jogada_comp == 0: 
        if ((n -n_temp) % (m + 1) == 0):
                flag_jogada_comp = 1
        else:
            if n_temp == 0:
                n_temp = m
                flag_jogada_comp = 1
            else:
                n_temp -= 1
    if n_temp > n:
        n_temp = n
    return n_temp

def jogada(jogador,n,n_jogada):
    print(f'O {jogador} retirou {n_jogada} peças.')
    print(f'Agora restam {n} peças no tabuleiro')

def verifica_vitoria(rodada,computador_inicia):
    if (rodada) % 2 != 0:
        if computador_inicia:
            print('O computador ganhou!')
            return False
        else:
            print('Você ganhou!')
            return True
    else:
        if computador_inicia:
            print('Você ganhou!')
            return True
        else:
            print('O computador ganhou!')
            return False

inicia_jogo()