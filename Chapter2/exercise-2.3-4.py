import unittest
import logging
import pdb
import random

def binary_search_recursive(l, value, low=0, high=None):
    """Return True if value is in sorted list l."""

    if high is None:
        high = len(l) - 1
    if high < low:
        return False

    middle = (low + high) / 2

    #logging.warning("Searching for %d in %s, in list[%d:%d] = %s, middle: list[%d] = %d" % (value, l, low, high+1, l[low:high+1], middle, l[middle]))

    if value < l[middle]:
        return binary_search_recursive(l, value, low, middle - 1)
    elif value > l[middle]:
        return binary_search_recursive(l, value, middle + 1, high)
    else:
        return True

def binary_search_iterative(l, value):
    lo, hi = 0, len(l) - 1

    while lo <= hi:
        middle = (hi + lo) / 2
        #logging.warning("Searching for %d in %s, in list[%d:%d] = %s, middle: list[%d] = %d" % (value, l, lo, hi+1, l[lo:hi+1], middle, l[middle]))

        if value > l[middle]:
            lo = middle + 1
        elif value < l[middle]:
            hi = middle - 1
        else:
            return True
        
    return False


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.lists = []

        for i in range(10):
            number_of_items = random.randrange(20)
            self.lists.append(sorted(random.sample(range(100), number_of_items)))

    def test_search(self):
        for l in self.lists:
            value = random.randrange(100)
            if value in l:
                self.assertTrue(binary_search_iterative(l, value))
                self.assertTrue(binary_search_recursive(l, value))
            else:
                self.assertFalse(binary_search_iterative(l, value))
                self.assertFalse(binary_search_recursive(l, value))

if __name__ == '__main__':
    #pdb.run("binary_search_iterative(2, [3, 4, 5])")
    unittest.main()
