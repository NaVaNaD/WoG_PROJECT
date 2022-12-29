
# The purpose of guess game is to start a new game, cast a random number between 1 to a
# variable called difficulty. The game will get a number input from the
# Properties :
#   1. Difficulty
#   2. Secret number

# 1. generate_number - Will generate number between 1 to difficulty and save it to
# secret_number.
# 2. get_guess_from_user - Will prompt the user for a number between 1 to difficulty and
# return the number.
# 3. compare_results - Will compare the the secret generated number to the one prompted
# by the get_guess_from_user.
# 4. play - Will call the functions above and play the game. Will return True / False if the user
# lost or won.

import random
from Score import add_score


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    validation_guess = False
    while not validation_guess:
        user_guess = input(f'Please guess a number between 1 and {difficulty}')
        if user_guess.isdigit():
            validation_guess = True
            return user_guess
        else:
            print('You must enter a number between 1 and {difficulty}, please try again.')


def compare_results(user_guess, secret_number):
    if int(user_guess) == int(secret_number):
        print('Wow, correct are you related to Uri Geller?')
        return True
    else:
        print(f'Sorry, the number is not correct. the correct number is {secret_number}')
        return False


def play(difficulty, name):
    generate_number(int(difficulty))
    if compare_results(get_guess_from_user(difficulty), int(difficulty)):
        # add_score(difficulty)
        return True
    else:
        return False

