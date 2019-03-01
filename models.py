__author__ = "Deng Yangjie"
'''
@ID:SA18225058
@copyright:USTC
@time:''
this module is for:
'''
from sqlalchemy import create_engine
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from init import login, db

engine = create_engine("mysql://root:dyj2468..@localhost:3306/travel",
                                    encoding='utf-8', echo=True)

class Flights(db.Model):
    flightnum = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, index=True)
    numseats= db.Column(db.Integer, index=True)
    numavail = db.Column(db.Integer, index=True)
    fromcity = db.Column(db.String(64), index=True)
    arivcity = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<Flights {}>'.format(self.flightsnum)


class Hotels(db.Model):
    hotels_id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(64), index=True)
    price = db.Column(db.Integer, index=True)
    numrooms = db.Column(db.Integer, index=True)
    numavail = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Hotels {}>'.format(self.location)


class Cars(db.Model):
    cars_id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(64), index=True)
    price = db.Column(db.Integer, index=True)
    numcars = db.Column(db.Integer, index=True)
    numavail = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Cars {}>'.format(self.location)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Reservations(db.Model):
    resvkey = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True)
    resvtype = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Reservations {}>'.format(self.resvkey)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Res_Flights(db.Model):
    reskey = db.Column(db.Integer, primary_key=True)
    flightnum = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)


class Res_Hotels(db.Model):
    reskey = db.Column(db.Integer, primary_key=True)
    hotels_id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)


class Res_Cars(db.Model):
    reskey = db.Column(db.Integer, primary_key=True)
    cars_id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)


db.Model.metadata.create_all(engine)