import unittest
from test2 import TestFinancialServices  
from test1 import TestAccountControl       
from unittest_1 import TestAuthorize
from unittest_2 import TestCustomerService
def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFinancialServices))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAccountControl))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAuthorize))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCustomerService))

    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())