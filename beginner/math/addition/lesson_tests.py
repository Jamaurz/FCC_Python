import unittest
import lesson_code

class AdditionTests(unittest.TestCase):
    def test_main(self):
        total = lesson_code.total
        self.assertIsInstance(total, int)
        self.assertEqual(total, 20)

# To run the tests from the console:
# Make sure that you are in the 'addition' directory
# ⇒  python3 -m unittest test_addition
