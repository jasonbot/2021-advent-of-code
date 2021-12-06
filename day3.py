import collections


def bit_stats(bitsequence):
    stats = collections.defaultdict(lambda: collections.defaultdict(int))
    for item in bitsequence:
        for index, value in enumerate(reversed(item)):
            stats[index][value] += 1

    return stats


def common_bits(bit_stats, index=-1):
    for _, statistics in sorted(bit_stats.items()):
        sorted_bit = sorted(statistics.items(), key=lambda x: -x[1])
        yield sorted_bit[index][0]


def common_int(bitsequence, index=0):
    stats = bit_stats(bitsequence)
    values = "".join(reversed(list(common_bits(stats, index=index))))
    return int(values, 2)


def gamma(bitsequence):
    return common_int(bitsequence, index=0)


def epsilon(bitsequence):
    return common_int(bitsequence, index=-1)


def bit_criteria(bitsequence, *, large):
    # To find oxygen generator rating, determine the most
    # common value (0 or 1) in the current bit position,
    # and keep only numbers with that bit in that position.
    # If 0 and 1 are equally common, keep values with a 1
    # in the position being considered.
    remaining_bits = bitsequence[:]

    bit_number = 0

    bv = None
    while len(remaining_bits) > 1:
        stats = bit_stats(remaining_bits)

        bit_value_key = stats[bit_number]
        if bit_value_key["1"] == bit_value_key["0"]:
            if large:
                bv = "1"
            else:
                bv = "0"
        elif bit_value_key["1"] > bit_value_key["0"]:
            if large:
                bv = "1"
            else:
                bv = "0"
        else:
            if large:
                bv = "0"
            else:
                bv = "1"
        remaining_bits = [b for b in remaining_bits if b[-1 - (bit_number)] == bv]

        print(bit_value_key, large, remaining_bits)

        bit_number += 1

    rv = int(remaining_bits[0], 2)
    print("!!!!", rv, remaining_bits)
    return rv


with open("day3.txt", "r") as in_handle:
    lines = [l.strip() for l in in_handle]

print(gamma(lines) * epsilon(lines))
print(bit_criteria(lines, large=True) * bit_criteria(lines, large=False))
