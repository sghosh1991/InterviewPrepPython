'''
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.
'''


class Solution(object):
    def __init__(self):
        self.visited = []
        self.maxRows = 0
        self.maxCols = 0
        self.numRecursiveCalls = 0


    def initVisited(self, grid):
        self.maxRows = len(grid)
        self.maxCols = len(grid[0])
        self.visited = [ [0 for i in range(self.maxCols)] for j in range(self.maxRows)]

    def connectedOnes(self, grid, x, y):
        print "Calling connected friends with " + str([x,y])
        val = grid[x][y]
        if not val or self.visited[x][y]:
            return
        self.visited[x][y] = 1
        self.visited[y][x] = 1
        for nbr in self.generateNeighbors(grid, x, y):
            nbrVal = grid[nbr[0]][nbr[1]]
            if nbrVal and not self.visited[nbr[0]][nbr[1]]:
                self.numRecursiveCalls += 1
                self.connectedOnes(grid, nbr[0], nbr[1])


    def isValidNbr(self, grid, x, y):
        return x < self.maxRows and x >= 0 and \
               y < self.maxCols and y >= 0

    def generateNeighbors(self, grid, x, y):
        children = []
        # for disp in [(0,-1), (0,1), (1,0), (-1,0)]:
        #     if self.isValidNbr(grid, x + disp[0], y + disp[1]):
        #         children.append((x + disp[0], y + disp[1]))

        xDirectFriends = []
        yDirectFriends = []
        for i in range(self.maxCols):
            if grid[x][i] and i!=y:
                xDirectFriends.append((x,i))
            if grid[y][i] and i!= x:
                yDirectFriends.append((y,i))
        children.extend(xDirectFriends)
        children.extend(yDirectFriends)
        print "Generated children " + str(children)
        return children


    def findCircleNum(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.initVisited(grid)
        numFriendCircles = 0
        # mark all grid[i][i] as visited as they are meaningless
        # for i in range(self.maxCols):
        #     self.visited[i][i] = 1
        for i in range(self.maxRows):
            for j in range(self.maxCols):
                print "Inspecting position " + str([i,j])
                if grid[i][j] and not self.visited[i][j]:
                    self.connectedOnes(grid, i, j)
                    numFriendCircles += 1
                self.printGrid(self.visited)
                print "Friend Circles " + str(numFriendCircles)
        print "Total recursive calls " + str(self.numRecursiveCalls)
        return numFriendCircles

    def printGrid(self, grid):
        for i in range(self.maxRows):
            print grid[i]
        print "*"*10

if __name__ == "__main__":
    x = Solution()
    #print x.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
    print x.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
