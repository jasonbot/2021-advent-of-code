def slide_increases(filehandle, size=2):
    """Returns a sliding window of {size} integers from a filehandle"""
    last_items = (None,) * (size)
    for line in filehandle:
        next_item = int(line.strip())
        last_items = last_items[1:] + (next_item,)
        if all(i is not None for i in last_items):
            yield last_items


def sum_windows(window_sequence):
    """Returns the sum of every item in a sequence"""
    for s in window_sequence:
        yield sum(s)


def two_window(sum_sequence):
    """Just takes two items in a sequence and groups them"""
    last = None
    for item in sum_sequence:
        if last is not None:
            yield (last, item)
        last = item


with open("day1-1.txt") as in_handle:
    print(sum(1 for a, b in slide_increases(in_handle, size=2) if b > a))

with open("day1-2.txt") as in_handle:
    print(
        sum(
            1
            for a, b in two_window(sum_windows(slide_increases(in_handle, size=3)))
            if b > a
        )
    )
