from util import get_input, print_answer, get_dict_coords
from intcode import Program
from collections import defaultdict


def get_new_location(position, direction):
    x, y = position
    # 1 = north
    if direction == 1:
        return x, y + 1
    # 2 = south
    elif direction == 2:
        return x, y - 1
    # 3 = west
    elif direction == 3:
        return x - 1, y
    # 4 = east
    else:
        return x + 1, y


def print_map(area):
    min_x, max_x, min_y, max_y = get_dict_coords(area)
    image = "\n"
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) == (0, 0):
                image += "*"
            elif area[(x, y)] == '':
                image += ' '
            else:
                image += area[(x, y)]
        image += "\n"
    print(image)


def get_direction(position, area, visited):

    possible = []

    for direction in range(1, 5):
        new_position = get_new_location(position, direction)
        if area[new_position] == "":
            return direction
        if area[new_position] != "#":
            possible.append((direction, visited[new_position]))

    min_visits = min([i[1] for i in possible])
    for i in possible:
        if i[1] == min_visits:
            return i[0]


def map_area():

    position = (0, 0)
    area_map = defaultdict(str)
    visited = defaultdict(int)

    for _ in range(10000):
        direction = get_direction(position, area_map, visited)
        new_position = get_new_location(position, direction)
        game.run_program([direction])

        if game.output_buffer[0] == 0:
            area_map[new_position] = "#"
        elif game.output_buffer[0] == 1:
            position = new_position
            area_map[position] = "."
        elif game.output_buffer[0] == 2:
            position = new_position
            area_map[position] = "O"
        visited[position] += 1

    return area_map


def find_oxygen():
    min_x, max_x, min_y, max_y = get_dict_coords(area)
    return set((x, y) for x in range(min_x, max_x + 1) for y in range(min_y, max_y + 1) if area[(x, y)] == "O")


def find_empty_neighbours(position, oxygen_map):
    return set(get_new_location(position, direction) for direction in range(1, 5)
               if oxygen_map[get_new_location(position, direction)] == ".")


def part1():
    return 0


def part2():
    oxygen_map = area.copy()
    tiles = find_oxygen()
    new_tiles = set()
    time = -1

    while tiles:
        for tile in tiles:
            oxygen_map[tile] = "O"
            new_tiles = new_tiles.union(find_empty_neighbours(tile, oxygen_map))
        tiles = new_tiles.copy()
        new_tiles.clear()
        time += 1
    return time


if __name__ == "__main__":

    part1_correct = 204
    part2_correct = 340

    game = Program("15")
    area = map_area()
    print_map(area)

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
