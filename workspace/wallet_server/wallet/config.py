import os 
from wallet.secret import csrf_token_secret

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
    os.path.join(BASE_DIR,'wallet.db')
)

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = csrf_token_secret

#비밀번호 최소 길이
MIN_LENGTH_OF_PASSWD = 7


