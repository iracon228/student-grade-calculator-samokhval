import unittest

from core import calculate_average


class TestCoreFunctions(unittest.TestCase):

    def test_calculate_average(self):
        scores = [90, 80, 70, 60]
        expected_average = 75.0
        self.assertEqual(calculate_average(scores), expected_average)

    def test_calculate_average_empty(self):
        scores = []
        expected_average = 0
        self.assertEqual(calculate_average(scores), expected_average)


if __name__ == "__main__":
    unittest.main()
