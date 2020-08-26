from util import print_answer
from intcode import Program


def start_computer(address):
    computer = Program("23")
    computer.run_program([address])
    return computer


def part1():

    computers = [start_computer(address) for address in range(50)]
    messages = [[] for _ in range(50)]

    while True:
        for computer in computers:
            for i in range(0, len(computer.output_buffer), 3):
                if computer.output_buffer[i] == 255:
                    return computer.output_buffer[i+2]
                messages[computer.output_buffer[i]].append(computer.output_buffer[i+1:i+3])
            if messages[computers.index(computer)]:
                input_buffer = messages[computers.index(computer)].pop(0)
            else:
                input_buffer = [-1]
            computer.run_program(input_buffer)


def part2():

    computers = [start_computer(address) for address in range(50)]

    messages = [[] for _ in range(50)]
    nat_message = None
    last_nat_y = None

    while True:
        idle = True
        for computer in computers:
            for i in range(0, len(computer.output_buffer), 3):
                idle = False
                if computer.output_buffer[i] == 255:
                    nat_message = computer.output_buffer[i+1:i+3]
                else:
                    messages[computer.output_buffer[i]].append(computer.output_buffer[i+1:i+3])
            if messages[computers.index(computer)]:
                idle = False
                input_buffer = messages[computers.index(computer)].pop(0)
            else:
                input_buffer = [-1]
            computer.run_program(input_buffer)
        if idle and nat_message is not None:
            if nat_message[1] == last_nat_y:
                return last_nat_y
            messages[0].append(nat_message)
            last_nat_y = nat_message[1]


if __name__ == "__main__":
    part1_correct = 18982
    part2_correct = 11088

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
