import unittest
import os


# import tests here to register them and they'll get run when this file is run
from app.test.user import UserTestCase
from app.test.connection import ConnectionTestCase


if __name__ == '__main__':
    os.environ['TESTING'] = 'true'
    unittest.main()
