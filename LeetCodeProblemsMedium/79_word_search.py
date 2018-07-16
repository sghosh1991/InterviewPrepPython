"""

invalidateCache is dicey.
In the example testcase below
I was getting a failure because of position 1,3
the cache entry was 1,3,4. We thought it was not possible to
get an answer begining at i,j at 1,3 with pos at 4. But it was wrong


"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.boardRows = len(board)
        if self.boardRows == 0:
            return False
        self.boardCols = len(board[0])
        self.board = board
        self.word = word
        self.visted = [ [0]*self.boardCols for i in range(self.boardRows) ]
        self.invalidateCache = set()
        for i in range(self.boardRows):
            for j in range(self.boardCols):
                if self.word[0] == self.board[i][j] and self.exitsHelper(i, j, 0, 0):
                    return True
        return False

    def getAdjacentCells(self, i, j, stack):
        res = []
        for (disp_x,disp_y) in [ (1,0), (-1,0), (0,1), (0,-1) ]:
            if i + disp_x >= 0 and i + disp_x < self.boardRows and \
               j + disp_y >= 0 and j + disp_y < self.boardCols:
                res.append((i + disp_x, j + disp_y))
        #print "\t"*stack + "Children of " + str(i) + "," + str(j) + " " + str(res)
        return res

    def exitsHelper(self, i, j, pos, stack):

        print "\t"*stack + "Called with " + str(i) + "," + str(j)
        if pos == len(self.word) - 1:
            print "\t"*stack + "Found a sequence"
            return True
        # if (i, j, pos) in self.invalidateCache:
        #     print "\t"*stack + "Already cached failure returning"
        #     return False
        self.visted[i][j] = 1
        for (adjacent_x, adjacent_y) in self.getAdjacentCells(i, j, stack):
            if not self.visted[adjacent_x][adjacent_y] and self.board[adjacent_x][adjacent_y] == self.word[pos+1] and \
                    self.exitsHelper(adjacent_x, adjacent_y, pos + 1, stack + 1):
                return True
        self.visted[i][j] = 0
        #self.invalidateCache.add((i, j, pos))
        print "\t"*stack + "Could not find a sequence begining at " + str(i) + "," + str(j)
        return False

    def printMatrix(self, T):
        print "*"*20
        for i in range(len(T)):
            print T[i]

if __name__ == "__main__":
    x = Solution()
    board =[
                ['A','B','C','E'],
                ['S','F','E','S'],
                ['A','D','E','E']
            ]
    # print x.exist(board, "ABCCED")
    # print x.exist(board, "SEE")
    # print x.exist(board, "ABCB")
    print x.exist(board, "ABCESEEEFS")

