import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = "secretkey"   #os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = "postgresql://ogbfzoaaronfll:ecff3f409a340d77f10ac744e1a9bf17e8fc92c70785189375a3a9c0349c60bd@ec2-3-214-2-141.compute-1.amazonaws.com:5432/dbi0i183fng1ot" #os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False