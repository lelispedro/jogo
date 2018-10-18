import velha

def start_game():
    print('Qual jogo você deseja jogar?')
    print('1) Velha')
    selector = input()
    if selector == 1 or selector.lower() == 'velha':
        velha.init_game()