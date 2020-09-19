from util import get_input, print_answer
from intcode import make_program, execute_program


def part1():
    program_copy = program.copy()
    program_copy[1] = 12
    program_copy[2] = 2
    return execute_program(program_copy)[0]


def part2():
    return 0


if __name__ == "__main__":
    part1_correct = 4945026
    part2_correct = 5296

    program = make_program(get_input("02", split=True))

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
