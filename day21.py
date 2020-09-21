from util import print_answer, print_ascii
from intcode import Program


def part1():
    instructions = ["",
                    "NOT C J\n",
                    "AND D J\n",
                    "NOT A T\n"
                    "OR T J\n"
                    "WALK\n"]
    ascii_instructions = [[ord(c) for c in instruction] for instruction in instructions]
    instruction_counter = 0
    while not program.finished:
        program.run(ascii_instructions[instruction_counter])
        instruction_counter += 1
        print_ascii(program.output_buffer)

    return program.output_buffer[-1]


def part2():
    program.reset()
    instructions = ["",
                    "NOT C J\n",
                    "AND D J\n",
                    "AND H J\n",

                    "NOT C T\n",
                    "AND D T\n",
                    "AND E T\n"
                    "OR T J\n"
                    
                    "NOT B T\n"
                    "AND D T\n"
                    "AND H T\n"
                    "OR T J\n"

                    "NOT A T\n"
                    "OR T J\n"
                    
                    "RUN\n"]
    ascii_instructions = [[ord(c) for c in instruction] for instruction in instructions]
    instruction_counter = 0
    while not program.finished:
        program.run(ascii_instructions[instruction_counter])
        instruction_counter += 1
        print_ascii(program.output_buffer)

    return program.output_buffer[-1]


if __name__ == "__main__":

    part1_correct = 19348359
    part2_correct = 1140850168

    program = Program("21")

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
