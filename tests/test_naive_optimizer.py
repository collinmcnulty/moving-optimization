from unittest import TestCase
from sample.naive_optimizer import Optimizer
from sample.input_def import MoveStrategy


class TestInput(TestCase):
    def test_objective(self):
        input = [20,30,40]
        a=MoveStrategy(input)
        b=Optimizer(input)
        self.assertEqual(Optimizer.objective(input), a.objective_value)

    def test_objective_options(self):
        input = [20,30,40]
        a=MoveStrategy(input, 'time')
        b=Optimizer(input, obj='time')
        self.assertEqual(b.objective(input, 'time'), a.objective_value)