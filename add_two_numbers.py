import unittest
"""

Title:

    Add two numbers with Python.

Description/Explanation/Lesson:

    In Python, an integer (int) is one of 3 distinct numeric types.
    In this exercise, you will add two integers using the plus (+) operator.

Code Prompt/Challenge:

    Change the 0 so that total will equal 20.

Pre-defined Code:

    total = 10 + 0

Solution:

    total = 10 + 10

Tests:

    self.assertIsInstance(total, int)
    self.assertEqual(total, 20)

"""

total = 10 + 10

class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(total, int)
        self.assertEqual(total, 20)

if __name__ == '__main__':
    unittest.main()
