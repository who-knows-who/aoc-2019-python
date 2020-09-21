from util import print_answer
from intcode import Program


def part1(program):

    # run program with input [1]
    program.run([1])

    # return diagnostic code (last item in output)
    diagnostic_code = program.output_buffer[-1]
    return diagnostic_code


def part2(program):

    # return program to initial state and run with input [5]
    program.restart([5])
    
    # return diagnostic code (last item in output)
    diagnostic_code = program.output_buffer[-1]
    return diagnostic_code


if __name__ == "__main__":

    part1_correct = 4511442
    part2_correct = 12648139

    program = Program(5)

    print_answer(1, part1(program), part1_correct)
    print_answer(2, part2(program), part2_correct)
