from util import get_input, print_answer, gcd
from math import degrees, atan2, sqrt, inf
from collections import defaultdict


def get_directions(asteroid):
    directions = defaultdict(lambda: {"location": None, "distance": inf})
    for a in asteroids:
        if a != asteroid:
            # y = 0 at top so invert y change
            direction = (a[0] - asteroid[0], -(a[1] - asteroid[1]))
            distance = sqrt((a[0] - asteroid[0])**2 + (a[1] - asteroid[1])**2)
            distance_gcd = gcd(direction[0], direction[1])
            direction = (direction[0] // distance_gcd, direction[1] // distance_gcd)
            if directions[direction]["distance"] > distance:
                directions[direction] = {"location": a, "distance": distance}
    return directions


def get_angle(direction):
    x, y = direction
    return (90 - degrees(atan2(y, x))) % 360


def part1():
    return max([len(get_directions(asteroid)) for asteroid in asteroids])


def part2():

    directions = [len(get_directions(asteroid)) for asteroid in asteroids]
    station = asteroids[directions.index(max(directions))]

    vectors = get_directions(station)
    angles = [(get_angle(x), vectors[x]["location"]) for x in vectors.keys()]
    angles.sort()

    target = 200
    return angles[target-1][1][0] * 100 + angles[target-1][1][1]


if __name__ == "__main__":

    part1_correct = 214
    part2_correct = 502

    space = get_input("10")

    asteroids = [(x, y) for y in range(len(space)) for x in range(len(space[0])) if space[y][x] == "#"]

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
