from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height, title="Window"):
        self.__root = Tk()
        self.__root.title(title)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack()
        self.__running = False
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)
        
    def get_canvas(self):
        return self.__canvas
        
    def close(self):
        self.__running = False
        
        
class Point():
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        
class Line():
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
        
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.start_point.x,
            self.start_point.y,
            self.end_point.x,
            self.end_point.y,
            fill=fill_color,
            width=2
        )
        