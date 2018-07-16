"""
https://leetcode.com/problems/search-a-2d-matrix/description/
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        num_rows = len(matrix)
        if num_rows == 0:
            return False
        num_cols = len(matrix[0])

        row = 0
        col = num_cols - 1

        while row < num_rows and col >= 0:
            #print "Inspecting row:" + str(row) + " col:" + str(col)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False

if __name__ == "__main__":
    x = Solution()
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    print x.searchMatrix(matrix, 13)


""""
**** A Binary Search Approach ****

Idea: Do a binary search on the Leftmost column to determine the row that
CAN potentially contain the element. Once found do a binary search on that row.

class Solution(object):
    def searchMatrix(self, matrix, target):
        l=0
        r=len(matrix)-1
        if len(matrix)==0 or len(matrix[0])==0: return False
        # Find the row that will contain the element
        while l<=r:
            m=l+(r-l)/2
            #print m,l,r
            #print target, matrix[m]
            if target<matrix[m][0]:
                r=m-1
            if  matrix[m][0]<=target<=matrix[m][-1]:
                break
            if matrix[m][-1]<target:
                l=m+1
        #print m,matrix[m]
        # Find the cell that will contain the element if a candidate row has been found
        if matrix[m][0]<=target<=matrix[m][-1]:
            l=0
            r=len(matrix[m])-1
            #print l,r
            while l<=r:
                k=l+(r-l)/2
                #print k
                if target<matrix[m][k]:
                    r=k-1
                if target==matrix[m][k]:
                    return True
                if matrix[m][k]<target:
                    l=k+1
        
        return False


"""