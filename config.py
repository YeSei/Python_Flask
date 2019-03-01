__author__ = "Deng Yangjie"
'''
@ID:SA18225058
@copyright:USTC
@time:''
this module is for:
'''
import os


class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = "mysql://root:dyj2468..@localhost:3306/travel"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

