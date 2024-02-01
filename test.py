import unittest

from __init__ import heap_sort

class TestHeapSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(heap_sort([]), [])

    def test_single_element(self):
        self.assertEqual(heap_sort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(heap_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(heap_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(heap_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()