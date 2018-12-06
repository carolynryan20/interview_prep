from unittest import TestCase
from euler76 import possible_sums


class TestPossible_sums(TestCase):
    def test_possible_sums_1(self):
        self.assertEqual(possible_sums(1), 0)
    def test_possible_sums_2(self):
        self.assertEqual(possible_sums(2), 1)
    def test_possible_sums_3(self):
        self.assertEqual(possible_sums(3), 2)
    def test_possible_sums_4(self):
        self.assertEqual(possible_sums(4), 4)
    def test_possible_sums_5(self):
        self.assertEqual(possible_sums(5), 6)
    def test_possible_sums_6(self):
        self.assertEqual(possible_sums(6), 10)
    def test_possible_sums_7(self):
        self.assertEqual(possible_sums(7), 14)
    def test_possible_sums_8(self):
        self.assertEqual(possible_sums(8), 21)
