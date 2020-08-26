from util import get_input, print_answer
from collections import deque


def part1():
    signal = [int(num) for num in input]

    for phase in range(100):
        new_signal = []
        for output_digit in range(len(signal)):
            pattern = deque([p for p in [0, 1, 0, -1] for _ in range(output_digit + 1)])
            pattern.rotate(-1)

            sum_mult = 0
            for i in signal:
                sum_mult += i * pattern[0]
                pattern.rotate(-1)
            new_signal.append(abs(sum_mult) % 10)
        signal = new_signal.copy()

    output = [str(signal[i]) for i in range(8)]
    return int(''.join(output))


def part2():
    offset = int(input[:7])
    signal = [int(num) for _ in range(10000) for num in input][offset:]

    for phase in range(100):
        for i in range(-2, -len(signal)-1, -1):
            signal[i] = (signal[i] + signal[i+1]) % 10

    output = [str(signal[i]) for i in range(8)]
    return int(''.join(output))


if __name__ == "__main__":

    part1_correct = 85726502
    part2_correct = 92768399

    input = get_input("16")

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
