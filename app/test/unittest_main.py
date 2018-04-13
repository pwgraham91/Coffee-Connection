import unittest
import os


if __name__ == '__main__':
    os.environ['TESTING'] = 'true'

    # import tests here to register them and they'll get run when this file is run
    from app.test.models.user import UserTestCase
    from app.test.models.connection import ConnectionTestCase
    from app.test.lib.connection import ConnectionLibTestCase

    unittest.main()
