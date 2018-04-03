import unittest
import os


if __name__ == '__main__':
    os.environ['TESTING'] = 'true'

    # import tests here to register them and they'll get run when this file is run
    from app.test.user import UserTestCase
    from app.test.connection import ConnectionTestCase

    unittest.main()
