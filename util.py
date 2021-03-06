from re import findall


def get_input(day, strip=True, split=False, test=False):
    
    # if day/test provided as int, convert to 2 char string
    if type(day) == int:
        day = str(day).zfill(2)
    if type(test) == int:
        test = str(test).zfill(2)
    
    # open input file
    if test:
        filename = "input/test/" + day + "-" + test
    else:
        filename = "input/" + day
    with open(filename) as file:
        data = file.readlines()
    
    # process input if specified
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
        print("Part " + str(part) + " INCORRECT: expected " +
              str(expected) + ", got " + str(answer))
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
    x = [location[0] for location in dictionary]
    y = [location[1] for location in dictionary]
    min_x = min(x)
    max_x = max(x)
    min_y = min(y)
    max_y = max(y)
    return min_x, max_x, min_y, max_y


def get_orthogonal_neighbours(position):

    x, y = position
    modifiers = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    return [(x + mx, y + my) for mx, my in modifiers]


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
