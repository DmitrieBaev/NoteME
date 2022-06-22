from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class SignInForm(FlaskForm):
    email = StringField('E-mail', validators=[Email()])
    pwd = PasswordField('Пароль', validators=[DataRequired(), Length(min=8, max=24)])
    remember_me = BooleanField('Запомнить меня', default=False)
    submit = SubmitField('Войти')
