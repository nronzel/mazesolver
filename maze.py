from cell import Cell
import time, random


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: float,
        cell_size_y: float,
        win=None,
        seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        """
        Populates the self._cells list with empty cells, then loops through
        each cell and calls _draw_cell() to calculate their locations and draw
        them on the canvas.
        """
        for i in range(self._num_cols):
            cols = []
            for j in range(self._num_rows):
                cols.append(Cell(self._win))
            self._cells.append(cols)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int):
        """
        Calculates the cells location given i and j (the index in self._cells)
        and then draws the cell, and animates each cell being drawn
        """
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        """
        The animate method is what allows us to visualize what the algorithms
        are doing in real time. It should simply call the window's redraw()
        method, then sleep for (0.05s) so your eyes can keep up with each
        render frame.
        """
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        """
        Removes the walls to enter and exit the maze from the respective cells.
        The start is always the top of the top left cell, and the exit is the
        bottom of the bottom right cell.
        """
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[-1][-1]

        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)
        exit_cell.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        """
        Recursive DFS through the cells, breaking walls as we go
        """
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            possible_directions = 0

            # find the cell to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
                possible_directions += 1
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
                possible_directions += 1
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
                possible_directions += 1
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
                possible_directions += 1

            # if nowhere to go, draw cell and return
            if possible_directions == 0:
                self._draw_cell(i, j)
                return

            # randomly choose direction to go
            direction_index = random.randrange(possible_directions)
            next_index = to_visit[direction_index]

            # knock out walls between this cell and next cell
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursive case - visit next cell
            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def solve(self):
        self._solve_r(0, 0)

    def _solve_r(self, i: int, j: int) -> bool:
        # return True if current cell is end cell OR if it leads to the end cell
        # else False

        # call the animate def
        self._animate()

        # mark current cell as visited
        self._cells[i][j].visited = True

        # if at the end cell, return True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            self._animate()
            return True

        # possible directions
        # up, right, down, left
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        for direction in directions:
            ni, nj = i + direction[0], j + direction[1]
            if 0 <= ni < self._num_cols and 0 <= nj < self._num_rows:
                if (
                    (direction == (0, -1) and not self._cells[i][j].has_top_wall)
                    or (direction == (1, 0) and not self._cells[i][j].has_right_wall)
                    or (direction == (0, 1) and not self._cells[i][j].has_bottom_wall)
                    or (direction == (-1, 0) and not self._cells[i][j].has_left_wall)
                ) and not self._cells[ni][nj].visited:
                    # draw a move between the current and next cell
                    self._cells[i][j].draw_move(self._cells[ni][nj])

                    # recursive case
                    if self._solve_r(ni, nj):
                        return True

                    # otherwise, "undo" the move
                    self._cells[i][j].draw_move(self._cells[ni][nj], undo=True)
        # no direction worked out - loser cell
        return False
