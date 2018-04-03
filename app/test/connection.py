#!flask/bin/python
import unittest

from app import app, db
from app.models import User, Connection
from config_director import Config


class ConnectionTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_TEST_DATABASE_URI
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_make_connection(self):
        u1 = User(name='john', email='john@example.com')
        db.session.add(u1)

        u2 = User(name='mike', email='mike@example.com')
        db.session.add(u2)

        connection = Connection(user_1=u1, user_2=u2)
        db.session.add(connection)
        db.session.flush()

        self.assertEqual(connection.user_1_id, u1.id)
        self.assertEqual(connection.user_2_id, u2.id)

        self.assertEqual(connection.user_1.user_1s[0].id, connection.id)
        self.assertEqual(connection.user_2.user_2s[0].id, connection.id)


if __name__ == '__main__':
    unittest.main()
