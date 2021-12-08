import collections

a, b, c, d, e, f, g = 1, 2, 3, 4, 5, 6, 7

digits = {
    0: {a, b, c, e, f, g},
    1: {c, f},
    2: {a, c, d, e, g},
    3: {a, c, d, f, g},
    4: {b, c, d, f},
    5: {a, b, d, f, g},
    6: {a, b, d, e, f, g},
    7: {a, c, f},
    8: {a, b, c, d, e, f, g},
    9: {a, b, c, d, f, g},
}

by_segment = collections.defaultdict(set)
by_length = collections.defaultdict(set)
for number, segments in digits.items():
    by_length[len(segments)].add(number)
    for segment in segments:
        by_segment[segment].add(number)


def parse_line(handle):
    for line in handle:
        print("L", repr(line))
        a, b = line.strip().split("|")
        inputs = [set(item.strip()) for item in a.split()]
        outputs = [set(item.strip()) for item in b.split()]

        yield inputs, outputs


def potential_segments_for_sequence(segment_chain):
    potential_segments = {}
    for item in segment_chain:
        for letter in item:
            for j in digits.values():
                if len(j) == len(item):
                    potential_segments[letter] = potential_segments.get(
                        letter, set()
                    ).union(j)
    # Now eliminate by unique length
    for item in segment_chain:
        dg = by_length[len(item)]
        print("Lookup", item, dg)
        if len(dg) == 1:
            potential_segments[letter] = list(dg)[0]
            print("Clobbering", letter, "to", potential_segments[letter])
    return potential_segments


def _combo_list(combo_chain, visited_items):
    letter, segments = combo_chain[0]
    rest = combo_chain[1:]
    for segment in segments:
        if segment not in visited_items:
            if rest:
                for tail in _combo_list(rest, visited_items.union({segment})):
                    yield ((letter, segment),) + tail
            else:
                yield ((letter, segment),)


def combinatoric_chain(potential_digits):
    items = sorted(potential_digits.items())
    for c in _combo_list(items, set()):
        yield {i[0]: i[1] for i in c}


with open("day8.txt") as handle:
    for inputs, outputs in parse_line(handle):
        print(inputs, outputs, potential_segments_for_sequence(inputs))
