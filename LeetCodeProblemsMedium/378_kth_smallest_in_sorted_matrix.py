"""

"""
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in range(len(matrix)):
            heapq.heappush(heap, (matrix[i][0], i, 0))

        for i in range(k-1):
            (n, row, col) = heapq.heappop(heap)
            print "Popped element " + str(n) + " from row:" + str(row) + " col:" + str(col)
            if col < len(matrix) - 1:
                heapq.heappush(heap, ( matrix[row][col+1], row, col+ 1))
            #print "Heap now " + str(heap)

        return heap[0][0]

if __name__ == "__main__":
    x = Solution()
    # matrix = [
    #     [ 1,  5,  9],
    #     [10, 11, 13],
    #     [12, 13, 15]
    # ]
    # print x.kthSmallest(matrix, 5)
    matrix = []
    print x.kthSmallest(matrix, 5)
"""

Idea: We try to guess the kth smallest element
We do a binary search to find elements to the smaller than 
or equal to the mid element in each row.
Sum them up and we know how many elements is smaller than the
mid. Mid here refers to matrix elements, not indices line in 1d array binary search.


class Solution(object):
    def kthSmallest(self, matrix, k): 
        l = matrix[0][0]
        r = matrix[-1][-1]
        
        while l < r:
            mid = l + ((r-l) >> 1)
            nums = sum([bisect.bisect_right(row, mid) for row in matrix])
            if nums < k:
                l = mid + 1
            else:
                r = mid
        return l


"""


