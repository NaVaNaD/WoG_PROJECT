# This game will use t he free currency api to get the current exchange rate from USD to ILS, will
# generate a new random number between 1-100 a will ask the user what he thinks is the value of
# the generated number from USD to ILS, depending on the user’s difficulty his answer will be
# correct if the guessed value is between the interval surrounding the correct answer
#   Properties
#       1. Difficulty
#   Methods
#       1. get_money_interval -Will get the current currency rate from USD to ILS and will
#       generate an interval as follows:
#        a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t +
#        (5 - d))
#       2. get_guess_from_user - A method to prompt a guess from the user to enter a guess of
#       value to a given amount of USD
#       3. play - Will call the functions above and play the game. Will return True / False if the user
#       lost or won.


from Score import add_score
import random

# import forex_python
from selenium import webdriver
from selenium.webdriver.common.by import By
# from forex_python.converter import CurrencyRates, get_rate
from currency_converter import CurrencyConverter

# this function taking the current USD to ILS rate

def get_money_interval(difficulty):

    c = CurrencyConverter()
    usd_ils_rate = c.convert(1, 'USD', 'ILS')

    # except:  # forex_python.converter.RatesNotAvailableError or requests.exceptions.SSLError: will try selenium
    #     my_driver = webdriver.Chrome(
    #         executable_path=r'C:\Users\AloushN\Downloads\chromedriver_win32\chromedriver.exe')
    #     my_driver.get(
    #         'https://www.google.com/search?q=usd+to+ils&oq=usd+to+ils&aqs=chrome..69i57j0i512l9.8286j1j7&sourceid=chrome&ie=UTF-8/')
    #     usd_ils_rate = my_driver.find_element(By.XPATH,
    #                                           '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text

    guess_interval = (5 - float(difficulty))

    return guess_interval, usd_ils_rate


# this function asking the user to enter his guess
def get_guess_from_user(guess_interval, usd_ils_rate):
    usd_to_guess = round(random.randint(1, 100))
    usd_ils = round(usd_to_guess * float(usd_ils_rate))
    # print(f'usd{usd_to_guess}')
    # print(f'ils {usd_ils}')
    while True:  # validation of user input
        try:
            user_currency_guess = float(input(f'How much ILS is {usd_to_guess}$?\n'))
        except ValueError:
            print('please make sure you input is a number...')
            continue
        else:
            break
    if usd_ils - guess_interval <= user_currency_guess <= usd_ils + guess_interval:  # checking if user guess is correct
        return True
    else:
        return False


def play(difficulty, name):
    guess_parameters = get_money_interval(difficulty)
    if get_guess_from_user(guess_parameters[0], guess_parameters[1]):
        # add_score(difficulty)
        return True
    else:
        return False