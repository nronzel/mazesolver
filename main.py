from graphics import Window
from maze import Maze


def main():
    # set size of maze
    num_rows = 16
    num_cols = 16

    # sets the offset of the maze from the sides of the Window, and
    # the size of each cell. Smaller number = smaller cells
    margin = 25

    screen_x = 800
    screen_y = 600

    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()

    win.wait_for_close()


main()
