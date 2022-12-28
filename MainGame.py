from Live import load_game, welcome

# print(welcome(input('Hello before we start can you please tell me your name?\n')))
# load_game()

name = (input('Hello before we start can you please tell me your name?\n'))
print(welcome(name))
load_game(name)

