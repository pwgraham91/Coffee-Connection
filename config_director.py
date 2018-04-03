import os


basedir = os.path.abspath(os.path.dirname(__file__))


class TestConfig:
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'secret'

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/coffee_connection'
    SQLALCHEMY_TEST_DATABASE_URI = 'postgresql://localhost/coffee_connection_test'
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

    class Auth:
        CLIENT_ID = 'clientid'
        CLIENT_SECRET = 'client_secret'
        REDIRECT_URI = 'http://75c05ee7.ngrok.io/gCallback'
        AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
        TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
        USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'

    ENVIRONMENT = 'test'


Config = TestConfig


if not os.environ.get('TESTING'):
    # import these variables from the other config
    from config import RealConfig
    Config = RealConfig
