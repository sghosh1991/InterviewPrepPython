"""

"""
from collections import deque
class Solution(object):
    def __init__(self):
        self.EMPTY = 2147483647
        self.WALL = -1
        self.DOOR = 0
    def wallsAndGates(self, rooms):
        num_rows = len(rooms)
        if num_rows == 0:
            return rooms
        num_cols = len(rooms[0])
        q = deque()
        for row in range(num_rows):
            for col in range(num_cols):
                if rooms[row][col] == self.DOOR:
                    q.append((row, col))
        while len(q):
            r,c = q.popleft()
            for disp_r, disp_c in [ (0,1), (0,-1), (1,0), (-1,0) ]:
                pos_x = r + disp_r
                pos_y = c + disp_c
                if pos_x < 0 or pos_x >= num_rows or \
                                pos_y < 0 or pos_y >= num_cols or \
                                rooms[pos_x][pos_y] != self. EMPTY:

                    continue
                rooms[pos_x][pos_y] = 1 + rooms[r][c]
                q.append((pos_x, pos_y))
        self.printMatrix(rooms)

    # def wallsAndGates(self, rooms):
    #     """
    #     :type rooms: List[List[int]]
    #     :rtype: void Do not return anything, modify rooms in-place instead.
    #     """
    #     self.rooms = rooms
    #     self.num_rows = len(rooms)
    #     if self.num_rows == 0:
    #         return rooms
    #     self.num_cols = len(rooms[0])
    #     self.visited = [ [False]*self.num_cols for i in range(self.num_rows)]
    #     for row in range(self.num_rows):
    #         for col in range(self.num_cols):
    #             if self.rooms[row][col] != self.WALL and self.rooms[row][col] != self.DOOR:
    #                 self.wallsAndGatesHelper(row, col, 0)
    #     self.printMatrix(self.rooms, 0)
    #     rooms = self.rooms
    #
    #
    # def generateAdjacentCells(self, x, y, stack):
    #     res = []
    #     for (disp_x, disp_y) in [(0,-1), (0,1), (-1,0), (1, 0)]:
    #         if x + disp_x >= 0 and x + disp_x < self.num_rows and \
    #            y + disp_y >= 0 and y + disp_y < self.num_cols and \
    #            not self.visited[x+disp_x][y+disp_y]  and \
    #            self.rooms[x+disp_x][y+disp_y] != self.WALL:
    #             res.append((x+disp_x, y+disp_y))
    #     print "\t"*stack + "Children for: " + str(x) + "," + str(y) + " : " + str(res)
    #     return res
    #
    # def wallsAndGatesHelper(self, x, y, stack):
    #
    #     print "\t"*stack + "Called with " + str(x) + "," + str(y)
    #     if self.rooms[x][y] == self.DOOR:
    #         print "\t"*stack + "Hit base case" + str(x) + "," + str(y) + " Value " + str(self.rooms[x][y])
    #         return self.rooms[x][y]
    #
    #     self.visited[x][y] = True
    #     adjacent_cells = self.generateAdjacentCells(x, y, stack+1)
    #     closest_door_from_neighbors = self.ROOM
    #
    #     for cell_x,cell_y in adjacent_cells:
    #         #self.printMatrix(self.visited, stack + 1)
    #         if not self.visited[cell_x][cell_y]:
    #             closest_door_from_neighbors = min(closest_door_from_neighbors, self.wallsAndGatesHelper(cell_x, cell_y, stack+1))
    #
    #     if closest_door_from_neighbors != self.ROOM:
    #         self.rooms[x][y] = 1 + closest_door_from_neighbors
    #     self.visited[x][y] = False
    #     print "\t"*stack + "Done with " + str(x) + "," + str(y) + " value " + str(self.rooms[x][y])
    #     return self.rooms[x][y]
    #
    # def printMatrix(self, T, stack):
    #     print "\t"*stack +  "***************************"
    #     for row in T:
    #         print "\t"*stack + str(row)

    def printMatrix(self, T):
        for row in T:
            print str(row)





if __name__ == "__main__":
    # rooms = [
    #             [2147483647,-1,0,2147483647],
    #             [2147483647,2147483647,2147483647,-1],
    #             [2147483647,-1,2147483647,-1],
    #             [0,-1,2147483647,2147483647]
    #          ]
    #rooms = [[0,2147483647,2147483647,0,-1,-1,0,0,0,-1,-1,0,2147483647,2147483647],[2147483647,-1,2147483647,-1,2147483647,0,-1,2147483647,-1,2147483647,2147483647,-1,-1,2147483647],[0,0,-1,2147483647,-1,2147483647,-1,-1,2147483647,0,0,2147483647,0,2147483647],[-1,0,2147483647,-1,0,0,-1,2147483647,0,2147483647,0,-1,0,-1]]
    rooms = [
        [0, 2147483647, 2147483647],
        [-1, -1, 2147483647],
        [2147483647, 0, 2147483647],
        [-1, 0, -1]
    ]
    x = Solution()
    x.wallsAndGates(rooms)

