from util import get_input, print_answer
from intcode import Program


def part1():
    program = Program("17")
    program.run()

    x, y = (0, 0)
    scaffold = []
    for c in program.output_buffer:
        print(chr(c), end='')
        if chr(c) == "\n":
            y += 1
            x = 0
            continue
        elif chr(c) in ["#", "^", "v", "<", ">"]:
            scaffold.append((x, y))
        x += 1

    intersections = [(x, y) for (x, y) in scaffold if
                     (all(neighbour in scaffold for neighbour in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]))]

    return sum([(x * y) for (x, y) in intersections])


def part2():
    program = Program("17")
    program.program[0] = 2
    main = "A,B,A,B,C,B,C,A,B,C\n"
    a = "R,4,R,10,R,8,R,4\n"
    b = "R,10,R,6,R,4\n"
    c = "R,4,L,12,R,6,L,12\n"
    camera = "n\n"

    input_buffer = []
    [input_buffer.extend(ord(c) for c in routine) for routine in [main, a, b, c, camera]]

    program.run(input_buffer)
    return program.output_buffer[-1]


if __name__ == "__main__":

    part1_correct = 5788
    part2_correct = 648545

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
