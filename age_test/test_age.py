import unittest
from age import categorize_by_age

class TestCategorizeByAge(unittest.TestCase):
    def test_child_age(self):
        self.assertEqual(categorize_by_age(5), "Child")
    def test_teenager_age(self):
        self.assertEqual(categorize_by_age(10), "Teenager")
    def test_adult_age(self):
        self.assertEqual(categorize_by_age(30), "Adult")
    def test_golden_age(self):
        self.assertEqual(categorize_by_age(70), "Golden Age")

#python -m unittest test_age -v