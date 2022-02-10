import unittest

class TestInputSex(unittest.TestCase):
    def test_sex_is_selected(self):
        """Link to the form or website to test and test with dummy data values."""

    def test_age_maximum(self):
        """Test that the input age is not above maximum"""
        self.assertGreater(self., 0, "Check that the average in not negative.")

    def test_age_minimum(self):
        """Test that the input age is not below minimum """

    def test_weight_maximum(self):
        """Test that the input weight is not above maximum"""

    def test_weight_minimum(self):
        """Test that the input weight is not below minimum"""

    def test_creatinine_maximum(self):
        """Test that the input serum creatinine is not above maximum"""

    def test_creatinine_minimum(self):
        """Test that the input serum creatinine is not below minimum"""


if __name__ == "__main__":
    unittest.main()