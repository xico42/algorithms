import unittest

from sort import insertion_sort


class SortTest(unittest.TestCase):
    def test_insertion_sort_ascending(self):
        data = [8, 9, 10, 7, 3, 2, 1]
        insertion_sort(data)
        self.assertEqual([1, 2, 3, 7, 8, 9, 10], data)

    def test_insertion_sort_descending(self):
        data = [8, 9, 10, 7, 3, 2, 1]
        insertion_sort(data, True)
        self.assertEqual([10, 9, 8, 7, 3, 2, 1], data)


if __name__ == '__main__':
    unittest.main()
