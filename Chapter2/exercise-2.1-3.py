
def search(sequence, value):
    for i, v in enumerate(sequence):
        if v == value:
            return i
    
    return None

if __name__ == '__main__':
    l = [2, 4, 12, 5, 7, 8]

    assert search(l, 7) == l.index(7)
    assert search(l, 12) == l.index(12)
