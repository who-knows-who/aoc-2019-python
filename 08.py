from util import get_input, print_answer


def get_value(layer, row, column):
    index = layer * layer_size + row * width + column
    return input[index]


def part1():
    min_0 = layer_size
    answer = 0
    for i in range(0, layers):
        start = i * layer_size
        end = start + layer_size
        layer = input[start:end]
        zeros = layer.count("0")
        if zeros < min_0:
            min_0 = zeros
            answer = layer.count("1") * layer.count("2")
    return answer


def part2():
    image = ""
    for row in range(0, height):
        for column in range(0, width):
            found = False
            layer = 0
            while not found:
                value = get_value(layer, row, column)
                if value == "0":
                    image += " "
                    found = True
                elif value == "1":
                    image += "0"
                    found = True
                else:
                    layer += 1

    out = "\n"
    for i in range(0, height):
        start = i * width
        end = start + width
        out += image[start:end] + "\n"
    return out


if __name__ == "__main__":

    part1_correct = 1742
    part2_correct = "\n 00    00 0   00000  00  " \
                    "\n0  0    0 0   00    0  0 " \
                    "\n0       0  0 0 000  0  0 " \
                    "\n0 00    0   0  0    0000 " \
                    "\n0  0 0  0   0  0    0  0 " \
                    "\n 000  00    0  0000 0  0 \n"

    width = 25
    height = 6
    layer_size = width * height

    input = get_input("08")
    layers = len(input) // layer_size

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
