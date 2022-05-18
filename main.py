from flask import Flask, url_for
from flask_moment import Moment
from flaskext.markdown import Markdown

app = Flask(__name__)
moment = Moment(app)
Markdown(app)

from view import *
from model import *


if __name__ == '__main__':
    app.run(debug=True)

    from controller import cntl_delete_notes
    cntl_delete_notes()
