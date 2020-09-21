from util import get_input, print_answer
from intcode import Program


def part1(program):
    
    # "replace position 1 with the value 12"
    program.program[1] = 12
    # "replace position 2 with the value 2"
    program.program[2] = 2

    # run program
    program.run()

    # return value at position 0
    return program.program[0]


def part2(program):
    
    for noun in range(99):
        for verb in range(99):
            
            # Reset program to initial state
            program.reset()
            
            # "the value placed in address 1 is called the noun"
            program.program[1] = noun
            # "the value placed in address 2 is called the verb"
            program.program[2] = verb
            
            program.run()
            
            # find noun and verb that cause program to output 19690720
            if program.program[0] == 19690720:
                # return 100 * noun + verb
                return 100 * noun + verb


if __name__ == "__main__":
    part1_correct = 4945026
    part2_correct = 5296

    program = Program(2)

    print_answer(1, part1(program), part1_correct)
    print_answer(2, part2(program), part2_correct)
