import os

DEBUG = True

SECRET_KEY = os.urandom(24)

HOSTNAME = 'localhost'
PORT = '3306'
DATABASE = 'blog_demo'
USERNAME = 'root'
PASSWORD = '11223.'
DB_URI = "mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
