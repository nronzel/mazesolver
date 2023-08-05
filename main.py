from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Mazesolver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(
            self.__root, {"bg": "white", "height": height, "width": width}
        )
        self.canvas.pack(fill=BOTH)
        self.window_running = False

    def redraw(self):
        # call the root widget's (self.root) `update_idletasks()` and `update()`
        # methods. Each time this is called it will redraw the window
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        # set running state to "True", call self.redraw() over and over
        # as long as state is True
        self.window_running = True
        self.__root.mainloop()
        while self.window_running is True:
            self.redraw()

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def close(self):
        self.window_running = False
        self.__root.quit()


class Point:
    # Takes x and y coordinate to create a point
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    # takes two Points and destructures their coordinates
    def __init__(self, point1: Point, point2: Point):
        self.__x1 = point1.x
        self.__y1 = point1.y
        self.__x2 = point2.x
        self.__y2 = point2.y

    # draws line using the provided coordinates and canvas
    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.__x1, self.__y1, self.__x2, self.__y2, fill=fill_color, width=2
        )
        canvas.pack()


class Cell:
    def __init__(self, top_left: Point, bottom_right: Point, window: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = top_left.x
        self.__y1 = top_left.y
        self.__x2 = bottom_right.x
        self.__y2 = bottom_right.y
        self.__win = window

    def draw(self):
        top_left = Point(self.__x1, self.__y1)
        top_right = Point(self.__x2, self.__y1)
        bottom_right = Point(self.__x2, self.__y2)
        bottom_left = Point(self.__x1, self.__y2)

        if self.has_left_wall:
            line = Line(top_left, bottom_left)
            self.__win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(top_left, top_right)
            self.__win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(top_right, bottom_right)
            self.__win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(bottom_left, bottom_right)
            self.__win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        # draw a line from the center of one cell to the center of the to_cell
        curr_center_point = Point(
            (self.__x1 + self.__x2 // 2), (self.__y1 + self.__y2 // 2)
        )

        to_center_point = Point(
            (to_cell.__x1 + to_cell.__x2) // 2, (to_cell.__y1 + to_cell.__y2) // 2
        )
        line = Line(curr_center_point, to_center_point)
        self.__win.draw_line(line, color)


def main():
    win = Window(800, 600)
    point1 = Point(0, 0)
    point2 = Point(200, 200)
    point3 = Point(200, 0)
    point4 = Point(400, 200)
    cell1 = Cell(point1, point2, win)
    cell2 = Cell(point3, point4, win)
    cell1.draw()
    cell2.draw()
    cell1.draw_move(cell2)

    win.wait_for_close()


main()
