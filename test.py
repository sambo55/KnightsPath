import unittest

from functions import (check_input, parse_input, translate_output, move_knight,
                       get_branches, get_shortest_path)


class TestCheckInput(unittest.TestCase):
    def test_check_input_raises_error(self):
        self.assertRaises(ValueError, check_input, 'DE12')


class TestParseInput(unittest.TestCase):
    def test_parse_input_returns_tuple(self):
        self.assertIsInstance(parse_input('D2 D4'), tuple)


class TestTranslateOutput(unittest.TestCase):
    def test_translate_output_returns_string(self):
        self.assertIsInstance(translate_output((0, 0)), str)


class TestMoveKnight(unittest.TestCase):
    def test_move_knight_returns_tuple(self):
        self.assertIsInstance(move_knight((0, 0), 0), tuple)

    def test_move_knight_correct_output_move0(self):
        self.assertEqual(move_knight((2, 0), 0), (0, 1))

    def test_move_knight_correct_output_move4(self):
        self.assertEqual(move_knight((2, 0), 4), (4, 1))


class TestGetBranches(unittest.TestCase):
    def test_get_branch_returns_list(self):
        self.assertIsInstance(get_branches([[(0, 0)]], (2, 2)), list)

    def test_get_branch_simple_target_reached(self):
        self.assertEqual(get_branches([[(0,0)]], (1,2)), [(0,0),(1,2)])

    def test_get_branch_two_target_not_reached(self):
        self.assertEqual(get_branches([[(0,0)]], (2,4)),
                         [[(0,0),(2,1)],[(0,0),(1,2)]])

class TestGetShortestPath(unittest.TestCase):
    def test_shortest_path_returns_list(self):
        self.assertIsInstance(get_shortest_path((0,0),(1,2)), list)

    def test_shortest_path_returns_list_of_tuples(self):
        self.assertIsInstance(get_shortest_path((0,0),(1,2))[0], tuple)

    def test_shortest_path_simple_path(self):
        self.assertEqual(get_shortest_path((0, 0), (1, 2)), [(0,0),(1,2)])

    def test_shortest_path_two_step_path(self):
        self.assertEqual(get_shortest_path((0, 0), (2, 4)), [(0,0),(1,2),(2,4)])


