from util import print_answer
from intcode import Program


def try_y(y):

    box_size = 100
    x = int(0.75 * y)
    program.restart_program([x, y])

    # Find first x coordinate in tractor beam
    while program.output_buffer[0] == 0:
        x += 1
        program.restart_program([x, y])
    x_min = x

    # Find last x coordinate in tractor beam
    while program.output_buffer[0] == 1:
        x += 1
        program.restart_program([x, y])
    x_max = x - 1

    # If too narrow for box return -1
    if x_max - x_min < (box_size-1):
        return -1, None

    # If beam shorter than box (from furthest right x) return -1
    program.restart_program([x_max - (box_size-1), y + (box_size-1)])
    if program.output_buffer[0] == 0:
        return -1, None

    # If beam taller than box (from furthest right x) return 1
    program.restart_program([x_max - (box_size-1), y + box_size])
    if program.output_buffer[0] == 1:
        return 1, None

    # If beam same height as box (from furthest right x) return 0
    # and coordinates of top left corner
    return 0, (x_max - (box_size-1), y)


def part1():
    count = 0
    for y in range(50):
        for x in range(50):
            program.reset_program()
            program.run_program([x, y])
            if program.output_buffer[0] == 1:

                count += 1
        #         print('#', end='')
        #     else:
        #        print('.', end='')
        # print()
    return count


def part2():
    min_y, max_y = 1800, 2000

    # Used to check/adjust min/max
    # while try_y(min_y)[0] == 1:
    #     min_y = int(0.9 * min_y)
    # while try_y(max_y)[0] == -1:
    #     max_y = int(1.1 * max_y)
    # print(min_y, try_y(min_y))
    # print(max_y, try_y(max_y))

    # Find a y value where the box will fit
    # Binary search the space
    while True:
        mid_y = (min_y + max_y) // 2
        size, feasible_corner = try_y(mid_y)
        if size == -1:
            min_y = mid_y
        elif size == 1:
            max_y = mid_y
        else:
            break

    # Decrement y until it just fits (size == 0 or next size == -1)
    while True:
        mid_y -= 1
        size, corner = try_y(mid_y)
        if size in [0, 1]:
            feasible_corner = corner
        if size == -1:
            return feasible_corner[0] * 10000 + feasible_corner[1]


if __name__ == "__main__":

    part1_correct = 112
    part2_correct = 18261982

    program = Program("19")

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)