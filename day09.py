from util import print_answer
from intcode import Program


def part1(program):

    # Run in test mode by providing value 1
    program.run([1])

    # Return BOOST keycode (single element in output buffer)
    return program.output_buffer[0]


def part2(program):

    # Resest program and run in sensor boost mode by providing value 2
    program.restart([2])

    # Return coordinates of distress signal (single element in output buffer)
    return program.output_buffer[0]


if __name__ == "__main__":

    part1_correct = 3460311188
    part2_correct = 42202

    program = Program(9)

    print_answer(1, part1(program), part1_correct)
    print_answer(2, part2(program), part2_correct)
