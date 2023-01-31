
from app import User
from passlib.hash import pbkdf2_sha256
'''
def invalid_credentials(form, field):
    """ Username and password checker """

    password = field.data
    username = form.username.data

    # Check username is invalid
    user_data = User.query.filter_by(username=username).first()
    if user_data is None:
        raise ValidationError("Username or password is incorrect")

    # Check password in invalid
    elif not pbkdf2_sha256.verify(password, user_data.hashed_pswd):
        raise ValidationError("Username or password is incorrect")

'''
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