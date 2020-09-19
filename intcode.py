from util import get_input
from collections import defaultdict


class Program:
    def __init__(self, day):
        self.day = day
        self.program_initial = make_program(get_input(day, split=True))
        self.program = self.program_initial.copy()
        self.ip = 0
        self.rb = 0
        self.output_buffer = []
        self.finished = False

    def run_program(self, input_buffer=None):
        if input_buffer is None:
            input_buffer = []
        self.finished, self.output_buffer, self.program, self.ip, self.rb = execute_intcode(
            self.program,
            self.ip,
            self.rb,
            input_buffer
        )

    def reset_program(self):
        self.program = self.program_initial.copy()
        self.ip = 0
        self.rb = 0
        self.output_buffer = []
        self.finished = False

    def restart_program(self, input_buffer=None):
        self.reset_program()
        self.run_program(input_buffer)

    def copy(self):
        copy = Program(self.day)
        copy.program = self.program.copy()
        copy.ip = self.ip
        copy.rb = self.rb
        copy.output_buffer = self.output_buffer.copy()
        copy.finsihed = self.finished
        return copy


def make_program(program_list):
    program_dict = defaultdict(int)
    for i in range(len(program_list)):
        program_dict[i] = int(program_list[i])

    return program_dict


def get_modes(full_opcode, p):
    # input:
    #   full opcode: ABCDE
    #       A = mode of parameter 3
    #       B = mode of parameter 2
    #       C = mode of parameter 1
    #       DE = opcode
    #   p: number of parameters (modes needed)
    # return:
    #   p = 1: [C]
    #   p = 2: [C, B]
    #   p = 3: [C, B, A]

    return [(full_opcode // 10 ** (i + 2)) % 10 for i in range(p)]


def get_addresses(program, ip, modes, rb=0):
    # 0 = position
    # 1 = immediate
    # 2 = relative
    addresses = []
    for mode in modes:
        ip += 1
        if mode == 0:
            addresses.append(program[ip])
        elif mode == 1:
            addresses.append(ip)
        else:
            addresses.append(program[ip] + rb)

    return addresses


def execute_intcode(program, ip=0, rb=0, input_buffer=None):
    if input_buffer is None:
        input_buffer = []
    output_buffer = []
    input_index = 0
    while True:
        full_opcode = program[ip]
        opcode = full_opcode % 100

        if opcode in [99]:
            # 0-parameter operations
            #   99 = halt
            return True, output_buffer, program, ip, rb
        elif opcode in [3, 4, 9]:
            # 1-parameter operations
            #   3 = store
            #   4 = output
            #   9 = adjust relative base
            parameter_count = 1
            modes = get_modes(full_opcode, parameter_count)
            addresses = get_addresses(program, ip, modes, rb)
            p1 = addresses[0]
            if opcode == 3:
                if input_index == len(input_buffer):
                    return False, output_buffer, program, ip, rb
                program[p1] = input_buffer[input_index]
                input_index += 1
            elif opcode == 4:
                output_buffer.append(program[p1])
            else:
                rb = rb + program[p1]
            ip += parameter_count + 1
        elif opcode in [5, 6]:
            # 2-parameter operations
            #   5 = jump-if-true
            #   6 = jump-if-false
            parameter_count = 2
            modes = get_modes(full_opcode, parameter_count)
            addresses = get_addresses(program, ip, modes, rb)
            p1 = addresses[0]
            p2 = addresses[1]
            if (opcode == 5 and program[p1] != 0) or (opcode == 6 and program[p1] == 0):
                ip = program[p2]
            else:
                ip += parameter_count + 1
        elif opcode in [1, 2, 7, 8]:
            # 3-parameter operations
            #   1 = add
            #   2 = mult
            #   7 = less than
            #   8 = equals
            parameter_count = 3
            modes = get_modes(full_opcode, parameter_count)
            addresses = get_addresses(program, ip, modes, rb)
            val_1 = program[addresses[0]]
            val_2 = program[addresses[1]]
            store = addresses[2]
            if opcode == 1:
                program[store] = val_1 + val_2
            elif opcode == 2:
                program[store] = val_1 * val_2
            elif opcode == 7 and val_1 < val_2:
                program[store] = 1
            elif opcode == 8 and val_1 == val_2:
                program[store] = 1
            else:
                program[store] = 0
            ip += parameter_count + 1
        else:
            return


def execute_until_input(program_state, input_buffer=None):
    program, ip, relative_base = program_state
    return execute_intcode(program, input_buffer, ip, relative_base)


def execute_program_io(program, input_buffer=None):
    _, output_buffer, _ = execute_intcode(program, input_buffer)
    return output_buffer


def execute_program(program):
    _, _, program_state = execute_intcode(program)
    return program_state[0]
