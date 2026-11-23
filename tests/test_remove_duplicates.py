import unittest

from programs.remove_duplicates import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        values = [1, 2, 3, 2, 4, 1]
        result = remove_duplicates(values)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_no_duplicates(self):
        values = [1, 2, 3]

        self.assertEqual(remove_duplicates(values), [1, 2, 3])

    def test_unhashable_values(self):
        with self.assertRaises(ValueError):
            remove_duplicates([[1], [2]])


if __name__ == "__main__":
    unittest.main()