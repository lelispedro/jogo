import random


def print_game(errors):

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

    cars = ['Corsa',
            'Celta',
            'Astra',
            'Fox',
            'Tucson',
            'Duster',
            'Fusca',
            'Sandeiro']

    possible_category = [fruits, cars]
    category = random.choice(possible_category)

    if category == fruits:
        cat = 'Fruta'
    elif category == cars:
        cat = 'Carros'

    word = random.choice(category).lower()
    return word, cat


def set_secret_word(secret_word):
    return ['_' for x in secret_word]


def question_letter():
    letter = input('Qual letra?')
    letter = letter.strip().lower()
    return letter


def place_right_guess(guess, word_game, secret_word):
    index = 0
    for x in secret_word:
        if guess == x:
            word_game[index] = x
        index += 1


def init_game():
    secret_word, secret_category = choose_word()
    word_game = set_secret_word(secret_word)
    print('Categoria: {}'.format(secret_category))
    print(word_game)

    win = False
    lose = False
    errors = 0

    while (not win and not lose):
        guess = question_letter()
        if guess in secret_word:
            place_right_guess(guess,word_game,secret_word)
        else:
            errors += 1
            print_game(errors)

        lose = errors == 7
        win = '_' not in word_game
        print(word_game)

    if win:
        print('Parabéns você ganhou, a palavra era {}!'.format(secret_word))
    else:
        print('Você perdeu! A palavra era {}.'.format(secret_word))

init_game()