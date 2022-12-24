import random


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


def play(difficulty):
    generate_number(int(difficulty))
    if compare_results(get_guess_from_user(difficulty), int(difficulty)):
        return True
    else:
        return False
