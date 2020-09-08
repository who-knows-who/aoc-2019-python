from re import findall


def get_input(name, strip=True, split=False):
    with open("input/" + name) as file:
        data = file.readlines()
    if strip:
        data = [x.strip() for x in data]
    if split:
        data = [x.split(',') for x in data]
    if len(data) == 1:
        return data[0]
    return data


def print_answer(part, answer, expected=None):

    if answer == expected:
        print("Part " + str(part) + " CORRECT: " + str(answer))
    elif expected is not None:
        print("Part " + str(part) + " INCORRECT: expected " + str(expected) + ", got " + str(answer))
    else:
        print("Part " + str(part) + ": " + str(answer))


def extract_ints(line):
    return [int(x) for x in findall(r'-?\d+', line)]


def gcd(x, y):
    while y:
        x, y = y, x % y
    return abs(x)


def lcm(x, y):
    return x * y // gcd(x, y)


def get_dict_coords(dictionary):
    x = [location[0] for location in dictionary.keys()]
    y = [location[1] for location in dictionary.keys()]
    min_x = min(x)
    max_x = max(x)
    min_y = min(y)
    max_y = max(y)
    return min_x, max_x, min_y, max_y

def get_orthogonal_neighbours(position):
    (x, y) = position
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def get_new_location(position, direction):
    x, y = position
    if direction == 0:
        return x, y - 1
    elif direction == 1:
        return x + 1, y
    elif direction == 2:
        return x, y + 1
    else:
        return x - 1, y


def print_ascii(chars):

    for c in chars:
        try:
            print(chr(c), end='')
        except ValueError:
            return
