import unittest
import random
from week4.RandomQuickSort3 import random_quick_sort3


class MyUnitTest(unittest.TestCase):
    def test_random_quicksort_3(self):
        data = random.sample(range(1, 10 ** 9), 10 ** 5)
        data_copy = data.copy()
        data.sort()
        random_quick_sort3(data_copy)
        self.assertEqual(data, data_copy, "Sort result didn't match")


if __name__ == '__main__':
    unittest.main()
