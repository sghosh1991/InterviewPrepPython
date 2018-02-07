'''

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]


'''
from collections import deque

class Solution(object):

    def __init__(self):
        #self.visited = set()
        self.max_row = 0
        self.max_col = 0
        #self.toBeProcessed = deque()
        self.grid = None
        self.perimeter = 0
        #self.num_adjacent_squares_by_pos_id = {}

    def get_neighbors(self, r, c):

        num_neighbors = 0
        for (displacement_x, displacement_y) in ((-1,0), (1,0), (0, -1), (0, 1)):
            pos_x = r + displacement_x
            pos_y = c + displacement_y
            if self.is_valid_pos(pos_x, pos_y) and  \
                    self.grid[pos_x][pos_y] == 1:
                num_neighbors += 1
        return num_neighbors

    def is_valid_pos(self, r, c):
        if r > self.max_row or \
                        r < 0 or \
                        c > self.max_col or \
                        c < 0:
            return False
        return True

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.max_col = len(grid[0]) - 1
        self.max_row = len(grid) - 1
        self.grid = grid
        self.islandPerimeterHelper()
        return self.perimeter

    def islandPerimeterHelper(self):
        for row in range(self.max_row + 1):
            for col in range(self.max_col + 1):
                if self.grid[row][col] == 1:
                    num_adjacent_squares = self.get_neighbors(row, col)
                    self.perimeter += 4
                    self.perimeter -= num_adjacent_squares


if __name__ == '__main__':
    x = Solution()
    grid = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]
    print x.islandPerimeter(grid)





