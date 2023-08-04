from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Mazesolver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(
            self.__root, {"bg": "white", "height": height, "width": width}
        )
        self.canvas.pack()
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


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.__x1 = point1.x
        self.__y1 = point1.y
        self.__x2 = point2.x
        self.__y2 = point2.y

    def draw(self, canvas, fill_color: str):
        canvas.create_line(
            self.__x1, self.__y1, self.__x2, self.__y2, fill=fill_color, width=2
        )
        canvas.pack()


def main():
    win = Window(800, 600)
    point1 = Point(100,300)
    point2 = Point(400, 300)
    line = Line(point1, point2)
    win.draw_line(line, "blue")

    win.wait_for_close()


main()
