from util import get_input, print_answer
from intcode import make_program, execute_program_io


def part1():
    return execute_program_io(program.copy(), [1])[0]


def part2():
    return execute_program_io(program.copy(), [2])[0]


if __name__ == "__main__":

    part1_correct = 3460311188
    part2_correct = 42202

    program = make_program(get_input("09", split=True))

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
