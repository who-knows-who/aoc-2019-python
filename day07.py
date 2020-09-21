from util import get_input, print_answer
from intcode import Program
from itertools import permutations
from queue import SimpleQueue


def get_signal(program, phase_setting_sequence):
    """
    Return final output of series of program copies initiated with specified phase settings

    Parameters:
    program (Program object): the intcode program for day 7
    phase_setting_sequence (int[]): list of integer phase settings

    Returns:
    int: output of final machine
    """

    queue = SimpleQueue()

    # First run should consider [0] as output buffer
    output_buffer = [0]

    for phase_setting in phase_setting_sequence:

        # Create copy of program and run with phase setting as input
        program_copy = program.copy()
        program_copy.run([phase_setting])

        # Add paused program to queue
        queue.put(program_copy)

    # Loop until all programs finish/halt
    while not queue.empty():

        # Rerun programs with output buffer as next input
        program = queue.get()
        program.run(output_buffer)

        # Get output buffer on halt/pause
        output_buffer = program.output_buffer

        # If program has paused, re-add to queue
        if not program.finished:
            queue.put((program))

    # Return final output (should only be 1 element in list)
    return output_buffer[0]


def part1(program):

    # Find maximum output with all permutations of inputs 0-5
    return max([get_signal(program, order) for order in permutations(range(0, 5))])


def part2(program):

    # Find maximum output with all permutations of inputs 5-9
    return max([get_signal(program, order) for order in permutations(range(5, 10))])


if __name__ == "__main__":

    part1_correct = 95757
    part2_correct = 4275738

    program = Program(7)

    print_answer(1, part1(program), part1_correct)
    print_answer(2, part2(program), part2_correct)
