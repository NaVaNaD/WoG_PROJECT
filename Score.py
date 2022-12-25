from Utils import SCORES_FILE_NAME

#Score.py
# A package that is in charge of managing the scores file.
# The scores file at this point will consist of only a number. That number is the accumulation of the
# winnings of the user. Amount of points for winning a game is as follows:
# POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
# Each time the user is winning a game, the points he one will be added to his current amount of
# point saved in a file.
# Methods
# 1. add_score - The function’s input is a variable called difficulty. The function will try to read
# the current score in the scores file, if it fails it will create a new one and will use it to save
# the current score.


def add_score(difficulty):
    POINTS_OF_WINNING = int((difficulty * 3) + 5)
    try:
        f = open(SCORES_FILE_NAME, 'r') #try to open the file, if it doesn't exist then create it in the except'
    except FileNotFoundError :
        f = open(SCORES_FILE_NAME, 'a+')
        f.write('0')
        f.close()
        new_score = POINTS_OF_WINNING
        new_score_str = str(new_score)
        f = open(SCORES_FILE_NAME, 'w')
        f.write(new_score_str)
        f.close()
        # print(new_score)
    else:
        new_score = int(f.read()) + POINTS_OF_WINNING
        new_score_str = str(new_score)
        f = open(SCORES_FILE_NAME, 'w')
        f.write(new_score_str)
        f.close()
        # print(new_score)

# add_score(7)
