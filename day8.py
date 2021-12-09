import collections

a, b, c, d, e, f, g = 1, 2, 3, 4, 5, 6, 7

segments_for_digit = {
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


# bcgda -> abcdg
def shelf_stable(item):
    return "".join(sorted(item))


digits_by_segment_count = collections.defaultdict(set)
intersection_segment_counts_for_digits = collections.defaultdict(
    lambda: collections.defaultdict(set)
)

for digit_1, segment_set_1 in segments_for_digit.items():
    digits_by_segment_count[len(segment_set_1)].add(digit_1)

    for digit_2, segment_set_2 in segments_for_digit.items():
        # Intersecting segments?
        if len(segment_set_1 & segment_set_2):
            intersection_segment_counts_for_digits[digit_1][
                (
                    len(segment_set_1),
                    len(segment_set_2),
                    len(segment_set_1 & segment_set_2),
                )
            ].add(digit_2)

known_unambiguous_digits_by_segment_count = {
    digit: list(segment_count_set)[0]
    for digit, segment_count_set in digits_by_segment_count.items()
    if len(segment_count_set) == 1
}


def parse_line(handle):
    for line in handle:
        a, b = line.strip().split("|")
        # Return all segment lists in a sorted way
        inputs = [shelf_stable(item.strip()) for item in a.split()]
        outputs = [shelf_stable(item.strip()) for item in b.split()]

        yield inputs, outputs


def figure_out_sequences(list_of_items):
    known_string_to_digit_mapping = {}
    visited_numbers = set()

    for segment_string in list_of_items:
        # Find unambiguous by segment count digits strings
        if known_unambiguous_digits_by_segment_count.get(len(segment_string)):
            known_string_to_digit_mapping[
                segment_string
            ] = known_unambiguous_digits_by_segment_count[len(segment_string)]
            visited_numbers.add(
                known_unambiguous_digits_by_segment_count[len(segment_string)]
            )

    for segment_string in list_of_items:
        # Find unknown digits (ambiguous by segment count)
        if segment_string not in known_string_to_digit_mapping:
            all_potential_digits = None
            for (
                digit_segment_string,
                digit_number,
            ) in known_string_to_digit_mapping.items():
                intersection_key = (
                    len(digit_segment_string),
                    len(segment_string),
                    len(set(digit_segment_string) & set(segment_string)),
                )
                digit_to_shared_segment_mapping = (
                    intersection_segment_counts_for_digits[digit_number][
                        intersection_key
                    ]
                )
                potential_digit_candidates = {
                    j
                    for j in digit_to_shared_segment_mapping
                    if j not in visited_numbers
                }
                # Whittle down potential number for string based on diffs
                # from known numbers
                if all_potential_digits is None:
                    all_potential_digits = potential_digit_candidates
                else:
                    all_potential_digits &= potential_digit_candidates
            assert (
                len(all_potential_digits) == 1
            ), f"Potential digits didn't winnow to one? {all_potential_digits}"
            inferred_digit_value = list(all_potential_digits)[0]
            visited_numbers.add(inferred_digit_value)
            known_string_to_digit_mapping[segment_string] = inferred_digit_value

    return known_string_to_digit_mapping


with open("day8.txt") as handle:
    part_1_total = 0
    part_2_total = 0
    digits_to_watch_for_part_1 = {1, 4, 7, 8}

    for inputs, outputs in parse_line(handle):
        computed_full_number_digit = 0

        sequence_to_digit_mapping = figure_out_sequences(inputs)
        for item in outputs:
            if sequence_to_digit_mapping[item] in digits_to_watch_for_part_1:
                part_1_total += 1
            computed_full_number_digit *= 10
            computed_full_number_digit += sequence_to_digit_mapping[item]
        part_2_total += computed_full_number_digit

    print(part_1_total)
    print(part_2_total)
