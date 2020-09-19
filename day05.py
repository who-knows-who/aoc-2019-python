from util import get_input, print_answer
from intcode import make_program, execute_program_io


def part1():
    return execute_program_io(program.copy(), [1])[1][-1:][0]


def part2():
    return execute_program_io(program.copy(), [5])[1][-1:][0]


if __name__ == "__main__":

    part1_correct = 4511442
    part2_correct = 12648139

    program = make_program(get_input("05", split=True))

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
