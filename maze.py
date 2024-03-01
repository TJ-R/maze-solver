from cell import Cell
import time
import random


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self.seed = seed

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited()

        if seed:
            random.seed(seed)

    def _create_cells(self):
        for i in range(self._num_cols):
            cell_col = []
            for j in range(self._num_rows):
                cell_col.append(Cell(self._win))
            self._cells.append(cell_col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return

        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)

        self._animate()

    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):

        last_col = self._num_cols - 1
        last_row = self._num_rows - 1

        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[last_col][last_row].has_bottom_wall = False
        self._draw_cell(last_col, last_row)

    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True

        while True:
            to_visit = []

            # Check all 4 directions
            # Check if left cell is visited
            if i > 0:
                if self._cells[i-1][j].visited is False:
                    to_visit.append((i-1, j, 'left'))

            # Check if right cell is visited
            if i < len(self._cells)-1:
                if self._cells[i+1][j].visited is False:
                    to_visit.append((i+1, j, 'right'))

            # Check if top cell is visite
            if j > 0:
                if self._cells[i][j-1].visited is False:
                    to_visit.append((i, j-1, 'top'))

            # Check if bottom cell is visited
            if j < len(self._cells[0])-1:
                if self._cells[i][j+1].visited is False:
                    to_visit.append((i, j+1, 'bottom'))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                break

            random_index = random.randrange(len(to_visit))

            direction = to_visit[random_index][2]

            if direction == 'left':
                current.has_left_wall = False
                self._draw_cell(i, j)

            elif direction == 'right':
                current.has_right_wall = False
                self._draw_cell(i, j)

            elif direction == 'top':
                current.has_top_wall = False
                self._draw_cell(i, j)

            else:
                current.has_bottom_wall = False
                self._draw_cell(i, j)

            self._break_walls_r(
                to_visit[random_index][0], to_visit[random_index][1])

    def _reset_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        end_i = len(self._cells) - 1
        end_j = len(self._cells[0]) - 1

        # Base Case
        if i == end_i and j == end_j:
            return True

        current = self._cells[i][j]
        current.visited = True
        to_visit = []

        if current.has_left_wall is False:
            to_visit.append((i-1, j))

        if current.has_right_wall is False:
            to_visit.append((i+1, j))

        if current.has_top_wall is False and (i+j != 0):
            to_visit.append((i, j-1))

        if current.has_bottom_wall is False:
            to_visit.append((i, j+1))

        for cell in to_visit:
            new_i = cell[0]
            new_j = cell[1]
            current.draw_move(self._cells[new_i][new_j])
            result = self._solve_r(new_i, new_j)

            if result:
                return True
            else:
                current.draw_move(self._cells[new_i][new_j], True)

        return False
