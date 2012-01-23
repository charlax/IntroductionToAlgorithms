#!/usr/bin/python

def is_sorted(sequence):
    return (sorted(sequence) == sequence)

def insertion_sort(sequence):
    """Returns a sorted list from a sequence."""

    # copying and making a list
    sequence = list(sequence)

    for i in range(1, len(sequence)):
        current_value = sequence[i]
        j = i
        while (current_value < sequence[j-1] and j > 0):
            j -= 1
        sequence.insert(j, sequence.pop(i))

    return sequence

if __name__ == "__main__":
    l = [3, 4, 19, 2, 10, 7, 1, 5, 8]
    sorted_list = insertion_sort(l)
    assert is_sorted(sorted_list)

    print "%s became %s" % (l, sorted_list)
