from util import print_answer
from intcode import Program


def get_joystick():
    paddle, ball = 0, 0
    for i in range(0, len(program.output_buffer), 3):
        if program.output_buffer[i+2] == 3:
            paddle = program.output_buffer[i]
        elif program.output_buffer[i+2] == 4:
            ball = program.output_buffer[i]
    if paddle == ball:
        return 0
    if paddle > ball:
        return -1
    return 1


def part1():
    program.run()
    return program.output_buffer[2::3].count(2)


def part2():
    program.reset()
    program.program[0] = 2
    while not program.finished:
        program.run([get_joystick()])

    return [program.output_buffer[i+2]
            for i in range(0, len(program.output_buffer), 3)
            if program.output_buffer[i] == -1 and program.output_buffer[i+1] == 0][-1]


if __name__ == "__main__":

    part1_correct = 315
    part2_correct = 16171

    program = Program("13")

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
