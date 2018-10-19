import velha
import forca

def start_game():
    print('Qual jogo você deseja jogar?')
    print('1) Velha')
    print('2) Forca')
    selector = input()
    if selector == 1 or selector.lower() == 'velha':
        velha.init_game()
    elif selector == 2 or selector.lower() == 'forca':
        forca.init_game()
