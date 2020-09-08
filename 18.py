from util import get_input, print_answer, get_orthogonal_neighbours
from intcode import Program, make_program, execute_program_io
from queue import SimpleQueue
from heapq import heappop, heappush


def get_details(start_pos):

    print("Mapping from", start_pos)
    # queue = [{"position": (int, int), "distance": int, "doors_seen": [string]}]

    q = SimpleQueue()
    seen = set()
    distances = dict()
    keys_needed = dict()

    q.put({"position": start_pos, "distance": 0, "keys_needed": set()})

    while not q.empty():
        item = q.get()
        q_pos = item["position"]
        if q_pos not in seen:
            q_d = item["distance"]
            q_keys = item["keys_needed"]
            seen.add(q_pos)
            if q_pos in keys.keys():
                distances[q_pos] = q_d
                keys_needed[q_pos] = q_keys
            if q_pos in doors.keys():
                q_keys.add(doors[q_pos].lower())
            for n_pos in get_orthogonal_neighbours(q_pos):
                if n_pos in walkable and n_pos not in seen:
                    q.put(
                        {"position": n_pos, "distance": q_d + 1, "keys_needed": q_keys.copy()})

    return {"distances": distances, "keys_needed": keys_needed}


def get_reachable_keys(position, keys_collected):
    return [key_position for key_position in maze_details[position]["distances"].keys() 
        if keys[key_position] not in keys_collected 
        and maze_details[position]["keys_needed"][key_position].issubset(keys_collected)]


def part1():
    q = [(0, initial_pos, frozenset())]
    seen = set()

    while q:
        d, pos, keys_collected = heappop(q)
        print(d, pos, keys_collected)
        if len(keys_collected) == len(keys.keys()):
            return(d)
        if not (pos, keys_collected) in seen:
            seen.add((pos, keys_collected))
            for key_position in get_reachable_keys(pos, keys_collected):
                heappush(q, (d + maze_details[pos]["distances"][key_position],
                             key_position, keys_collected.union([keys[key_position]])))


def part2():
    return 0


if __name__ == "__main__":

    part1_correct = 3962
    part2_correct = None

    counter = []

    maze = get_input("18")
    keys = {(x, y): maze[y][x] for y in range(len(maze))
            for x in range(len(maze[0])) if maze[y][x].islower()}
    doors = {(x, y): maze[y][x] for y in range(len(maze))
             for x in range(len(maze[0])) if maze[y][x].isupper()}
    walkable = [(x, y) for y in range(len(maze))
                for x in range(len(maze[0])) if maze[y][x] != '#']

    initial_pos = [(x, y) for y in range(len(maze))
                   for x in range(len(maze[0])) if maze[y][x] == '@'][0]

    # List of all points of interest in maze
    start_points = list(keys.keys())
    start_points.append(initial_pos)

    maze_details = {start_pos: get_details(
        start_pos) for start_pos in start_points}

    print_answer(1, part1(), part1_correct)
    print_answer(2, part2(), part2_correct)
