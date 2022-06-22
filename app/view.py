""" Роутер. Обрабатывает url`ы """

from . import app
from .controller import *
from flask import render_template, request, redirect


@app.route('/')
def index():
    # TODO: Если пользователь не авторизирован, перенаправить на /sign-in
    pass
