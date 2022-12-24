# from GuessGame import generate_number, get_guess_from_user, compare_results
# from MemoryGame import generate_sequence, get_list_from_user, is_list_equal
# from CurrencyRouletteGame import get_money_interval, get_guess_from_user
#
# # from Live import load_game, welcome
#
#
# # game = load_game()[0]
# # game parameters get game and difficulty from load_game
# def play(game, difficulty):
#     # print(game, difficulty)
#     if game == '1':
#         print('generate')
#         if is_list_equal(generate_sequence(int(difficulty)), get_list_from_user(difficulty)):
#             return True
#         else:
#             return False
#     if game == '2':
#         print('Guess')
#         generate_number(int(difficulty))
#         # get_guess_from_user(game[1])
#         if compare_results(get_guess_from_user(difficulty), int(difficulty)):
#             return True
#         else:
#             return False
#     if game == '3':
#         guess_parameters = get_money_interval(difficulty)
#         if get_guess_from_user(guess_parameters[0], guess_parameters[1]):
#             return True
#         else:
#             return False
#
