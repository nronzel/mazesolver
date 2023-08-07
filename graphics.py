from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("Mazesolver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(
            self.__root, {"bg": "white", "height": height, "width": width}
        )
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        # call the root widget's (self.root) `update_idletasks()` and `update()`
        # methods. Each time this is called it will redraw the window
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        # set running state to "True", call self.redraw() over and over
        # as long as state is True
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed..")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False


class Point:
    # Takes x and y coordinate to create a point
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    # takes two Points and destructures their coordinates
    def __init__(self, point1: Point, point2: Point):
        self.p1 = point1
        self.p2 = point2

    # draws line using the provided coordinates and canvas
    def draw(self, canvas: Canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)
