import unittest
from module1 import Account, AccountControl  # Assuming these are in module1
from your_module import Authorize  # Replace with the actual module name

class MockAccountControl:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

class TestAuthorize(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up class resources for TestAuthorize")
        cls.mock_account_control = MockAccountControl()

    @classmethod
    def tearDownClass(cls):
        print("Tearing down class resources for TestAuthorize")
        del cls.mock_account_control

    def setUp(self):
        self.authorize = Authorize('123456', 'password123', self.mock_account_control)
        self.authorize.add_user('user1', 'pass1')
        self.authorize.add_user('user2', 'pass2')

    def tearDown(self):
        del self.authorize

    def test_add_user(self):
        self.assertIn('user1', self.authorize.accounts)
        self.assertIn('user2', self.authorize.accounts)
        self.assertNotIn('user3', self.authorize.accounts)
        self.assertEqual(self.authorize.accounts['user1'], 'pass1')

    def test_login_logout(self):
        self.assertTrue(self.authorize.login('user1', 'pass1'))
        self.assertEqual(self.authorize.current_user, 'user1')
        self.authorize.logout()
        self.assertIsNone(self.authorize.current_user)
        self.assertFalse(self.authorize.login('user1', 'wrongpass'))

    def test_delete_account(self):
        self.authorize.delete_account('user2')
        self.assertNotIn('user2', self.authorize.accounts)
        self.assertIn('user1', self.authorize.accounts)  # user1 should still exist
        self.assertIsNone(self.mock_account_control.accounts.get('user2'))

    def test_check_login_status(self):
        self.authorize.login('user1', 'pass1')
        self.assertEqual(self.authorize.current_user, 'user1')
        self.authorize.logout()
        self.assertIsNone(self.authorize.current_user)

if __name__ == '__main__':
    unittest.main()