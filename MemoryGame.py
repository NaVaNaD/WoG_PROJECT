import random
import time
import os


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
        user_number = int(input(f'please enter the {x + 1}{numbering[x]} number you remember \n'))
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


def play(difficulty):
    # print(game, difficulty)
    if is_list_equal(generate_sequence(int(difficulty)), get_list_from_user(difficulty)):
        return True
    else:
        return False
# print(list_number)
# print(user_list)
