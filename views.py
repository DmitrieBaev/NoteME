from main import app
from flask import render_template


@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as ex:
        return {'data': None, 'error': str(ex)}