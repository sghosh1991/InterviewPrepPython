"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.


"""
class Solution(object):

    def findKthLargest(self, nums, k):

        numElements = len(nums)
        return self.select(nums, 0, numElements - 1, numElements - k + 1)


    def select(self, nums, lo, hi, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        pivot = self.partition(nums, lo, hi)
        print "Pivot for subarray " + str(lo) + ":" + str(hi) + " " + str(pivot) + " elem " + str(nums[pivot])
        if pivot + 1 == k:
            print "Found " + str(pivot) + " : " + str(nums[pivot])
            return nums[pivot]
        elif pivot + 1 < k:
            print "Pivot is smaller. Searching for : " + str(k)
            return self.select(nums, pivot + 1, hi,  k)
        else:
            print "Pivot is larger. Searching for :" + str(k)
            return self.select(nums, lo, pivot - 1, k)

    def partition(self, arr, lo, hi):
        pivotIdx = lo
        pivotElement = arr[pivotIdx]
        firstIdx = lo # Index of the first element >= pivotIdx

        print "In partition pivot element " + str(pivotElement)
        print arr
        (arr[pivotIdx], arr[hi]) = (arr[hi], arr[pivotIdx])
        print arr

        while lo < hi:
            if arr[lo] < pivotElement:
                (arr[firstIdx], arr[lo]) = (arr[lo], arr[firstIdx])
                firstIdx += 1
            lo += 1
        print arr
        (arr[firstIdx], arr[hi]) = (arr[hi], arr[firstIdx])
        print arr
        return firstIdx

if __name__ == "__main__":
    x = Solution()
    #x.findKthLargest([8,3,7,6,7,7,7,1,5,9], 4)
    #x.findKthLargest([1,2,3,4,5,6,7,8], 8)
    x.findKthLargest([3,2,1,5,6,4], 2)