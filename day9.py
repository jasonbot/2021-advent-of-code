import collections


def neighbor_coords(x, y, height_map):
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if x < (len(height_map[y]) - 1):
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < (len(height_map) - 1):
        neighbors.append((x, y + 1))

    return neighbors


def neighbors(x, y, height_map):
    neighbors = []
    for x, y in neighbor_coords(x, y, height_map):
        neighbors.append(height_map[y][x])
    return neighbors


def find_basins(height_map, basin_seeds):
    visited_coords = set()
    basin_crawl_queue = list(basin_seeds)
    basins = collections.defaultdict(set)

    while basin_crawl_queue:
        basin_number, (col, row) = basin_crawl_queue.pop(0)
        visited_coords.add((col, row))

        if height_map[row][col] != 9:
            basins[basin_number].add((col, row))
            for neighbor_x, neighbor_y in neighbor_coords(col, row, height_map):
                if (neighbor_x, neighbor_y) not in visited_coords and height_map[
                    neighbor_y
                ][neighbor_x] > height_map[row][col]:
                    basin_crawl_queue.append((basin_number, (neighbor_x, neighbor_y)))

    return sorted((len(x) for x in basins.values()), reverse=True)


with open("day9.txt") as in_handle:
    height_map = []

    basin_seeds = []

    for line in in_handle:
        height_map.append([int(x) for x in line.strip()])

    risk = 0
    basin_number = 0

    for row in range(len(height_map)):
        for col in range(len(height_map[row])):
            if all(n > height_map[row][col] for n in neighbors(col, row, height_map)):
                risk += height_map[row][col] + 1

                basin_seeds.append((basin_number, (col, row)))
                basin_number += 1

    print(risk)

    multiplied_area_total = None
    for basin_area in find_basins(height_map, basin_seeds)[:3]:
        if multiplied_area_total is None:
            multiplied_area_total = basin_area
        else:
            multiplied_area_total *= basin_area
    print(multiplied_area_total)