"""
NAME:          test_database.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          24/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Suite of tests for testing the dashboards database
               functionality.
"""

import unittest
#from app import app
from app.database.controllers import Database

class DatabaseTests(unittest.TestCase):
    """Class for testing database functionality and connection."""
    def setUp(self):
        """Run prior to each test."""
        self.db_mod = Database()

    def tearDown(self):
        """Run post each test."""
        pass

    def test_get_total_number_items(self):
        """Test that the total number of items returns the correct value."""
        self.assertEquals(self.db_mod.get_total_number_items(), 8218165, 'Test total items returns correct value')


class Test_ACT_return(unittest.TestCase):
    """Class for testing returned value from db."""
    def test_is_ACT_pos(self):
        """Check ACT is positive."""
        self.assertGreater(self.db_mod.get_avg_ACT_cost(), 0, "Check that the average in not negative.")

    def test_get_avg_ACT_cost(self):
        """Test that the total number of items returns the correct value."""
        self.assertEquals(self.db_mod.get_avg_ACT_cost(), 73, 'Test total items returns correct value')








if __name__ == "__main__":
    unittest.main()