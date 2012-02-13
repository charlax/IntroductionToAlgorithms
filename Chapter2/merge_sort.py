import unittest
import logging
import math
import pdb

def merge(A, p, q, r):
    # counting from p to q
    left = [A[i] for i in range(p, q + 1)]
    # counting from q+1 to r
    right = [A[i] for i in range(q + 1, r + 1)]
    left.append(float("inf"))
    right.append(float("inf"))

    i = 0
    j = 0
    for k in range(p, r + 1):
        if left[i] <= right [j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1

def merge_sort(A, p, r):
    if p < r:
        middle = int(math.floor((p + r) / 2.))
        merge_sort(A, p, middle)
        merge_sort(A, middle + 1, r)
        merge(A, p, middle, r)

def sort(l):
    # copying
    sorted_list = list(l)
    merge_sort(sorted_list, 0, len(l) - 1)
    return sorted_list

class TestSorted(unittest.TestCase):

    def setUp(self):
        self.lists = (
                [1,],
                [2, 3],
                [4, 3, 2, 2, 6, 7],
                [0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10],
                [12, 34, 32, 34, 32, 34, 65, 34, 1, 4, 3, 5],
                [3, 5, 6, 3, 5, 6, 7, 3, 5, 6, 3, 5, 3, 123])

    def test_sorted(self):
        for original_list in self.lists:
            sorted_list = sort(original_list)
            self.assertListEqual(sorted_list, sorted(original_list))

if __name__ == '__main__':
    pdb.run('sort([4, 3, 2, 2, 6, 7])')
    unittest.main()
