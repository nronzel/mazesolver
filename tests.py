import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 5, 5)

        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[-1][-1].has_bottom_wall, False)

    def test_reset_cells_visited(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 5, 5)
        # set each cell visited to True
        for column in m1._cells:
            for cell in column:
                cell.visited = True
        # assert visited = True
        for column in m1._cells:
            for cell in column:
                self.assertEqual(cell.visited, True)

        # reset visited to False
        m1._reset_cells_visited()

        # assert visited is False for each cell
        for column in m1._cells:
            for cell in column:
                self.assertEqual(cell.visited, False)


if __name__ == "__main__":
    unittest.main()
