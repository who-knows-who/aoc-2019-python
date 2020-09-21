import unittest
from util import get_input
from day20 import find_portals, get_walkable, part1, part2


class ClientTest(unittest.TestCase):

    def test_portals(self):
        maze = get_input(20, test=1, strip=False)
        expected_names = {(9, 2): 'AA', (9, 6): 'BC', (2, 8): 'BC',
                          (6, 10): 'DE', (2, 13): 'DE', (11, 12): 'FG', (2, 15): 'FG', (13, 16): 'ZZ'}
        expected_locations = {'AA': {(9, 2)}, 'BC': {(9, 6), (2, 8)},
                              'DE': {(6, 10), (2, 13)}, 'FG': {(11, 12), (2, 15)}, 'ZZ': {(13, 16)}}
        expected_sides = {(9, 2): 'outer', (9, 6): 'inner', (2, 8): 'outer',
                          (6, 10): 'inner', (2, 13): 'outer', (11, 12): 'inner', (2, 15): 'outer', (13, 16): 'outer'}
        portal_names, portal_locations, portal_sides = find_portals(maze)
        self.assertEqual(portal_names, expected_names)
        self.assertEqual(portal_locations, expected_locations)
        self.assertEqual(portal_sides, expected_sides)

    def test_walkable(self):
        maze = get_input(20, test=1, strip=False)
        expected_walkable = {(9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (10, 3), (11, 3), (12, 3),
                             (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (17, 4), (17, 5), (17, 6), 
                             (17, 7), (17, 8), (17, 9), (17, 10), (17, 11), (17, 12), (17, 13), (17, 14), 
                             (17, 15), (16, 15), (15, 15), (14, 15), (13, 15), (13, 16), (13, 14), (13, 13), 
                             (12, 13), (11, 13), (11, 12), (2, 15), (3, 15), (3, 14), (3, 13), (2, 13), 
                             (2, 8), (3, 8), (4, 8), (4, 9), (4, 10), (5, 10), (6, 10)}
        walkable = get_walkable(maze)
        self.assertEqual(walkable, expected_walkable)

    def test_part1(self):
        maze = get_input(20, test=1, strip=False)
        portal_names, portal_locations, _ = find_portals(maze)
        walkable = get_walkable(maze)
        self.assertEqual(part1(portal_names, portal_locations, walkable), 23)

    # def test_part2(self):
    #     maze = get_input(20, test=2, strip=False)
    #     portal_names, portal_locations, portal_sides = find_portals(maze)
    #     walkable = get_walkable(maze)
    #     self.assertEqual(part2(portal_names, portal_locations, walkable, portal_sides), 396)


if __name__ == '__main__':
    unittest.main()
