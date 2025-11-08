def get_lowest_list_value(values):
    """
    Return the lowest value from the iterable 'values' using loops.
    Raises ValueError if 'values' is empty.
    """
    iterator = iter(values)
    try:
        lowest = next(iterator)
    except StopIteration:
        raise ValueError("get_lowest_list_value() arg is an empty sequence")

    for v in iterator:
        if v < lowest:
            lowest = v
    return lowest

def get_highest_list_value(values):
    """
    Return the highest value from the iterable 'values' using loops.
    Raises ValueError if 'values' is empty.
    """
    iterator = iter(values)
    try:
        highest = next(iterator)
    except StopIteration:
        raise ValueError("get_highest_list_value() arg is an empty sequence")

    for v in iterator:
        if v > highest:
            highest = v
    return highest