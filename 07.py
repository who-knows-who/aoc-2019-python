from util import get_input, print_answer
from intcode import make_program, execute_until_input
from itertools import permutations
from collections import deque


def get_signal(order):
    output_buffer = [0]
    waiting = deque()
    for setting in order:
        waiting.append({"program_state": (program.copy(), 0, 0), "input_buffer": [setting]})
    while waiting:
        amp = waiting.popleft()
        amp["input_buffer"].extend(output_buffer)
        exit_code, output_buffer, program_state = execute_until_input(amp["program_state"], amp["input_buffer"])
        if exit_code == 1:
            waiting.append({"program_state": program_state, "input_buffer": []})
    return output_buffer[0]


def part1():
    signal_orders = list(permutations(range(0, 5)))
    return max([get_signal(order) for order in signal_orders])


def part2():
    signal_orders = list(permutations(range(5, 10)))
    return max([get_signal(order) for order in signal_orders])


if __name__ == "__main__":

    part1_correct = 95757
    part2_correct = 4275738

    program = make_program(get_input("07", split=True))

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
