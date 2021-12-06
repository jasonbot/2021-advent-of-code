import collections


def coord_stream(line_handle):
    for line in line_handle:
        origin, end = [l.strip() for l in line.strip().split("->")]
        yield (
            tuple(int(i) for i in origin.split(",")),
            tuple(int(i) for i in end.split(",")),
        )


delta_map = {
    (True, None): (1, 0),
    (False, None): (-1, 0),
    (None, True): (0, 1),
    (None, False): (0, -1),
    (True, True): (1, 1),
    (True, False): (1, -1),
    (False, True): (-1, 1),
    (False, False): (-1, -1),
}

with open("day5.txt") as lines:
    visited_coords = collections.defaultdict(int)
    for coords in coord_stream(lines):
        (x1, y1), (x2, y2) = coords
        # Hardcode false on part 1
        diagonal = abs(x1 -x2) == abs(y1 - y2)
        if x1 == x2 or y1 == y2 or diagonal:
            # print(coords)

            x, y = x1, y1
            if x1 == x2:
                dx, dy = delta_map[(None, y2 > y1)]
                steps = abs(y2 - y1) + 1
                # print(steps, dx, dy)
            elif y1 == y2:
                dx, dy = delta_map[(x2 > x1, None)]
                steps = abs(x2 - x1) + 1
                # print(steps, dx, dy)
            else:
                dx, dy = delta_map[(x2 > x1, y2 > y1)]
                steps = abs(x2 - x1) + 1
                # print ("DIAGONAL", coords, steps, dx, dy)

            for step in range(steps):
                visited_coords[(x, y)] += 1
                # print("Visiting", x, y, dx, dy, coords, visited_coords[(x, y)])

                x += dx
                y += dy

    mv = max(visited_coords.values())
    # print(mv)
    part_1 = [(k, v) for k, v in visited_coords.items() if v >= 2]
    print(len(part_1))
