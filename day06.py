from util import get_input, print_answer
from collections import defaultdict


class Tree(object):
    def __init__(self, name, depth):
        self.children = []
        self.child_names = []
        self.name = name
        self.depth = depth
        self.leaf = False


def get_orbits(input):
    orbits = defaultdict(list)
    for line in input:
        inner, outer = line.split(")")
        orbits[inner].append(outer)
    return orbits


def get_tree(orbits, root, depth):
    new_tree = Tree(root, depth)
    if root in orbits.keys():
        for child in orbits[root]:
            new_tree.children.append(get_tree(orbits, child, depth + 1))
            new_tree.child_names.append(child)
    else:
        new_tree.leaf = True
    return new_tree


def count_orbits(tree):
    count = tree.depth
    if not tree.leaf:
        for child in tree.children:
            count += count_orbits(child)
    return count


def route_to_target(tree, target):
    if target in tree.child_names:
        return [target, tree.name]
    elif tree.leaf:
        return False
    else:
        for child in tree.children:
            route = route_to_target(child, target)
            if route:
                route.append(tree.name)
                return route
    return False


def part1():
    return count_orbits(orbit_tree)


def part2():
    to_san = route_to_target(orbit_tree, "SAN")
    to_you = route_to_target(orbit_tree, "YOU")

    for planet in to_san:
        if planet in to_you:
            return to_san.index(planet) + to_you.index(planet) - 2


if __name__ == "__main__":

    part1_correct = 278744
    part2_correct = 475

    orbit_dict = get_orbits(get_input("06"))
    orbit_tree = get_tree(orbit_dict, "COM", 0)

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
