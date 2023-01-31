from flask import Flask, render_template, redirect,flash, url_for
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
import os

#from flask_sqlalchemy import SQLAlchemy
import psycopg2
FLASK_DEBUG = True
load_dotenv()

#Configure app
app = Flask(__name__)
app.secret_key = 'Makku'

#Configure Data Base
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:qtzZsZgSm3NxxfcPmSAp@containers-us-west-85.railway.app:6174/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#db.init_app(app)

class User(db.Model):
    """User_model"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(100),  nullable=False)
#    hashed_pswd = db.Column(db.String(), nullable=False)

class RegistrationForm(FlaskForm):
    '''Registration form'''
    username = StringField(label='Username_label', validators=[InputRequired(message='Введите имя пользователя'),
                                                       Length(min=4, max=25, message='Имя пользователя должно быть не менее 4 и не более 15 символов')])
    password = PasswordField(label='Password_label', validators=[InputRequired(message='Введите пароль'),
                                                       Length(min=4, max=25, message='Пароль должен быть не менее 4 и не более 15 символов')])
    confirm_pswd = PasswordField(label='Confirm_pswd_label', validators=[InputRequired(message='Повторите пароль'),
                                                       EqualTo('password', message='Пароль должен совпадать')])
    submit_button = SubmitField('Создать')

    def validate_username(self, username):
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            raise ValidationError('Пользователь с таким именем существует')

#Routes
@app.route("/", methods = ['GET', 'POST'])
def index():
#    conn = psycopg2.connect("postgresql://postgres:Revcrjdvjkjltw1@localhost:5432/users")

    reg_form = RegistrationForm()

    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        user = User(username=username, password=password)

        db.session.add(user)
        db.session.commit()
        return 'Пользователь добавлен в БД'

    return render_template("index.html", form=reg_form)

'''
        # Hash password
        hashed_pswd = pbkdf2_sha256.hash(password)

        # Add username & hashed password to DB
        user = User(username=username, hashed_pswd=hashed_pswd)
        db.session.add(user)
        db.session.commit()

        flash('Registered successfully. Please login.', 'success')
        return redirect(url_for('login'))
'''



# if running this module as a standalone program (cf. command in the Python Dockerfile)

if __name__ == "__main__":
#   app.run(host="0.0.0.0")
    app.run(debug=True)