from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# To be able to run flask applications, you need to export a flask_app env

# export FLASK_APP="29-flask.py"
# flask run

# You can enable debug mode to have hot reloading
# flask run --debug

# __main__ allows us to show the module where code is running

print("Running from terminal", __name__)

import random

print("Running code from module", random.__name__)


class CustomClass:
    def __init__(self):
        pass


print("Running from module", CustomClass.__name__)

# You can also run it using the __name__ attribute
if __name__ == "__main__":
    app.run(debug=True)
