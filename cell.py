from graphics import Point, Line


class Cell:
    def __init__(self, window, x1, x2, y1, y2):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = window

    def draw(self):
        top_left_point = Point(self.__x1, self.__y1)
        top_right_point = Point(self.__x2, self.__y1)
        bottom_right_point = Point(self.__x2, self.__y2)
        bottom_left_point = Point(self.__x1, self.__y2)

        if self.has_left_wall:
            left_line = Line(top_left_point, bottom_left_point)
            self.__win.draw_line(left_line, "black")

        if self.has_right_wall:
            right_line = Line(top_right_point, bottom_right_point)
            self.__win.draw_line(right_line, "black")

        if self.has_top_wall:
            top_line = Line(top_left_point, top_right_point)
            self.__win.draw_line(top_line, "black")

        if self.has_bottom_wall:
            bottom_line = Line(bottom_left_point, bottom_right_point)
            self.__win.draw_line(bottom_line, "black")

    def draw_move(self, to_cell, undo=False):
        if self.__win is None:
            return

        c1_x_mid = (self.__x1 + self.__x2) / 2
        c1_y_mid = (self.__y1 + self.__y2) / 2

        c2_x_mid = (to_cell.__x1 + to_cell.__x2) / 2
        c2_y_mid = (to_cell.__y1 + to_cell.__y2) / 2

        color = "red"
        if undo:
            color = "gray"

        # go left
        if self.__x1 > to_cell.__x1:
            line = Line(Point(self.__x1, c1_y_mid), Point(c1_x_mid, c1_y_mid))
            self.__win.draw_line(line, color)
            line = Line(Point(to_cell.__x2, c2_y_mid), Point(c2_x_mid, c2_y_mid))
            self.__win.draw_line(line, color)

        # go right
        elif self.__x1 < to_cell.__x1:
            line = Line(Point(self.__x2, c1_y_mid), Point(c1_x_mid, c1_y_mid))
            self.__win.draw_line(line, color)
            line = Line(Point(to_cell.__x1, c2_y_mid), Point(c2_x_mid, c2_y_mid))
            self.__win.draw_line(line, color)

        # go up
        elif self.__y1 > to_cell.__y1:
            line = Line(Point(c1_x_mid, self.__y1), Point(c1_x_mid, c1_y_mid))
            self.__win.draw_line(line, color)
            line = Line(Point(c2_x_mid, to_cell.__y2), Point(c2_x_mid, c2_y_mid))
            self.__win.draw_line(line, color)

        # go down
        elif self.__y1 < to_cell.__y1:
            line = Line(Point(c1_x_mid, self.__y2), Point(c1_x_mid, c1_y_mid))
            self.__win.draw_line(line, color)
            line = Line(Point(c2_x_mid, to_cell.__y1), Point(c2_x_mid, c2_y_mid))
            self.__win.draw_line(line, color)
