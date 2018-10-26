#!flask/bin/python
from app import app
from config_director import Config

app.config.update(
    SECRET_KEY=Config.SECRET_KEY,
    WTF_CSRF_ENABLED=Config.WTF_CSRF_ENABLED,
    SQLALCHEMY_DATABASE_URI=Config.SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TEST_DATABASE_URI=Config.SQLALCHEMY_TEST_DATABASE_URI,
    SQLALCHEMY_MIGRATE_REPO=Config.SQLALCHEMY_MIGRATE_REPO
)
app.secret_key = Config.SECRET_KEY
app.run(host='0.0.0.0', debug=True, threaded=True)
