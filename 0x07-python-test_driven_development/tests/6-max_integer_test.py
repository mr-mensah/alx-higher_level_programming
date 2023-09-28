import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class that defines unittests for max_integer([..])."""

    def test_max_ordered_list(self):
        """function to test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_max_unordered_list(self):
        """function to test unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """function to test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_max_empty_list(self):
        """function to test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_max_one_element_list(self):
        """function to test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_max_floats(self):
        """function to test a list of floats."""
        floats = [1.33, 8.33, -7.123, 23.2, 9.0]
        self.assertEqual(max_integer(floats), 23.2)

    def test_max_ints_and_floats(self):
        """function to test a list of ints and floats."""
        ints_and_floats = [1.33, 23.5, -7, 23, 9]
        self.assertEqual(max_integer(ints_and_floats), 23.5)

    def test_max_list_of_strings(self):
        """function to test a list of strings."""
        strings = ["Bright", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_max_empty_string(self):
        """function to test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
