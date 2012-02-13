import unittest
import logging

# Number of times to indent output
# A list is used to force access by reference
__report_indent = [0]

# From Paul Butler
# http://paulbutler.org/archives/python-debugging-with-decorators/
def report(fn):
    """Decorator to print information about a function
    call for use while debugging.
    Prints function name, arguments, and call number
    when the function is called. Prints this information
    again along with the return value when the function
    returns.
    """

    def wrap(*params,**kwargs):
        call = wrap.callcount = wrap.callcount + 1

        indent = ' ' * __report_indent[0]
        fc = "%s(%s)" % (fn.__name__, ', '.join(
            [a.__repr__() for a in params] +
            ["%s = %s" % (a, repr(b)) for a,b in kwargs.items()]
        ))

        print "%s%s called [#%s]" % (indent, fc, call)
        __report_indent[0] += 1
        ret = fn(*params,**kwargs)
        __report_indent[0] -= 1
        print "%s%s returned %s [#%s]" % (indent, fc, repr(ret), call)

        return ret
    wrap.callcount = 0
    return wrap


def find_max_crossing_subarray(array, low, mid, high):
    _sum = 0
    left_sum = float("-inf")
    max_left_index = None
    for i in range(mid, low - 1, -1):
        _sum += array[i]
        if _sum > left_sum:
            left_sum = _sum
            max_left_index = i

    _sum = 0
    right_sum = float("-inf")
    max_right_index = None
    for i in range(mid + 1, high + 1):
        _sum += array[i]
        if _sum > right_sum:
            right_sum = _sum
            max_right_index = i

    return (max_left_index, max_right_index, left_sum + right_sum)

def find_max_subarray(array, low=0, high=None):
    if high == None:
        high = len(array) - 1

    if low == high:
        return (low, high, array[low])

    mid = (low + high) / 2
    (left_low, left_high, left_sum) = find_max_subarray(array, low, mid)
    (right_low, right_high, right_sum) = find_max_subarray(array, mid + 1, high)
    (crossing_low, crossing_high, crossing_sum) = find_max_crossing_subarray(array,
            low, mid, high)

    if left_sum >= right_sum and left_sum >= crossing_sum:
        return (left_low, left_high, left_sum)
    elif right_sum >= left_sum and right_sum >= crossing_sum:
        return (right_low, right_high, right_sum)
    return (crossing_low, crossing_high, crossing_sum)


class TestFindMaxSubarray(unittest.TestCase):

    def test_find_max_subarray(self):
        to_test = (
                    {"array": (4, -25, 12, -8, 39),
                    "result": (2, 4, 43)},
                    {"array": (13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, 
                        -5, -22, 15, -4, 7),
                    "result": (7, 10, 43)},
                    )
        for t in to_test:
            low, high, _sum = find_max_subarray(t["array"])
            self.assertEqual((low, high, _sum), t["result"])

if __name__ == '__main__':
    unittest.main()
