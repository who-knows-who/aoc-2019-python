from util import get_input, print_answer, get_new_location


def adjacent(position, bugs):
    return sum([1 for direction in range(4) if get_new_location(position, direction) in bugs])


def get_neighbours(position):
    x, y, z = position
    neighbours = [get_new_location((x, y), direction) for direction in range(4)]
    neighbours = [(x_new, y_new, z) for (x_new, y_new) in neighbours if (x, y) != (2, 2)]

    if (x, y) == (2, 1):
        return neighbours + [(x_new, 0, z + 1) for x_new in range(5)]

    if (x, y) == (3, 2):
        return neighbours + [(4, y_new, z + 1) for y_new in range(5)]

    if (x, y) == (2, 3):
        return neighbours + [(x_new, 4, z + 1) for x_new in range(5)]

    if (x, y) == (1, 2):
        return neighbours + [(0, y_new, z + 1) for y_new in range(5)]

    # Top edge
    if y == 0:
        neighbours.append((2, 1, z - 1))

    # Right edge
    if x == 4:
        neighbours.append((3, 2, z - 1))

    # Bottom edge
    if y == 4:
        neighbours.append((2, 3, z - 1))

    # Left edge
    if x == 0:
        neighbours.append((1, 2, z - 1))

    return neighbours


def adjacent3(position, bugs):
    return sum([1 for neighbour in get_neighbours(position) if neighbour in bugs])


def print_bugs(bugs):
    for z in range(-5, 6):
        print("level", z)
        for y in range(5):
            for x in range(5):
                if (x, y, z) in bugs:
                    print("#", end='')
                else:
                    print(".", end='')
            print()


def part1():

    bugs = set((x, y) for x in range(5) for y in range(5) if input[y][x] == "#")
    biodiversities = []

    while True:
        adjacent_1 = set((x, y) for x in range(5) for y in range(5) if adjacent((x, y), bugs) == 1)
        adjacent_2 = set((x, y) for x in range(5) for y in range(5) if adjacent((x, y), bugs) in [1, 2])

        bugs = set((x, y) for x in range(5) for y in range(5) if
                   (x, y) in bugs and (x, y) in adjacent_1 or
                   (x, y) not in bugs and (x, y) in adjacent_2)

        biodiversity = sum([2**(5*y+x) for (x, y) in bugs])
        if biodiversity in biodiversities:
            return biodiversity
        biodiversities.append(biodiversity)


def part2():
    bugs = set((x, y, 0) for x in range(5) for y in range(5) if input[y][x] == "#")

    for minute in range(200):
        levels = range(-minute-1, minute+2)
        adjacent_1 = set((x, y, z)
                         for x in range(5)
                         for y in range(5)
                         for z in levels
                         if adjacent3((x, y, z), bugs) == 1)

        adjacent_2 = set((x, y, z)
                         for x in range(5)
                         for y in range(5)
                         for z in levels
                         if adjacent3((x, y, z), bugs) in [1, 2])

        bugs = set((x, y, z) for x in range(5) for y in range(5) for z in levels if
                   (x, y, z) in bugs and (x, y, z) in adjacent_1 or
                   (x, y, z) not in bugs and (x, y, z) in adjacent_2)

    return len(bugs)


if __name__ == "__main__":

    part1_correct = 2130474
    part2_correct = 1923

    input = get_input("24")

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
