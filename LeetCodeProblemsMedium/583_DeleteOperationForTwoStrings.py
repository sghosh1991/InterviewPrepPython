"""

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

"""

class Solution(object):

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        matrix = [ [0 for i in range(len(word2)+1) ] for j in  range(len(word1) + 1) ]

        self.printMatrix(matrix)
        # Init the first row and col
        for i in range(1,len(matrix)):
            matrix[i][0] = matrix[i-1][0] + 1
        for j in range(1, len(matrix[0])):
            matrix[0][j] = matrix[0][j-1] + 1
        self.printMatrix(matrix)

        for chr1 in range(1,len(matrix)):
            for chr2 in range(1, len(matrix[0])):
                print "Inspecting " + word1[chr1-1] + " : " + word2[chr2-1]
                if(word1[chr1-1] == word2[chr2-1]):
                    matrix[chr1][chr2] = matrix[chr1-1][chr2-1]
                else:
                    matrix[chr1][chr2] = min(matrix[chr1-1][chr2], matrix[chr1][chr2-1]) + 1
                self.printMatrix(matrix)
        return matrix[len(matrix)-1][len(matrix[0])-1]

    def printMatrix(self,m):
        for i in range(len(m)):
            print m[i]
        print "\n"

if __name__ == "__main__":
    x = Solution()
    print "Min delete distance " +  str(x.minDistance("a","ba"))