from flask import Flask, url_for
from flask_moment import Moment

app = Flask(__name__)
moment = Moment(app)

from view import *
from model import *


if __name__ == '__main__':
    app.run(debug=True)
