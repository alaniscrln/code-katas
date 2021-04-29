import unittest
from main import range_parser

class MainTest(unittest.TestCase):
    def test_all_tokens(self):
        self.assertEqual(range_parser('1-10,14, 20-25:2'),
                          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 22, 24])

    def test_range_token(self):
        self.assertEqual(range_parser('5-10'), [5, 6, 7, 8, 9, 10])

    def test_single_token(self):
        self.assertEqual(range_parser('2'), [2])
