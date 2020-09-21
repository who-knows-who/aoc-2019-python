from util import get_input, print_answer, get_orthogonal_neighbours
from heapq import heappop, heappush


def part1(portal_names, portal_locations, walkable):

    seen = set()

    # Start from maze entrace - AA
    q = [(0, portal_locations['AA'])]

    while q:
        q_distance, q_pos = heappop(q)

        # queue is sorted by distance, first route to exit is shortest
        if q_pos == portal_locations['ZZ']:
            return q_distance
        
        # Maze is fixed so only need to consider a location once
        if q_pos in seen:
            continue
        seen.add(q_pos)

        if q_pos in portal_names:
            portal_name = portal_names[q_pos]
            if portal_name not in ['AA', 'ZZ']:
                for portal in (portal_locations[portal_name] - {q_pos}):
                    if portal not in seen:
                        heappush(q, (q_distance + 1, portal))

        for position in get_orthogonal_neighbours(q_pos):
            if position in walkable - seen:
                heappush(q, (q_distance + 1, position))     

def part2():
    return 0


def find_portals(maze):
    portal_names = dict()
    portal_locations = dict()
    height = len(maze)
    width = len(maze[0])
    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if char.isupper():
                if y < height - 2 and maze[y+1][x].isupper() and maze[y+2][x] == '.':
                    name = char + maze[y+1][x]
                    location = (x, y+2)
                    store_portal(portal_names, portal_locations,
                                 name, location)
                if y < height - 1 and maze[y+1][x].isupper() and maze[y-1][x] == '.':
                    name = char + maze[y+1][x]
                    location = (x, y-1)
                    store_portal(portal_names, portal_locations,
                                 name, location)
                if x < width - 2 and maze[y][x+1].isupper() and maze[y][x+2] == '.':
                    name = char + maze[y][x+1]
                    location = (x+2, y)
                    store_portal(portal_names, portal_locations,
                                 name, location)
                if x < width - 1 and maze[y][x+1].isupper() and maze[y][x-1] == '.':
                    name = char + maze[y][x+1]
                    location = (x-1, y)
                    store_portal(portal_names, portal_locations,
                                 name, location)
    return portal_names, portal_locations


def store_portal(portal_names, portal_locations, name, location):
    portal_names[location] = name
    if name in ['AA', 'ZZ']:
        portal_locations[name] = location
    elif name in portal_locations:
        portal_locations[name].add(location)
    else:
        portal_locations[name] = {location}

def get_walkable(maze):
    return {(x, y) for y, line in enumerate(maze) for x, char in enumerate(line) if line[x] == '.'}


if __name__ == "__main__":

    part1_correct = 596
    part2_correct = None

    maze = get_input(20, strip=False)
    portal_names, portal_locations = find_portals(maze)
    walkable = get_walkable(maze)

    print_answer(1, part1(portal_names, portal_locations, walkable), part1_correct)
    print_answer(2, part2(), part2_correct)
