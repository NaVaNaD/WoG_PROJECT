from flask import Flask, render_template, current_app
from Utils import BAD_RETURN_CODE, SCORES_FILE_NAME
# from MainGame import name

def score_server(name): #need to check how to send the name to the  server!!!!!
    try:
        f = open(SCORES_FILE_NAME, 'r')  # try to open the file, if it doesn't exist then create it in the except'
        user_score = f.read()
        print(user_score)
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


# score_server(name)
# def score_server ():
#     app = Flask(__name__)
#     @app.route("/")
#  try:
#      return render_template('index.html',SCORE = new_score_str)
#     # return current_app.send_static_file('index.html')
#  except:
# # def error()
#    return render_template('error.html',ERROR= BAD_RETURN_CODE)
# app.run ()
#
