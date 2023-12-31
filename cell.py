from graphics import Line, Point


class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        walls = [
            (self.has_left_wall, Point(x1, y1), Point(x1, y2)),
            (self.has_top_wall, Point(x1, y1), Point(x2, y1)),
            (self.has_right_wall, Point(x2, y1), Point(x2, y2)),
            (self.has_bottom_wall, Point(x1, y2), Point(x2, y2)),
        ]

        for has_wall, start, end in walls:
            color = None if has_wall else "white"
            line = Line(start, end)
            self._win.draw_line(line, color)

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return

        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2

        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2

        color = "red"
        if undo:
            color = "gray"

        # moving left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, y_mid), Point(x_mid, y_mid))
            self._win.draw_line(line, color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_cell._x2, to_y_mid))
            self._win.draw_line(line, color)

        # moving right
        elif self._x1 < to_cell._x1:
            line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
            self._win.draw_line(line, color)
            line = Line(Point(to_cell._x1, to_y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, color)

        # moving up
        elif self._y1 > to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
            self._win.draw_line(line, color)
            line = Line(Point(to_x_mid, to_cell._y2), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, color)

        # moving down
        elif self._y1 < to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
            self._win.draw_line(line, color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell._y1))
            self._win.draw_line(line, color)
