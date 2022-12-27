# The purpose of memory game is to display an amount of random numbers to the users for 0.7
# seconds and then prompt them from the user for the numbers that he remember. If he was right
# with all the numbers the user will win otherwise he will lose.
# Properties
#            1. Difficulty
# Methods
#       1. generate_sequence - Will generate a list of random numbers between 1 to 101. The list
#       length will be difficulty.
#       2. get_list_from_user - Will return a list of numbers prompted from the user. The list length
#       will be in the size of difficulty.
#       3. is_list_equal - A function to compare two lists if they are equal. The function will return
#          True / False.
#       4. play - Will call the functions above and play the game. Will return True / False if the user
#          lost or won.



import random
import time
import os
from Score import add_score
def generate_sequence(difficulty):
    # def generate_sequence(4):
    list_number = []
    x = 0
    while x < int(difficulty):
        y = random.randint(1, 101)
        if y not in list_number:
            list_number.insert(x, y)
            x += 1

    print(list_number)
    time.sleep(0.7)
    os.system('cls')
    return list_number


def get_list_from_user(difficulty):
    numbering = ['st', 'nd', 'rd', 'th', 'th']
    user_list = []
    print('You should enter the number in the same order as presented')
    x = 0
    while x < int(difficulty):
    #     user_number = int(input(f'please enter the {x + 1}{numbering[x]} number you remember \n'))
    #     user_list.append(user_number)
    #     x += 1
    # return user_list
    #     while True:  # validation of user input
         try:
            user_number = int(input(f'please enter the {x + 1}{numbering[x]} number you remember \n'))

         except ValueError:
              print('please make sure your input is a number...')
              continue
         else:
            user_list.append(user_number)
            x += 1
    return user_list
def is_list_equal(user_list, list_number):
    # a = set(user_list)
    # b = set(list_number)
    if user_list == list_number:
        print('Wow, you have one hell of photogenic memory')
        return True
    else:
        print('Sorry didn\'t nail this one, guess you are human after all')
        return False


def play(difficulty, name):
    # print(game, difficulty)
    if is_list_equal(generate_sequence(int(difficulty)), get_list_from_user(difficulty)):
        # add_score(difficulty)
        return True
    else:
        return False
# print(list_number)
# print(user_list)
