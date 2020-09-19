from util import get_input, print_answer
from functools import reduce


def cut(deck, value):
    return deck[value:] + deck[:value]


def increment(deck, value):
    new_deck = [0 for _ in range(len(deck))]
    for i in range(len(deck)):
        new_deck[value * i % len(deck)] = deck[i]
    return new_deck


def new(deck):
    return deck[::-1]


def reverse_cut(value, position, deck_size):
    return (value + position + deck_size) % deck_size


def reverse_increment(value, position, deck_size):

    # return modinv(value, deck_size) * position % deck_size
    # modulus (deck size) is prime so can find modular multiplicative inverse with:
    # y = x**(m-2) mod m
    return pow(value, deck_size-2, deck_size) * position % deck_size


def reverse_new(position, deck_size):
    return deck_size - 1 - position


def shuffle(deck, instruction):

    if instruction[0] == "cut":
        return cut(deck, int(instruction[1]))
    elif instruction[1] == "with":
        return increment(deck, int(instruction[3]))
    else:
        return new(deck)


def reverse_shuffle(position, deck_size, instructions):
    for instruction in instructions:
        if instruction[0] == "cut":
            position = reverse_cut(int(instruction[1]), position, deck_size)
        elif instruction[1] == "with":
            position = reverse_increment(int(instruction[3]), position, deck_size)
        else:
            position = reverse_new(position, deck_size)
    return position


def part1():

    deck = [[x for x in range(10007)]]
    deck = reduce(shuffle, deck + shuffles)
    return deck.index(2019)


def part2():

    deck_size = 119315717514047
    iterations = 101741582076661

    instructions = shuffles[::-1]

    # https://www.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions/fbnifwk/
    # X = 2020
    position = 2020
    # Y = f(X)
    position_2 = reverse_shuffle(position, deck_size, instructions)
    # Z = f(Y) = f(f(X))
    position_3 = reverse_shuffle(position_2, deck_size, instructions)

    # Find integers A, B such that f(x) = A * x + B
    # Y = A*X+B, Z = A*Y+B
    # Y-Z = A*(X-Y)
    # A = (Y-Z)/(X-Y)
    # instead of dividing, multiply by modular inverse then take modulus
    a = (position_2-position_3) * pow(position-position_2, deck_size-2, deck_size) % deck_size
    b = (position_2 - a * position) % deck_size

    # f(x) = A*x+B
    # f(f(x)) = A*(A*x+B)+B
    #         = A^2 * x + A * B + B
    # f(f(f(x))) = A*(A*(A*x+B)+B)+B
    #            = A^3 * x + A^2 * B + A * B + B
    # f**n(x) = A^n * x + (A^(n-1) + A^(n-2) + ... + 1) * B     (FINITE POWER SERIES)
    #         = A^n * x + (1 - A^n) / (1 - A) * B
    return((pow(a, iterations, deck_size) * position + (1 - pow(a, iterations, deck_size))
           * pow(1 - a, deck_size-2, deck_size) * b) % deck_size)


if __name__ == "__main__":

    part1_correct = 1498
    part2_correct = 74662303452927

    shuffles = get_input("22")
    shuffles = [line.split(' ') for line in shuffles]

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
