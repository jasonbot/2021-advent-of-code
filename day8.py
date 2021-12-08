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

def shelf_stable(item):
    return"".join(sorted(item))

length_count = collections.defaultdict(set)
intersections = collections.defaultdict(lambda: collections.defaultdict(set))

for d1, i1 in digits.items():
    length_count[len(i1)].add(d1)

    for d2, i2 in digits.items():
        if d1 + d2:
            if len(i1 & i2):
                intersections[d1][(len(i1), len(i2), len(i1 & i2))].add(d2)

by_length = {k: list(v)[0] for k, v in length_count.items() if len(v) == 1}

# print("LC", length_count)
# print("IS", intersections)
# print("BL", by_length)


def parse_line(handle):
    for line in handle:
        a, b = line.strip().split("|")
        inputs = [shelf_stable(item.strip()) for item in a.split()]
        outputs = [shelf_stable(item.strip()) for item in b.split()]

        yield inputs, outputs


def figure_out_sequences(list_of_items):
    digits = {}
    items = {}
    visited_numbers = set()

    for item in list_of_items:
        if by_length.get(len(item)):
            digits[item] = by_length[len(item)]
            items[by_length[len(item)]] = item
            visited_numbers.add(by_length[len(item)])
    
    for item in list_of_items:
        if item not in digits:
            # print("Need to find", item, digits)

            alls = None
            for d, i in digits.items():
                rk = (len(d), len(item), len(set(d) & set(item)))
                if rk in intersections[i]:
                    # print("Found it!", i, rk, intersections[i][rk])
                    ifs = intersections[i][rk]
                    ii = {j for j in ifs if j not in visited_numbers}
                    # print("II", ii)
                    if alls is None:
                        alls = ii
                    else:
                        alls &= ii
            # print("----", alls)
            assert len(alls) == 1
            an = list(alls)[0]
            visited_numbers.add(an)
            digits[item] = an
            # print("Mapps", an, digits)

    return digits


with open("day8.txt") as handle:
    totals = 0
    totals_2 = 0
    look_for = {1,4,7,8}

    for inputs, outputs in parse_line(handle):
        num = 0

        mappings = figure_out_sequences(inputs)
        for item in outputs:
            if mappings[item] in look_for:
                totals += 1
            num *= 10
            num += mappings[item]
        totals_2 += num

    print(totals)
    print(totals_2)