#!flask/bin/python
import unittest
from copy import deepcopy

from app import app, db
from app.lib.connection import generate_connections, get_available_connections
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
        # return
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
        # return
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
        # return
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

    def test_get_available_connections(self):
        users = []
        u1 = User(name='john', email='john@example.com')
        self.session.add(u1)
        users.append(u1)

        u2 = User(name='mike', email='mike@example.com')
        self.session.add(u2)
        users.append(u2)

        u3 = User(name='joe', email='joe@example.com')
        self.session.add(u3)
        users.append(u3)

        u4 = User(name='steve', email='steve@example.com')
        self.session.add(u4)
        users.append(u4)

        self.session.flush()

        available_user_ids = {user.id for user in users}

        # first, test that with no connections, everyone is fair game
        self.assertEqual(get_available_connections(self.session, available_user_ids, u1), {u2.id, u3.id, u4.id})
        self.assertEqual(get_available_connections(self.session, available_user_ids, u2), {u1.id, u3.id, u4.id})
        self.assertEqual(get_available_connections(self.session, available_user_ids, u3), {u1.id, u2.id, u4.id})
        self.assertEqual(get_available_connections(self.session, available_user_ids, u4), {u1.id, u2.id, u3.id})

        # second, test that if there's a connection, that user gets removed
        cxn = Connection(user_1_id=u1.id, user_2_id=u2.id)
        self.session.add(cxn)
        # for the backrefs
        self.session.commit()

        self.assertEqual(get_available_connections(self.session, available_user_ids, u1), {u3.id, u4.id})
        self.assertEqual(get_available_connections(self.session, available_user_ids, u2), {u3.id, u4.id})
        self.assertEqual(get_available_connections(self.session, available_user_ids, u3), {u1.id, u2.id, u4.id})
        self.assertEqual(get_available_connections(self.session, available_user_ids, u4), {u1.id, u2.id, u3.id})

        # third, add a connection with u3 as user_1 and u1 as user_2
        cxn = Connection(user_1_id=u3.id, user_2_id=u1.id)
        self.session.add(cxn)
        # for the backrefs
        self.session.commit()

        available_user_ids_after_discard = get_available_connections(self.session, available_user_ids, u1)
        self.assertEqual(available_user_ids_after_discard, {u4.id})

        # fourth, add a connection with u2 as user_1 and u3 as user_2
        cxn = Connection(user_1_id=u3.id, user_2_id=u1.id)
        self.session.add(cxn)
        # for the backrefs
        self.session.commit()

        available_user_ids_after_discard = get_available_connections(self.session, available_user_ids, u1)
        self.assertEqual(available_user_ids_after_discard, {u4.id})


if __name__ == '__main__':
    unittest.main()
