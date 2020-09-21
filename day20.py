from util import get_input, print_answer, get_orthogonal_neighbours
from heapq import heappop, heappush


def find_portals(maze):
    """
    Return details of portals in maze.

    Parameters:
    maze (str[]): list of strings representing the maze.

    Returns:
    portal_names (dict of (int, int): string): dictionary mapping coordinates (x, y) to portal names.
    portal_locations (dict of string: (int, int){}): dictionary mapping portal names to sets of coordinates (x, y).
    portal_sides (dict of (int, int): string): dictionary mapping coordinates (x, y) to "inner" or "outer" wall of maze.
    """

    portal_names = dict()
    portal_locations = dict()
    portal_sides = dict()

    height = len(maze)
    width = len(maze[0])

    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            # Upper case letters indicate portals
            if char.isupper():
                if y < height - 2 and maze[y+1][x].isupper() and maze[y+2][x] == '.':
                    # X <- char
                    # X
                    # .
                    name = char + maze[y+1][x]
                    location = (x, y+2)
                    if y < height / 2:
                        side = "outer"
                    else:
                        side = "inner"
                    store_portal(portal_names, portal_locations, portal_sides,
                                 name, location, side)
                if y < height - 1 and maze[y+1][x].isupper() and maze[y-1][x] == '.':
                    # .
                    # X <- char
                    # X
                    name = char + maze[y+1][x]
                    location = (x, y-1)
                    if y < height / 2:
                        side = "inner"
                    else:
                        side = "outer"
                    store_portal(portal_names, portal_locations, portal_sides,
                                 name, location, side)
                if x < width - 2 and maze[y][x+1].isupper() and maze[y][x+2] == '.':
                    # XX.
                    # ^
                    name = char + maze[y][x+1]
                    location = (x+2, y)
                    if x < width / 2:
                        side = "outer"
                    else:
                        side = "inner"
                    store_portal(portal_names, portal_locations, portal_sides,
                                 name, location, side)
                if x < width - 1 and maze[y][x+1].isupper() and maze[y][x-1] == '.':
                    # .XX
                    #  ^
                    name = char + maze[y][x+1]
                    location = (x-1, y)
                    if x < width / 2:
                        side = "inner"
                    else:
                        side = "outer"
                    store_portal(portal_names, portal_locations, portal_sides,
                                 name, location, side)
    return portal_names, portal_locations, portal_sides


def store_portal(portal_names, portal_locations, portal_sides, name, location, side):

    portal_names[location] = name
    portal_sides[location] = side
    if name in portal_locations:
        # Other portal with name already found - add to existing set
        portal_locations[name].add(location)
    else:
        # First portal with name found - make new entry in dict
        portal_locations[name] = {location}


def get_walkable(maze):
    """
    Return set of coordinates (x, y) for walkable positions in maze.

    Parameters:
    maze (str[]): list of strings representing the maze.
    """
    return {(x, y) for y, line in enumerate(maze) for x, char in enumerate(line) if line[x] == '.'}


def get_shortest_route(portal_names, portal_locations, walkable, portal_sides=dict()):
    """
    Return length of shortest route from AA to ZZ.

    Parameters:
    portal_names (dict of (int, int): string): dictionary mapping coordinates (x, y) to portal names.
    portal_locations (dict of string: (int, int){}): dictionary mapping portal names to sets of coordinates (x, y).
    walkable ((int, int){}): set of coordinates (x, y) of walkable positions
    portal_sides (dict of (int, int): string): dictionary mapping coordinates (x, y) to "inner" or "outer" wall of maze. (Optional, default=False).

    Returns:
    int: length of shortest route
    """

    # Start from maze entrace - AA
    q = [(0, 0, start_location) for start_location in portal_locations['AA']]
    seen = set()

    while q:
        q_distance, q_level, q_pos = heappop(q)

        # Maze is fixed so only need to consider a location/level pair once
        if (q_pos, q_level) in seen:
            continue
        seen.add((q_pos, q_level))

        # If landed on a portal
        if q_pos in portal_names:
            portal_name = portal_names[q_pos]
            if portal_name not in ['AA', 'ZZ']:

                # Get new level when moving through portal
                if not portal_sides:
                    # If not using portal sides (part1) level always 0
                    n_level = 0
                elif portal_sides[q_pos] == "outer":
                    # If portal is outer side than level decreases
                    n_level = q_level - 1
                    print("Recurse up through", portal_name, "to", n_level)
                elif portal_sides[q_pos] == "inner":
                    # If portal in inner side than level increases
                    n_level = q_level + 1
                    print("Recurse down through", portal_name, "to", n_level)
                else:
                    print("Unknown portal side", portal_sides[q_pos])
                    exit()

                # Level cannot be less than 0, outer portals act as walls in level 0
                if n_level >= 0:
                    # Find opposite portal and add to queue
                    for portal in (portal_locations[portal_name] - {q_pos}):
                        if (portal, n_level) not in seen:
                            heappush(q, (q_distance + 1, n_level, portal))

        # Add walkable neighbours to queue
        for position in get_orthogonal_neighbours(q_pos):
            if position in portal_locations['ZZ'] and q_level == 0:
                # queue is sorted by distance, first route to exit is shortest
                return q_distance + 1
            if position in walkable - seen:
                heappush(q, (q_distance + 1, q_level, position))


def part1(portal_names, portal_locations, walkable):

    return get_shortest_route(portal_names, portal_locations, walkable)


def part2(portal_names, portal_locations, walkable, portal_sides):

    return get_shortest_route(portal_names, portal_locations, walkable, portal_sides)


if __name__ == "__main__":

    part1_correct = 596
    part2_correct = 7610

    maze = get_input(20, strip=False)
    portal_names, portal_locations, portal_sides = find_portals(maze)
    walkable = get_walkable(maze)

    print_answer(1, part1(portal_names, portal_locations,
                          walkable), part1_correct)
    print_answer(2, part2(portal_names, portal_locations,
                          walkable, portal_sides), part2_correct)
