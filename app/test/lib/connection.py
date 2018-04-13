#!flask/bin/python
import unittest
from copy import deepcopy

from app import app, db
from app.lib.connection import generate_connections
from app.models import User, Connection
from config_director import Config


class ConnectionLibTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_TEST_DATABASE_URI
        self.app = app.test_client()
        db.create_all()
        self.session = db.session

    def tearDown(self):
        self.session.remove()
        db.drop_all()

    def validate_connections(self, user_matches):
        connections = self.session.query(Connection).all()

        for cxn in connections:
            user_matches[cxn.user_1.name].append(cxn.user_2.name)
            user_matches[cxn.user_2.name].append(cxn.user_1.name)

        for user, matches in user_matches.items():
            cant_match_with = [user]
            for match in matches:
                self.assertNotIn(match, cant_match_with)
                cant_match_with.append(match)

        return user_matches

    def test_make_connection_even_num_all_active(self):
        user_matches = {}
        u1 = User(name='john', email='john@example.com')
        self.session.add(u1)
        user_matches[u1.name] = []

        u2 = User(name='mike', email='mike@example.com')
        self.session.add(u2)
        user_matches[u2.name] = []

        u3 = User(name='joe', email='joe@example.com')
        self.session.add(u3)
        user_matches[u3.name] = []

        u4 = User(name='steve', email='steve@example.com')
        self.session.add(u4)
        user_matches[u4.name] = []

        returned_user_matches = {}
        for i in range(len(user_matches.keys()) + 10):
            generate_connections(self.session)
            returned_user_matches = self.validate_connections(deepcopy(user_matches))

        # assert that everyone has the same number of matches
        self.assertLessEqual(max(map(len, returned_user_matches.values())),
                             min(map(len, returned_user_matches.values())))

    def test_make_connection_even_num_all_active_6(self):
        user_matches = {}
        u1 = User(name='john', email='john@example.com')
        self.session.add(u1)
        user_matches[u1.name] = []

        u2 = User(name='mike', email='mike@example.com')
        self.session.add(u2)
        user_matches[u2.name] = []

        u3 = User(name='joe', email='joe@example.com')
        self.session.add(u3)
        user_matches[u3.name] = []

        u4 = User(name='steve', email='steve@example.com')
        self.session.add(u4)
        user_matches[u4.name] = []

        u5 = User(name='fred', email='fred@example.com')
        self.session.add(u5)
        user_matches[u5.name] = []

        u6 = User(name='adam', email='adam@example.com')
        self.session.add(u6)
        user_matches[u6.name] = []

        returned_user_matches = {}
        for i in range(len(user_matches.keys()) + 10):
            generate_connections(self.session)
            returned_user_matches = self.validate_connections(deepcopy(user_matches))

        # assert that everyone has the same number of matches
        self.assertLessEqual(max(map(len, returned_user_matches.values())),
                             min(map(len, returned_user_matches.values())))

    def test_make_connection_even_num_all_active_6_one_inactive(self):
        user_matches = {}
        u1 = User(name='john', email='john@example.com')
        self.session.add(u1)
        user_matches[u1.name] = []

        u2 = User(name='mike', email='mike@example.com')
        self.session.add(u2)
        user_matches[u2.name] = []

        u3 = User(name='joe', email='joe@example.com')
        self.session.add(u3)
        user_matches[u3.name] = []

        u4 = User(name='steve', email='steve@example.com')
        self.session.add(u4)
        user_matches[u4.name] = []

        u5 = User(name='fred', email='fred@example.com')
        self.session.add(u5)
        user_matches[u5.name] = []

        u6 = User(name='adam', email='adam@example.com', active=False)
        self.session.add(u6)

        returned_user_matches = {}
        for i in range(len(user_matches.keys()) + 10):
            generate_connections(self.session)
            returned_user_matches = self.validate_connections(deepcopy(user_matches))

        # assert that everyone has the same number of matches
        self.assertLessEqual(max(map(len, returned_user_matches.values())),
                             min(map(len, returned_user_matches.values())))


if __name__ == '__main__':
    unittest.main()
