from util import get_input, print_answer, get_dict_coords, get_new_location
from intcode import make_program, execute_until_input
from collections import defaultdict


def turn_robot(direction, turn):
    if turn == 0:
        direction -= 1
    else:
        direction += 1
    return direction % 4


def print_panels(panels):
    min_x, max_x, min_y, max_y = get_dict_coords(panels)

    image = "\n"
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if panels[(x, y)] == 0:
                image += " "
            else:
                image += "0"
        image += "\n"
    return image


def part1():
    panels = defaultdict(int)
    painted = set()
    location = (0, 0)
    direction = 0
    program_state = (program, 0, 0)
    while True:
        exit_code, output_buffer, program_state = execute_until_input(program_state, [panels[location]])
        paint, turn = output_buffer
        panels[location] = paint
        painted.add(location)
        direction = turn_robot(direction, turn)
        location = get_new_location(location, direction)
        if exit_code == 0:
            return len(painted)


def part2():
    panels = defaultdict(int)
    location = (0, 0)
    panels[location] = 1
    direction = 0
    program_state = (program, 0, 0)
    while True:
        exit_code, output_buffer, program_state = execute_until_input(program_state, [panels[location]])
        paint, turn = output_buffer
        panels[location] = paint
        direction = turn_robot(direction, turn)
        location = get_new_location(location, direction)
        if exit_code == 0:
            return print_panels(panels)


if __name__ == "__main__":

    part1_correct = 1894
    part2_correct = "\n   00 0  0 0000 0    0000   00 000  0  0   " \
                    "\n    0 0 0     0 0       0    0 0  0 0  0   " \
                    "\n    0 00     0  0      0     0 000  0000   " \
                    "\n    0 0 0   0   0     0      0 0  0 0  0   " \
                    "\n 0  0 0 0  0    0    0    0  0 0  0 0  0   " \
                    "\n  00  0  0 0000 0000 0000  00  000  0  0   \n"

    program = make_program(get_input("11", split=True))

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
