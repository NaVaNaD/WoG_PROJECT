# This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with
# HTML. This will be done by using python’s flask library.
# Methods
# 1. score_server - This function will serve the score. It will read the score from the scores file
# and will return an HTML

from flask import Flask, render_template, current_app
from Utils import BAD_RETURN_CODE, SCORES_FILE_NAME
# from MainGame import name

def score_server(name): #need to check how to send the name to the  server!!!!!
    try:
        f = open(SCORES_FILE_NAME, 'r')  # try to open the file, if it doesn't exist then create it in the except'
        user_score = f.read()
        # print(user_score) for testing can be removed in production
        app = Flask(__name__)

        @app.route("/")
        def index():
            return render_template('index.html', SCORE=user_score,user_name=name)

        app.run()

    except:
        print('error')
        app = Flask(__name__)

        @app.route("/")
        def error():
            return render_template('error.html', ERROR=BAD_RETURN_CODE)

        app.run()


