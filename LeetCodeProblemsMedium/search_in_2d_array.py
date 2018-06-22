"""

"""

class Solution(object):


    def searchInmatrix(self, matrix, s):
        self.matrix = matrix
        self.s = s
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.visited = [ [False]*self.cols for i in range(self.rows) ]

        #self.printMatrix(self.matrix)
        for i in range(self.rows):
            for j in range(self.cols):
                self.res = []
                res = self.searchInMatrixHelper(i, j, 0, 0)
                if res:
                    print "Found a path starting at (" + str(i) + "," + str(j) + ") --> " + str(self.res[::-1])

    def getAdjacentCells(self, x, y):
        children = []
        for (disp_x, disp_y) in [(1,0), (-1, 0), (0, 1), (0, -1)]:
            if self.isVlaidCell(x + disp_x, y + disp_y):
                children.append((x + disp_x, y + disp_y))
        return children

    def isVlaidCell(self, i, j):
        return i < self.rows and i >= 0 and j < self.cols and j >= 0


    def searchInMatrixHelper(self, i, j, k, stack):

        #print "\t"*stack + "Searching at " + str(i) + "," + str(j) + " for string at index " + str(k)
        #self.printMatrix(self.visited, stack)
        if k == len(self.s) - 1 and self.matrix[i][j] == int(self.s[k]):
            self.visited[i][j] = True
            self.res.append((i,j))
            #print "\t"*stack + "String found"
            return True
        elif self.visited[i][j] or self.matrix[i][j] != int(self.s[k]):
            #print "\t"*stack + "String not matching or already visited"
            return False
        # elif self.visited[i][j]:
        #     print "\t"*stack + "Already visited"
        #     return False
        # elif self.matrix[i][j] != int(self.s[k]):
        #     print "\t"*stack + "String not matching"
        #     return False
        else:
            self.visited[i][j] = True
            res = False
            #print "\t"*stack + str(self.getAdjacentCells(i, j))
            for (x , y) in self.getAdjacentCells(i, j):
                #print "\t"*stack + "Inspecting child " + str(x) + ":" + str(y)
                #self.printMatrix(self.visited, stack)
                if not self.visited[x][y]:
                    res = self.searchInMatrixHelper(x, y, k+1, stack + 1)
                    #print "\t"*stack + "Result : " + str(x) + "," + str(y) + " " + str(res)
                    if res:
                        self.res.append((i, j))
                        #print "\t"*stack + "Found string skipping rest calls"
                        return res
            #print "\t"*stack + "Returning " + str(res)
            return res

    def printMatrix(self, m, stack):
        for i in range(len(m)):
            print "\t"*stack + str(m[i])



if __name__ == "__main__":
    x = Solution()
    matrix = [ [1,2,3], [4,1,4], [3, 2, 5]]
    x.searchInmatrix(matrix, "1234")




