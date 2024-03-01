import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(maze._cells),
            num_cols,
        )

        self.assertEqual(
            len(maze._cells[0]),
            num_rows,
        )

    def test_large_maze_create_cells(self):
        num_cols = 24
        num_rows = 20
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(maze._cells),
            num_cols,
        )

        self.assertEqual(
            len(maze._cells[0]),
            num_rows,
        )

    def test_entrance_and_exit_broken(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(
            maze._cells[0][0].has_top_wall,
            False
        )

        self.assertEqual(
            maze._cells[num_cols-1][num_rows-1].has_bottom_wall,
            False
        )

    def test_reset_visited(self):
        num_cols = 6
        num_rows = 5
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        for col in maze._cells:
            for cell in col:
                self.assertEqual(cell.visited, False)


if __name__ == "__main__":
    unittest.main()
