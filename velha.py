def check_winner (game_list):
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

    print(result)
    return result

def print_game(game_list):
    print(' {} | {} | {}'.format(game_list[0],game_list[1],game_list[2]))
    print('-----------')
    print(' {} | {} | {}'.format(game_list[3], game_list[4], game_list[5]))
    print('-----------')
    print(' {} | {} | {}'.format(game_list[6], game_list[7], game_list[8]))


game = ['0','1','2','3','4','5','6','7','8']

check_winner(game)
print_game(game)
