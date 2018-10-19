def print_game(game_list):
    print(' {} | {} | {}'.format(game_list[0],game_list[1],game_list[2]))
    print('-----------')
    print(' {} | {} | {}'.format(game_list[3], game_list[4], game_list[5]))
    print('-----------')
    print(' {} | {} | {}'.format(game_list[6], game_list[7], game_list[8]))

def check_winner(game_list):
    result = False

    #Verificando horizontal
    if game_list[0] == game_list[1] and game_list[0] == game_list[2] and game_list[0] != ' ':
        result = True
    if game_list[3] == game_list[4] and game_list[3] == game_list[5] and game_list[3] != ' ':
        result = True
    if game_list[6] == game_list[7] and game_list[6] == game_list[8] and game_list[6] != ' ':
        result = True

    # Verificando vertical
    if game_list[0] == game_list[3] and game_list[0] == game_list[6] and game_list[0] != ' ':
        result = True
    if game_list[1] == game_list[4] and game_list[1] == game_list[7] and game_list[1] != ' ':
        result = True
    if game_list[2] == game_list[5] and game_list[2] == game_list[8] and game_list[2] != ' ':
        result = True

    # Verificando diagonal
    if game_list[0] == game_list[4] and game_list[0] == game_list[8] and game_list[0] != ' ':
        result = True
    if game_list[2] == game_list[4] and game_list[2] == game_list[6] and game_list[2] != ' ':
        result = True

    return result

def play(game, position, player):
    if game[position] != ' ':
        print('Esta posição está ocupada escolha outra')
        return
    game[position] = player
    return

def init_game():
    game = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player = 'X'
    print('Iniciando o jogo.........')
    print('')

    while not check_winner(game):
        print_game(game)
        position = input('Qual posição de 1 a 9? ')
        if position.isnumeric() and int(position) < 9:
            position = int(position) - 1
        else:
            print('Escolha uma posição de 1 a 9')
            continue
        play(game, position, player)
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        if ' ' not in game:
            break

    if ' ' not in game:
        print('Deu velha')
        return
    if player == 'X':
        print('O jogador com O ganhou')
        print('')
        print_game(game)
    else:
        print('O jogador com X ganhou')
        print('')
        print_game(game)


init_game()