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

    def close(self):
        self.window_running = False
        self.__root.quit()


def main():
    win = Window(800, 600)
    win.wait_for_close()

main()
