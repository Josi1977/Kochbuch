import os

basedir = os.path.abspath(os.path.dirname(__file__))
 
 
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hate'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://JOZ:Legioni7777$$@flaskwebapp.mysql.database.azure.com:3306/kochbuch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False