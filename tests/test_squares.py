import unittest

from programs.squares import calculate_squares


class TestSquares(unittest.TestCase):

    def test_squares(self):
        result = calculate_squares()

        expected = [number ** 2 for number in range(1, 21)]

        self.assertEqual(result, expected)

    def test_result_length(self):
        result = calculate_squares()

        self.assertEqual(len(result), 20)

    def test_first_and_last_values(self):
        result = calculate_squares()

        self.assertEqual(result[0], 1)
        self.assertEqual(result[-1], 400)


if __name__ == "__main__":
    unittest.main()