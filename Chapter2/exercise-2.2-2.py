#!/usr/bin/python

def is_sorted(sequence, reverse=False):
    return (sorted(sequence, reverse=reverse) == sequence)

def selection_sort(sequence):
    """Returns a sorted list."""

    sequence = list(sequence)

    for j in range(len(sequence) - 1):
        minimum = sequence[j]
        index_of_minimum = j

        for i in range(j + 1, len(sequence)):
            if sequence[i] < minimum:
                minimum = sequence[i]
                index_of_minimum = i

        sequence[j], sequence[index_of_minimum] = sequence[index_of_minimum], \
                sequence[j]

    return sequence

if __name__ == "__main__":
    l = [3, 4, 19, 2, 10, 7, 1, 5, 8]

    sorted_list = selection_sort(l)
    assert is_sorted(sorted_list)
    assert all(v in sorted_list for v in l)
    print "%s became %s" % (l, sorted_list)
