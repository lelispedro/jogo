def print_game(errors):

    print(' __________ ')
    print('|          |')

    if errors == 0:
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|__________')

    if errors == 1:
        print('|         ( )')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|__________')

    if errors == 2:
        print('|         ( )')
        print('|          |')
        print('|')
        print('|')
        print('|')
        print('|__________')

    if errors == 3:
        print('|         ( )')
        print('|         \|')
        print('|')
        print('|')
        print('|')
        print('|__________')

    if errors == 4:
        print('|         ( )')
        print('|         \|/')
        print('|')
        print('|')
        print('|')
        print('|__________')

    if errors == 5:
        print('|         ( )')
        print('|         \|/')
        print('|          |')
        print('|')
        print('|')
        print('|__________')

    if errors == 6:
        print('|         ( )')
        print('|         \|/')
        print('|          |')
        print('|         /')
        print('|')
        print('|__________')

    if errors == 7:
        print('|         ( )')
        print('|         \|/')
        print('|          |')
        print('|         / \ ')
        print('|')
        print('|__________')



print_game(7)