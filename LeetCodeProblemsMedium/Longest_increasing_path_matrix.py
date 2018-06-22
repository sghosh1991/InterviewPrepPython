"""

Recurrence:
LIS(i,j) = max of all adjacent cell LIS + 1
Cache for optimality
"""

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.lisCache = [ [-1]*self.cols for i in range(self.rows) ]

        self.printMatrix(self.matrix)
        #self.printMatrix(self.lisCache)

        lisLength = 0
        for i in range(self.rows):
            for j in range(self.cols):
                res = self.longestIncreasingPathHelper(i,j)
                if lisLength < res:
                    lisLength = res
        return lisLength




    def getAdjacentCells(self, x, y):
        children = []
        for (disp_x, disp_y) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if self.isValidCell(x+ disp_x, y + disp_y):
                children.append((x + disp_x, y + disp_y))
        return children

    def isValidCell(self, i, j):
        return i >= 0 and i < self.rows and j >= 0 and j < self.cols


    def longestIncreasingPathHelper(self, i, j):

        #print "Search computing LIS at " + str(i) + "," + str(j)
        if self.lisCache[i][j] > 0:
            #print "Cache hit for " + str(i) + "," + str(j)
            return self.lisCache[i][j]

        lisChildren = []
        lisEndingHere = 1
        for (x, y) in self.getAdjacentCells(i, j):
            #print "Inspecting child" + str(x) + "," + str(y)
            if self.matrix[x][y] < self.matrix[i][j]:
               lisChildren.append( self.longestIncreasingPathHelper(x, y))
        lisEndingHere += 0 if len(lisChildren) == 0 else max(lisChildren)
        self.lisCache[i][j] = lisEndingHere
        return lisEndingHere

    def printMatrix(self, m):
        for i in range(len(m)):
            print str(m[i])

if __name__ == "__main__":
     x = Solution()
     matrix = [
         [9,9,4],
         [6,6,8],
         [2,1,1]
     ]
     print x.longestIncreasingPath(matrix)
     matrix = [
         [3,4,5],
         [3,2,6],
         [2,2,1]
     ]
     print x.longestIncreasingPath(matrix)
