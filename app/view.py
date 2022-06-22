""" Роутер. Обрабатывает url`ы. По совместительству выступает контроллером """

from flask import render_template, request, redirect, url_for
from . import app, db
from .model import Note, Creator, Profile, Category
from .forms import SignInForm


@app.route('/')
@app.route('/index')
def index():
    # TODO: Если пользователь не авторизирован, перенаправить на /sign-in
    return redirect(url_for('signin'))


@app.route('/signin', methods=['GET', 'POST'])
def sign_in():
    # TODO: Добавить обработчик авторизации
    return render_template('base.html')


def sign_up():
    # TODO: Добавить обработчик регистрации
    pass


def sign_out():
    # TODO: Добавить обработчик logout
    pass
