from util import get_input, print_answer
from math import ceil


def extract_reaction(line):
    parts = line.replace(',', '').split()

    recipe = []
    while parts:
        if parts[0] == "=>":
            return int(parts[1]), recipe
        recipe.append((parts.pop(1), int(parts.pop(0))))


def extract_product(line):
    return line.split()[-1]


def new_needs(inventory, chemical_needed, quantity_needed):
    if inventory[chemical_needed] > 0:
        quantity_needed -= inventory[chemical_needed]
        inventory[chemical_needed] = 0
    (quantity_produced, reaction) = reactions[chemical_needed]
    reactions_needed = ceil(quantity_needed / quantity_produced)
    inventory[chemical_needed] = (reactions_needed * quantity_produced) - quantity_needed
    return [(reagent[0], reactions_needed * reagent[1]) for reagent in reaction]


def part1():
    inventory = {product: 0 for product in reactions.keys()}
    need = [("FUEL", 1)]
    ore_needed = 0

    while need:
        (chemical_needed, quantity_needed) = need.pop(0)
        if chemical_needed == "ORE":
            ore_needed += quantity_needed
        elif quantity_needed <= inventory[chemical_needed]:
            inventory[chemical_needed] -= quantity_needed
        else:
            need.extend(new_needs(inventory, chemical_needed, quantity_needed))
    return ore_needed


def part2():

    inventory = {product: 0 for product in reactions.keys()}
    inventory['ORE'] = 1000000000000
    fuel_produced = 0
    producing = 0
    need = []

    while True:
        if not need:
            fuel_produced += producing
            producing = max(int(inventory["ORE"] / part1_correct), 1)
            need.append(("FUEL", producing))
        while need:
            (chemical_needed, quantity_needed) = need.pop(0)
            if chemical_needed == "ORE" and quantity_needed >= inventory["ORE"]:
                return fuel_produced
            if quantity_needed <= inventory[chemical_needed]:
                inventory[chemical_needed] -= quantity_needed
            else:
                need.extend(new_needs(inventory, chemical_needed, quantity_needed))


if __name__ == "__main__":

    part1_correct = 1046184
    part2_correct = 1639374

    reactions = {extract_product(line): extract_reaction(line) for line in get_input("14")}

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
