import unittest
from util import get_input
from day20 import find_portals, part1, part2


class ClientTest(unittest.TestCase):

    def test_portals(self):
        maze = get_input(20, test=1, strip=False)
        expected_names = {(9, 2): 'AA', (9, 6): 'BC', (2, 8): 'BC',
                          (6, 10): 'DE', (2, 13): 'DE', (11, 12): 'FG', (2, 15): 'FG', (13, 16): 'ZZ'}
        expected_locations = {'AA': (9, 2), 'BC': {(9, 6), (2, 8)},
                              'DE': {(6, 10), (2, 13)}, 'FG': {(11, 12), (2, 15)}, 'ZZ': (13, 16)}
        portal_names, portal_locations = find_portals(maze)
        self.assertEqual(portal_names, expected_names)
        self.assertEqual(portal_locations, expected_locations)

    def test_walkable(self):
        maze = get_input(20, test=1, strip=False)
        expected_walkable = {(9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (10, 3), (11, 3), (12, 3),
                             (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (17, 4), (17, 5), (17, 6), 
                             (17, 7), (17, 8), (17, 9), (17, 10), (17, 11), (17, 12), (17, 13), (17, 14), 
                             (17, 15), (16, 15), (15, 15), (14, 15), (13, 15), (13, 16), (13, 14), (13, 13), 
                             (12, 13), (11, 13), (11, 12), (2, 15), (3, 15), (3, 14), (3, 13), (2, 13), 
                             (2, 8), (3, 8), (4, 8), (4, 9), (4, 10), (5, 10), (6, 10)}
        walkable = {(x, y) for y, line in enumerate(maze)
                    for x, char in enumerate(line) if line[x] == '.'}
        self.assertEqual(walkable, expected_walkable)

    def test_example1(self):
        maze = get_input(20, test=1, strip=False)
        portal_names, portal_locations = find_portals(maze)
        walkable = {(x, y) for y, line in enumerate(maze)
                    for x, char in enumerate(line) if line[x] == '.'}
        self.assertEqual(part1(portal_names, portal_locations, walkable), 23)


if __name__ == '__main__':
    unittest.main()
