import numpy as np


class Sheet:

    def __init__(self, dimension_x=42, dimension_y=42, t_left=100, t_top=200, t_right=50, t_bottom=150):
        self.matrix = np.zeros((dimension_y, dimension_x))

        self.matrix[:, 0] = t_left
        self.matrix[0, :] = t_top
        self.matrix[:, -1] = t_right
        self.matrix[-1, :] = t_bottom

        self.matrix[0, 0] = 0
        self.matrix[0, -1] = 0
        self.matrix[-1, 0] = 0
        self.matrix[-1, -1] = 0

    def calc_heat(self):
        for i in range(len(self.matrix[1:-1])):
            y = i + 1
            for j in range(len(self.matrix[0][1:-1])):
                x = j + 1
                self.matrix[y][x] = (self.matrix[y - 1][x] + self.matrix[y + 1][x] +
                                     self.matrix[y][x - 1] + self.matrix[y][x + 1]) / 4

