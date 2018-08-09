
def mask1(bytearr):
    """Returns a mask of 122 bits"""
    word_mask = 0
    for c in bytearr:
        word_mask |= 1 << c
    return word_mask


def mask2(bytearr):
    """Returns a mask of 83 bits"""
    word_mask = 0
    for c in bytearr:
        word_mask |= 1 << (c - 39)
    return word_mask


def mask3(bytearr):
    """Returns a mask of 27 bits"""
    word_mask = 0
    for c in bytearr:
        word_mask |= 1 << ((c - 39) or 57)
    return (word_mask >> 57)
