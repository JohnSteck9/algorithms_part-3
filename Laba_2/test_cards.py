import unittest
from cards import *
from sorting_algo import *


# class TestFile(unittest.TestCase):
#     def test_file(self):
#         # Test file when content not eql integer
#         pass

class TestSequence(unittest.TestCase):
    def test_sequence(self):
        self.assertEqual(max_sequence([1, 2, 3]), 3)
        self.assertEqual(max_sequence([3, 2, 1]), 1)
        self.assertEqual(max_sequence([1, 1, 2, 2, 5, 3]), 2)
        self.assertEqual(max_sequence([1, 1, 2, 2, 3, 3]), 3)
        self.assertEqual(max_sequence([1]), 1)
        self.assertEqual(max_sequence([]), 0)

    # def test_joker(self):
    #     self.assertEqual()


class TestSorting(unittest.TestCase):
    def sorting(self):
        self.assertEqual(Sort.quick_sort([3, 2, 1], 0, (len(deck) - 1)), [1, 2, 3])
        self.assertEqual(Sort.quick_sort([], 0, (len(deck) - 1)), [])

        self.assertEqual(Sort.insertion_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(Sort.insertion_sort([]), [])

# class TestMain(unittest.TestCase):
#     pass


if __name__ == '__main__':
    # python -m unittest test_sort
    # python -m unittest
    # python -> import unittest -> help(unittest.TestCase.assertSetEquals)

    unittest.main()
