import unittest
from average_scores import average_scores

class MyTestCase(unittest.TestCase):

    def test_average(self):
        #Arrange
        self.scores_dict = {"Test 1": 31, "Test 2": 34, "Test 3": 54}
        expected = 39.66666666  # 7 decimal places, remove one and see the test fail
            # Act
        actual = average_scores(self.scores_dict)
        # Assert
        self.assertAlmostEqual(expected, actual)

    def test_average_five(self):
        # Arrange
        self.scores_dict = {"Test 1": 100, "Test 2": 75, "Test 3": 50, "Test 4": 50, "Test 5": 50}
        expected = 65.0000000
        # Act
        actual = average_scores(self.scores_dict)
        # Assert
        self.assertAlmostEqual(expected, actual)

    def test_average_zero(self):
        # Arrange
        self.scores_dict = {}
        # Act
        # Assert
        with self.assertRaises(ZeroDivisionError):
            average_scores(self.scores_dict)