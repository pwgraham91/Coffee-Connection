#!flask/bin/python
import unittest

from app import app, db
from app.models import User
from config_director import Config


class UserTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_TEST_DATABASE_URI
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_name_email(self):
        name = 'john'
        email = 'john@example.com'

        u = User(name=name, email=email)
        db.session.add(u)
        db.session.commit()

        john = db.session.query(User).one()
        self.assertEqual(john.name, name)
        self.assertEqual(john.email, email)


if __name__ == '__main__':
    unittest.main()
