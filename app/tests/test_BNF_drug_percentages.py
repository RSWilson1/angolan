"""
NAME:          test_database.py
AUTHOR:        Rob Wilson, Giovanni, Ieva
DATE:          09/02/2022
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Suite of tests for testing the dashboards new infection
               drug percentages for OpenPrescribing dataset.
"""

import unittest
#from app import app
from app.database.controllers import Database
import regex as re

class Test_BNF_Codes(unittest.TestCase):
    """Class for testing database functionality and BNF code inputs"""
    def setUp(self):
        """Run prior to each test."""
        self.db_mod = Database()

    def tearDown(self):
        """Run post each test."""
        pass

    def test_get_total_number_items(self):
        """Test that the total number of items returns the correct value."""
        self.assertEquals(self.db_mod.get_total_number_items(), 8218165, 'Test total items returns correct value')

class Test_Drug_Percentage_Tile(unittest.TestCase):
    """Class for testing database functionality and BNF code inputs"""
    def setUp(self):
        """Run prior to each test."""
        self.db_mod = Database()

    def tearDown(self):
        """Run post each test."""
        pass

    def test_get_antiB_per(self):
        """Test that the total number of items returns the correct value."""
        self.assertEquals(self.db_mod.get_antiB_per(), 82.25,
                          'Test % Antibiotics function returns correct value')

    def test_get_antiF_per(self):
        """Test that the total number of items returns the correct value."""
        self.assertEquals(self.db_mod.get_antifungal_per(), 5.22,
                          'Test % Antifungal function returns correct value')

    def test_get_antiV_per(self):
        """Test that the total number of items returns the correct value."""
        self.assertEquals(self.db_mod.get_antiviral_per(), 2.68,
                          'Test % Antivirals function returns correct value')

    def test_get_antiP_per(self):
        """Test that the total number of items returns the correct value."""
        self.assertEquals(self.db_mod.get_antiproto_per(), 9.62,
                          'Test % Antiprotozoals function returns correct value')

    def test_get_antiH_per(self):
        """Test that the total number of items returns the correct value."""
        self.assertEquals(self.db_mod.get_anthelmintics_per(), 0.23,
                          'Test % Anthelmintics function returns correct value')


if __name__ == "__main__":
    unittest.main()