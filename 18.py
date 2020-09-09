from util import get_input, print_answer, get_orthogonal_neighbours
from intcode import Program, make_program, execute_program_io
from queue import SimpleQueue
from heapq import heappop, heappush


def get_details(start_pos, keys, doors, walkable):

    print("Mapping from", start_pos)

    q = SimpleQueue()
    seen = set()
    details = dict()

    q.put({"position": start_pos, "distance": 0, "keys_needed": set()})
    # queue = [{"position": (int, int), "distance": int, "keys_needed": {string}}]

    while not q.empty():
        item = q.get()
        q_pos = item["position"]
        if q_pos in seen:
            continue
        seen.add(q_pos)
        q_distance = item["distance"]
        q_keys = item["keys_needed"]
        if q_pos in keys.keys():
            details[q_pos] = {"distance": q_distance, "keys_needed": q_keys}
        if q_pos in doors.keys():
            q_keys.add(doors[q_pos].lower())
        for n_pos in get_orthogonal_neighbours(q_pos):
            if n_pos in walkable - seen:
                q.put(
                    {"position": n_pos, "distance": q_distance + 1, "keys_needed": q_keys.copy()})

    return details


def get_reachable_keys(positions, keys_collected, keys, vault_details):
    return [[key_position for key_position in vault_details[position].keys()
             if keys[key_position] not in keys_collected
             and vault_details[position][key_position]["keys_needed"].issubset(keys_collected)]
            for position in positions]


def get_shortest_route(keys, doors, walkable, initial_positions, vault_details):
    q = [(0, initial_positions, set())]
    seen = set()

    while q:
        d, pos, keys_collected = heappop(q)
        if len(keys_collected) == len(keys.keys()):
            return(d)
        if (frozenset(pos), frozenset(keys_collected)) not in seen:
            print(d, pos, keys_collected)
            seen.add((frozenset(pos), frozenset(keys_collected)))
            reachable_keys = get_reachable_keys(
                pos, keys_collected, keys, vault_details)
            for bot, key_positions in enumerate(reachable_keys):
                for key_position in key_positions:
                    n_pos = pos.copy()
                    n_pos[bot] = key_position
                    heappush(q, (d + vault_details[pos[bot]][n_pos[bot]]["distance"],
                                 n_pos, keys_collected.union([keys[key_position]])))


def part1():

    maze = get_input("18")
    keys = {(x, y): maze[y][x] for y, _ in enumerate(maze)
            for x, _ in enumerate(maze[0]) if maze[y][x].islower()}
    doors = {(x, y): maze[y][x] for y, _ in enumerate(maze)
             for x, _ in enumerate(maze[0]) if maze[y][x].isupper()}
    walkable = {(x, y) for y, _ in enumerate(maze)
                for x, _ in enumerate(maze[0]) if maze[y][x] != '#'}
    initial_positions = [(x, y) for y, _ in enumerate(maze)
                         for x, _ in enumerate(maze[0]) if maze[y][x] == '@']

    points_of_interest = list(keys.keys()) + initial_positions
    vault_details = {position: get_details(
        position, keys, doors, walkable) for position in points_of_interest}
    return get_shortest_route(keys, doors, walkable, initial_positions, vault_details)


def part2():

    maze = get_input("18.2")
    keys = {(x, y): maze[y][x] for y, _ in enumerate(maze)
            for x, _ in enumerate(maze[0]) if maze[y][x].islower()}
    doors = {(x, y): maze[y][x] for y, _ in enumerate(maze)
             for x, _ in enumerate(maze[0]) if maze[y][x].isupper()}
    walkable = {(x, y) for y, _ in enumerate(maze)
                for x, _ in enumerate(maze[0]) if maze[y][x] != '#'}
    initial_positions = [(x, y) for y, _ in enumerate(maze)
                         for x, _ in enumerate(maze[0]) if maze[y][x] == '@']

    points_of_interest = list(keys.keys()) + initial_positions
    vault_details = {position: get_details(
        position, keys, doors, walkable) for position in points_of_interest}
    return get_shortest_route(keys, doors, walkable, initial_positions, vault_details)


if __name__ == "__main__":

    part1_correct = 3962
    part2_correct = 1844 

    #print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
