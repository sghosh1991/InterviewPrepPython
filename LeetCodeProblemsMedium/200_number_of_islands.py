'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
'''

class Solution(object):
    def __init__(self):
        self.visited = []
        self.maxRows = 0
        self.maxCols = 0


    def initVisited(self, grid):
        self.maxRows = len(grid)
        self.maxCols = len(grid[0])
        self.visited = [ [0 for i in range(self.maxCols)] for j in range(self.maxRows)]

    def connectedZeros(self, grid, x, y):
        val = grid[x][y]
        if val != 'O' or self.visited[x][y]:
            return grid
        self.visited[x][y] = 1
        for nbr in self.generateNeighbors(grid, x, y):
            nbrVal = grid[nbr[0]][nbr[1]]
            if not self.visited[nbr[0]][nbr[1]] and val == nbrVal:
                grid = self.connectedZeros(grid, nbr[0], nbr[1])
        grid[x][y] = 'Y'
        return grid


    def isValidNbr(self, grid, x, y):
        return x < self.maxRows and x >= 0 and \
               y < self.maxCols and y >= 0

    def generateNeighbors(self, grid, x, y):
        children = []
        for disp in [(0,-1), (0,1), (1,0), (-1,0)]:
            if self.isValidNbr(grid, x + disp[0], y + disp[1]):
                children.append((x + disp[0], y + disp[1]))
        return children


    def solve(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.initVisited(grid)
        print self.visited

        # Get all connected O s from the boundary.
        # Any O that is in boundary of the grid and all its associated O neighbors
        # cannot be captured.
        # We do a dfs traversal starting from each boundary 'O' and mark all its connected 'O's
        # as 'Y'. Any 'O' left is totally surrounded by 'X' and can be captured

        for i in range(self.maxRows):
            print "Checking " + str(i) + ":0"
            grid  = self.connectedZeros(grid, i, 0)
            self.printGrid(grid)
            print "Checking " + str(i) + ":" + str(self.maxCols-1)
            grid = self.connectedZeros(grid, i, self.maxCols-1)
            self.printGrid(grid)

        for j in range(self.maxCols):
            print "Checking " + "0:" + str(j)
            grid  = self.connectedZeros(grid, 0, j)
            self.printGrid(grid)
            print "Checking " + str(self.maxRows-1) + ":" + str(j)
            grid  = self.connectedZeros(grid, self.maxRows-1, j)
            self.printGrid(grid)


        for i in range(self.maxRows):
            for j in range(self.maxCols):
                if grid[i][j] == 'O':
                    grid[i][j] = 'X'
                elif(grid[i][j]) == 'Y':
                    grid[i][j] = 'O'
        self.printGrid(grid)

    def printGrid(self, grid):
        for i in range(self.maxRows):
            print grid[i]
        print "*"*10

if __name__ == "__main__":
    x = Solution()
    grid = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    x.solve(grid)