from graphics import Window, Point, Line
from cell import Cell


def main():
    win = Window(800, 600)
#    point1 = Point(200, 150)
#    point2 = Point(200, 250)
#    point3 = Point(400, 250)
#    point4 = Point(400, 150)

#    line1 = Line(point1, point2)
#    line2 = Line(point2, point3)
#    line3 = Line(point3, point4)
#    line4 = Line(point4, point1)

#    win.draw_line(line1, "black")
#    win.draw_line(line2, "red")
#    win.draw_line(line3, "yellow")
#    win.draw_line(line4, "blue")

    cell1 = Cell(win, 100, 200, 100, 200)
    cell2 = Cell(win, 300, 400, 300, 400)
    cell3 = Cell(win, 300, 400, 500, 600)

    cell1.draw()
    cell2.draw()
    cell3.draw()

    cell1.draw_move(cell2, False)
    cell2.draw_move(cell3, True)
    win.wait_for_close()


main()
