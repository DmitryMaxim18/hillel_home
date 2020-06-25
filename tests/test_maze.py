from unittest import TestCase
import maze


class CellsTestCase(TestCase):

    @staticmethod
    def test_start_cell():
        maze.grid[1][0] = '/'
        assert maze.is_start(1, 0) is False

    @staticmethod
    def test_is_visited():
        maze.grid[1][0] = 'v'
        assert maze.is_visited(1, 0) is True

    @staticmethod
    def test_mark_visited():
        maze.mark_visited(1, 3)
        assert maze.grid[1][3] == 'v'



