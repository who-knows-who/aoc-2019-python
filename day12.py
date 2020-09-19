from util import get_input, print_answer, extract_ints, lcm
from functools import reduce
import copy


def calc_energy(moons, velocities):
    total_energy = 0
    for moon in range(len(moons)):
        potential = sum([abs(moons[moon][dim]) for dim in range(3)])
        kinetic = sum([abs(velocities[moon][dim]) for dim in range(3)])
        total_energy += potential * kinetic

    return total_energy


def apply_gravity_dimension(moons, velocities):
    for i in range(len(moons) - 1):
        for j in range(i + 1, len(moons)):
            if moons[i] > moons[j]:
                velocities[i] -= 1
                velocities[j] += 1
            elif moons[i] < moons[j]:
                velocities[i] += 1
                velocities[j] -= 1


def apply_velocity_dimension(moons, velocities):
    for i in range(len(moons)):
        moons[i] += velocities[i]


def apply_gravity(moons, velocities):
    for i in range(len(moons) - 1):
        for j in range(i + 1, len(moons)):
            for dim in range(3):
                if moons[i][dim] > moons[j][dim]:
                    velocities[i][dim] -= 1
                    velocities[j][dim] += 1
                elif moons[i][dim] < moons[j][dim]:
                    velocities[i][dim] += 1
                    velocities[j][dim] -= 1


def apply_velocity(moons, velocities):
    for i in range(len(moons)):
        for dim in range(3):
            moons[i][dim] += velocities[i][dim]


def get_period(moons, velocities, dim):
    moons = [moons[moon][dim] for moon in range(len(moons))]
    velocities = [velocities[moon][dim] for moon in range(len(moons))]
    moons_initial = moons.copy()
    velocities_initial = velocities.copy()
    steps = 0
    while True:
        apply_gravity_dimension(moons, velocities)
        apply_velocity_dimension(moons, velocities)
        steps += 1
        if moons == moons_initial and velocities == velocities_initial:
            return steps


def part1(moons, velocities):
    for _ in range(1000):
        apply_gravity(moons, velocities)
        apply_velocity(moons, velocities)

    total_energy = calc_energy(moons, velocities)
    return total_energy


def part2(moons, velocities):
    return reduce(lcm, [get_period(moons, velocities, dim) for dim in range(3)])


if __name__ == "__main__":

    part1_correct = 12082
    part2_correct = 295693702908636

    moons = [extract_ints(moon) for moon in get_input("12")]
    velocities = [[0 for _ in ["x", "y", "z"]] for moon in moons]

    print_answer(1, part1(copy.deepcopy(moons), copy.deepcopy(velocities)), part1_correct)
    print_answer(2, part2(copy.deepcopy(moons), copy.deepcopy(velocities)), part2_correct)
