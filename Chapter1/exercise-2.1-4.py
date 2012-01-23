
def add_single_binary(b1, b2, carry):
    assert isinstance(b1, int) and isinstance(b2, int)

    if (b1 + b2 + carry) == 3:
        return (1, 1)
    elif (b1 + b2 + carry) == 2:
        return (1, 0)
    else:
        return (0, b1 + b2 + carry)

def add_binary(bin1, bin2):
    assert len(bin1) == len(bin2)

    result = []

    carry = 0
    for b1, b2 in zip(reversed(bin1), reversed(bin2)):
        carry, addition = add_single_binary(b1, b2, carry)
        result.insert(0, addition)

    result.insert(0, carry)

    return result

if __name__ == '__main__':
    bin1 = (1, 0, 1, 0, 1, 0)
    bin2 = (1, 1, 1, 0, 1, 1)
    addition = add_binary(bin1, bin2)

    print "%s + %s = %s" % (bin1, bin2, addition)
