import random

def print_game(errors, word_lenght):

    print(' __________ ')
    print('|          |')

    if errors == 0:
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')

    if errors == 1:
        print('|         ( )')
        print('|')
        print('|')
        print('|')
        print('|')

    if errors == 2:
        print('|         ( )')
        print('|          |')
        print('|')
        print('|')
        print('|')

    if errors == 3:
        print('|         ( )')
        print('|         \|')
        print('|')
        print('|')
        print('|')

    if errors == 4:
        print('|         ( )')
        print('|         \|/')
        print('|')
        print('|')
        print('|')

    if errors == 5:
        print('|         ( )')
        print('|         \|/')
        print('|          |')
        print('|')
        print('|')

    if errors == 6:
        print('|         ( )')
        print('|         \|/')
        print('|          |')
        print('|         /')
        print('|')

    if errors == 7:
        print('|         ( )')
        print('|         \|/')
        print('|          |')
        print('|         / \ ')
        print('|')

def choose_word():
    fruits = ['Abacaxi',
              'Banana',
              'Mexirica',
              'Melancia',
              'Mamao',
              'Laranja',
              'Limao',
              'Morango',
              'Pera']

    word = random.choice(fruits)
    return word

def set_secret_word(secret_word):
    return ['_' for x in secret_word]






print_game()