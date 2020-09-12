class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:3201227@localhost/sql_test'
    STORAGE = 'static'
    SECURITY_PASSWORD_SALT = 'asdasdasd'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'