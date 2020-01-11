import unittest
import random
from AvgCalculate import AvgCalculate


class TestAvg(unittest.TestCase):

    def setUp(self):
        self.a = AvgCalculate()

    def test_predefine_numbers(self):
        self.a.update(1)
        self.a.update(2)
        self.a.update(3)
        self.a.update(4)
        self.assertEqual(self.a.getAvg(), 2.5)

    def test_negative_numbers(self):
        self.a.update(-19)
        self.a.update(-82)
        self.a.update(-37)
        self.a.update(-64)
        self.a.update(55)
        self.assertEqual(self.a.getAvg(), -29.4)

    def test_random_numbers(self):
        random.seed(1)
        _sum = 0

        for x in range(0, 10):
            tmp = random.randint(-100, 100)
            self.a.update(tmp)
            _sum += tmp
        self.assertEqual(self.a.getAvg(), (_sum / 10))

    def test_casting_and_errors(self):
        self.a.update("10")
        self.a.update("twenty")
        self.a.update("30")
        self.a.update(40)
        self.a.update(50.0)
        self.assertEqual(self.a.getAvg(), 32.5)


if __name__ == '__main__':
    unittest.main()
