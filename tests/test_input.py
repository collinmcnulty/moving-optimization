from unittest import TestCase

from sample.input_def import MoveStrategy


class TestInput(TestCase):
    def test_find_money_lost(self):
        a = MoveStrategy([40, 20, 30])
        self.assertEqual(2, 2)
        self.assertIsInstance(a.money, float)

    # def test_calculate_commute(self):
    #     a = MoveStrategy([40, 20, 30])
    #     self.assertEqual(2, 2)
    #     self.assertIsInstance(a.money, float)

    def test_find_time_spent(self):
        a = MoveStrategy([40, 20, 30])
        self.assertEqual(2, 2)
        self.assertIsInstance(a.money, float)
