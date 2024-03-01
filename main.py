from graphics import Window
from maze import Maze
import time


def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 12, 12, 40, 40, win)

    start = time.time_ns()
    maze.solve()
    end = time.time_ns()
    result_time = (end - start) / (10**9)
    print(f"It took {result_time} seconds to solve")

    win.wait_for_close()


main()
