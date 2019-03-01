__author__ = "Deng Yangjie"
'''
@ID:SA18225058
@copyright:USTC
@time:''
this module is for:
'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from models import User


class Store_Flights(FlaskForm):

    flightnum = StringField('flightnum', validators=[DataRequired()])
    price = StringField('price', validators=[DataRequired()])
    numseats = StringField('numseats', validators=[DataRequired()])
    numavail = StringField('numavail', validators=[DataRequired()])
    fromcity = StringField('fromcity', validators=[DataRequired()])
    arivcity = StringField('arivcity', validators=[DataRequired()])
    submit = SubmitField('store')


class Store_Hotels(FlaskForm):

    location = StringField('location', validators=[DataRequired()])
    price = StringField('price', validators=[DataRequired()])
    numrooms = StringField('numrooms', validators=[DataRequired()])
    numavail = StringField('numavail', validators=[DataRequired()])
    submit = SubmitField('store')


class Store_Cars(FlaskForm):

    location = StringField('location', validators=[DataRequired()])
    price = StringField('price', validators=[DataRequired()])
    numcars = StringField('numcars', validators=[DataRequired()])
    numavail = StringField('numavail', validators=[DataRequired()])
    submit = SubmitField('store')


class Store_Customers(FlaskForm):

    custname = StringField('custname', validators=[DataRequired()])
    submit = SubmitField('store')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class Update_Flights_left(FlaskForm):
    flightnum = StringField('flightnum')
    submit = SubmitField('search')


class Update_Flights_right(FlaskForm):
    flightnum1 = StringField('flightnum1', validators=[DataRequired()])
    flightnum2 = StringField('flightnum2', validators=[DataRequired()])
    price = StringField('price', validators=[DataRequired()])
    numseats = StringField('numseats', validators=[DataRequired()])
    numavail = StringField('numavail', validators=[DataRequired()])
    fromcity = StringField('fromcity', validators=[DataRequired()])
    arivcity = StringField('arivcity', validators=[DataRequired()])
    submit = SubmitField('update')


class Update_Hotels_left(FlaskForm):
    hotels_id = StringField('hotels_id')
    submit = SubmitField('search')


class Update_Hotels_right(FlaskForm):
    hotels_id1 = StringField('hotels_id1', validators=[DataRequired()])
    hotels_id2 = StringField('hotels_id2', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    price = StringField('price', validators=[DataRequired()])
    numrooms = StringField('numrooms', validators=[DataRequired()])
    numavail = StringField('numavail', validators=[DataRequired()])
    submit = SubmitField('update')


class Update_Cars_left(FlaskForm):
    cars_id = StringField('cars_id')
    submit = SubmitField('search')


class Update_Cars_right(FlaskForm):
    cars_id1 = StringField('cars_id1', validators=[DataRequired()])
    cars_id2 = StringField('cars_id2', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    price = StringField('price', validators=[DataRequired()])
    numcars = StringField('numcars', validators=[DataRequired()])
    numavail = StringField('numavail', validators=[DataRequired()])
    submit = SubmitField('update')


class Res_Flights_right(FlaskForm):
    username = StringField('username')
    flightnum = StringField('flightnum')
    submit = SubmitField('buy')


class Res_Hotels_right(FlaskForm):
    username = StringField('username')
    hotels_id = StringField('hotels_id')
    submit = SubmitField('buy')


class Res_cars_right(FlaskForm):
    username = StringField('username')
    cars_id = StringField('cars_id')
    submit = SubmitField('buy')


class User_Travel(FlaskForm):
    user_id = StringField('user_id')
    submit = SubmitField('search')