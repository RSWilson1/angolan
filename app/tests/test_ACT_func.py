
"""
NAME:          test_database.py
AUTHOR:        Rob Wilson
DATE:          09/02/2022
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Suite of tests for testing the dashboards database
               functionality.
"""

import unittest
#from app import app
from app.database.controllers import Database

class Test_ACT_return(unittest.TestCase):
    """Class for testing returned value from db."""
    def setUp(self):
        """Run prior to each test."""
        self.db_mod = Database()

    def tearDown(self):
        """Run post each test."""
        pass

    def test_is_ACT_pos(self):
        """Check ACT is positive."""
        self.assertGreater(self.db_mod.get_avg_ACT_cost(), 0, "Check that the average in not negative.")

    def test_get_avg_ACT_cost(self):
        """Test that the total number of items returns the correct value."""
        self.assertEquals(self.db_mod.get_avg_ACT_cost(), 76.22, 'Test total items returns correct value')


#class Test_unique():
#   def test_is_int():
#        self.assert
#if type (value) == tuple


if __name__ == "__main__":
    unittest.main()