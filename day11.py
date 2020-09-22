from util import print_answer, get_dict_coords, get_new_location
from intcode import Program
from collections import defaultdict


def paint_panels(program, task):
    """
    Returns dictionary representation of panels after running painting program

    Parameters:
    program (Program object): the intcode program for day 11
    task (int): the task number (1 or 2)

    Returns:
    painted ((int, int){}): set of coordinates (x, y) for panels that have been painted at least once
    panels (dict of (int, int): int)): dict mapping coordinates (x, y) to colour of panel, 0 = black, 1 = white 
    """

    # Reset program to initial state
    program.reset()

    # Initially at (0, 0) and facing forwards
    location = (0, 0)
    direction = 0

    # Panel are be black (0) by default
    panels = defaultdict(int)

    # For task 2, initial panel should be painted white (1)
    if task == 2:
        panels[(0, 0)] = 1
        painted = {(0, 0)}
    else:
        painted = set()

    while not program.finished:

        # Run program with current panels state as input
        program.run([panels[location]])

        # Output buffer will contain 2 values:
        #   1st: colour to paint panel (0 = black, 1 = white)
        #   2nd: direction to turn (0 = 90deg left, 1 = right)
        paint, turn = program.output_buffer

        # Paint panel
        panels[location] = paint
        painted.add(location)

        # Get new direction
        direction = turn_robot(direction, turn)

        # Get new location
        location = get_new_location(location, direction)

    return painted, panels


def turn_robot(direction, turn):
    """
    Returns new direction given current direction and turn instruction

    Paramters:
    direction (int): 0 = north, 1 = east, 2 = south, 3 = west
    turn (int): 0 = 90deg anti-clockwise, 1 = 90deg clockwise

    Returns:
    int: new direction, 0 = north, 1 = east, 2 = south, 3 = west
    """

    if turn == 0:
        direction -= 1
    else:
        direction += 1
    return direction % 4


def print_panels(painted, panels):

    # Get min/max coordinates of painted panels
    x = [location[0] for location in painted]
    y = [location[1] for location in painted]
    x_min = min(x)
    x_max = max(x)
    y_min = min(y)
    y_max = max(y)

    image = "\n"
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if panels[(x, y)] == 0:
                # Represent black panels with blank space
                image += " "
            else:
                # Represent white panels with '0' (easy to read pattern)
                image += "0"
        image += "\n"
    return image


def part1(program):

    painted, _ = paint_panels(program, 1)

    # Return number of panels painted at least once
    return len(painted)


def part2(program):

    painted, panels = paint_panels(program, 2)

    # Print representation of panels to find code
    return print_panels(painted, panels)


if __name__ == "__main__":

    part1_correct = 1894
    part2_correct = "\n   00 0  0 0000 0    0000   00 000  0  0   " \
                    "\n    0 0 0     0 0       0    0 0  0 0  0   " \
                    "\n    0 00     0  0      0     0 000  0000   " \
                    "\n    0 0 0   0   0     0      0 0  0 0  0   " \
                    "\n 0  0 0 0  0    0    0    0  0 0  0 0  0   " \
                    "\n  00  0  0 0000 0000 0000  00  000  0  0   \n"

    program = Program(11)

    print_answer(1, part1(program), part1_correct)
    print_answer(2, part2(program), part2_correct)
