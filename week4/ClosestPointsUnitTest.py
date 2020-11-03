import unittest
import random
from week4 import ClosestPoints


class MyUnitTest(unittest.TestCase):
    def test_random(self):
        data = [[random.randint(-1 * 10 ** 9, 10 ** 9), random.randint(-1 * 10 ** 9, 10 ** 9)] for _ in range(10 ** 5)]
        print("success:{}".format(ClosestPoints.get_closest_distance(data)))
        self.assertTrue(True)

    def test_same(self):
        data = [[2222, 3333] for _ in range(10 ** 5)]
        print("success:{}".format(ClosestPoints.get_closest_distance(data)))
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
