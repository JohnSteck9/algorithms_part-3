import unittest
from cards_v2 import *
# from Laba_2.cards import *
# from Laba_2.sorting_algo import *

array1 = [1, 2, 3]
array2 = [0, 1, 2, 3]
array3 = [0, 0, 9, 10, 12, 14, 15, 40, 50]
array4 = [0, 1, 2, 4, 6, 7, 8]
array5 = [0, 0, 0, 0, 1, 3, 5, 7, 8, 10, 12, 13, 14]
array6 = [0, 0, 0, 0, 0, 1, 8, 9, 11, 1000, 1002, 1003]
array7 = [0, 0, 0, 2, 4, 5, 6, 8, 9, 20, 21, 24, 26]
array8 = [0, 0, 0, 2, 4, 5, 6, 8, 9, 20, 21, 24, 26, 28, 29, 30, 31, 32, 33]
array9 = [0, 0, 0, 0, 1, 3, 5, 7, 9, 12, 13, 16, 17, 18,
          19, 21, 22, 24, 26, 27, 29, 30, 31, 32, 34, 36, 37]
array10 = [0, 0, 1, 2, 3, 999997, 999998, 999999, 1000000]
array11 = [0, 0, 1, 2, 3, 999999, 1000000]
array12 = [0, 0, 0, 2, 3, 5, 8, 9, 10,12,20]
array13 = [0, 0, 0, 2, 4, 6, 9, 10]
array14 = [0, 0, 0]

class TestSequence(unittest.TestCase):
    def test_sequence(self):
        self.assertEqual(max_sequence(array1, joker(array1)), 3)
        self.assertEqual(max_sequence(array2, joker(array2)), 4)
        self.assertEqual(max_sequence(array3, joker(array3)), 7)
        self.assertEqual(max_sequence(array4, joker(array4)), 5)
        self.assertEqual(max_sequence(array5, joker(array5)), 12)
        self.assertEqual(max_sequence(array6, joker(array6)), 8)
        self.assertEqual(max_sequence(array7, joker(array7)), 9)
        self.assertEqual(max_sequence(array8, joker(array8)), 11)
        self.assertEqual(max_sequence(array9, joker(array9)), 17)
        self.assertEqual(max_sequence(array10, joker(array10)), 6)
        self.assertEqual(max_sequence(array11, joker(array11)), 5)
        self.assertEqual(max_sequence(array12, joker(array12)), 9)
        self.assertEqual(max_sequence(array13, joker(array13)), 7)
        self.assertEqual(max_sequence(array14, joker(array14)), 3)
if __name__ == "__main__":
    unittest.main()
