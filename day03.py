from util import get_input, print_answer
from math import inf


def get_wires(line):
    wire = list()
    move = {"direction": None, "length": 0, "unchanging": 0, "start": 0, "end": 0}
    for section in line:
        direction = section[0]
        distance = int(section[1:])
        if direction in ["L", "D"]:
            distance = - distance
        if direction in ["L", "R"]:
            orientation = "H"
        else:
            orientation = "V"
        move = {"orientation": orientation,
                "unchanging": move["end"],
                "length": abs(distance),
                "start": move["unchanging"],
                "end": move["unchanging"] + distance}
        wire.append(move)
    return wire


def overlap(section_1, section_2):
    # If wire sections are not the initial sections of the wire (from (0,0)
    if not (section_1["unchanging"] == 0 and section_2["unchanging"] == 0):
        # If wire sections are perpendicular
        if section_1["orientation"] != section_2["orientation"]:
            # If section_1 unchanging between section_2 start and end
            if True in [section_1["unchanging"] in range(section_2["start"], section_2["end"], i) for i in
                        [1, -1]]:
                # If section 2 unchanging between section 1 start and end
                if True in [section_2["unchanging"] in range(section_1["start"], section_1["end"], i) for i
                            in [1, -1]]:
                    return True
    return False


def get_distance(section_i, section_j):
    if overlap(section_i, section_j):
        return abs(section_i["unchanging"]) + abs(section_j["unchanging"])
    else:
        return inf


def part1():
    return min([get_distance(i, j) for i in wires[0] for j in wires[1]])


def part2():
    min_steps = inf
    length_1 = 0
    for section_1 in wires[0]:
        length_2 = 0
        for section_2 in wires[1]:
            if overlap(section_1, section_2):
                to_overlap = abs(section_1["start"] - section_2["unchanging"]) + \
                             abs(section_2["start"] - section_1["unchanging"])
                total_steps = length_1 + length_2 + to_overlap
                min_steps = min(total_steps, min_steps)
            length_2 += section_2["length"]
        length_1 += section_1["length"]

    return min_steps


if __name__ == "__main__":
    part1_correct = 651
    part2_correct = 7534

    wires = [get_wires(line) for line in get_input("03", split=True)]

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
