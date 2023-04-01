import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

while True:
    player_move = input('Choose [r]ock, [p]aper or [s]cissors (or type [q]uit to exit): ')

    if player_move == 'q':
        print('Thanks for playing!')
        break

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        print('Invalid Input. Try again..')
        continue

    computer_random_number = random.randint(1, 3)

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print('You win!')
    elif player_move == computer_move:
        print('Draw!')
    else:
        print('You lose!')

    play_again = input('Do you want to play again? [y/n]: ')

    if play_again == 'n':
        print('Thanks for playing!')
        break