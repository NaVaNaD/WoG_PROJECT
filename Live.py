def welcome(name):
    welcome_sting = f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.'
    return welcome_sting



def load_game():
    global difficulty, game
    validation_game = False
    validation_difficulty = False
    while not validation_game:
        game = input('''Please choose a game to play:
         1.Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back 
         2.Guess Game - Guess a number and see if you choose like the computer
         3.Currency Roulette - try and guess the value of random amount of USD in ILS\n''')
        # validate input
        if game.isdigit():
            if int(game) < 1 or int(game) > 3:
                print('Ops...game number should be between 1 to 3')
                validation_game = False
            else:
                validation_game = True
        else:
            print('Ops..game number should be between 1 to 3')
            validation_game = False
    # validate input
    while not validation_difficulty:
        difficulty = input('Please choose a game difficulty from 1 to 5:\n')
        if difficulty.isdigit():
            if int(difficulty) < 1 or int(difficulty) > 5:
                print('Ops...game difficulty level should be a number between 1-5')
            else:
                validation_difficulty = True
        else:
            print('Ops...game difficulty level should be a number between 1-5')
            validation_difficulty = False
    # import play from the correct directory
    if game == '1':
        from MemoryGame import play
    if game == '2':
        from GuessGame import play
    if game == '3':
        from CurrencyRouletteGame import play

    print(play(difficulty))