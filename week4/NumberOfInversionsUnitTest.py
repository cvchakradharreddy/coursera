import unittest
import random
from itertools import combinations
from week4.NumberOfInversions import number_of_inversion


def number_of_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


class MyUnitTest(unittest.TestCase):
    def test_number_of_inversions(self):
        data = random.sample(range(1, 10 ** 5), 10 ** 3)
        self.assertEqual(number_of_inversions_naive(data), number_of_inversion(data),
                         "Number of inversions didn't match")


if __name__ == '__main__':
    unittest.main()
