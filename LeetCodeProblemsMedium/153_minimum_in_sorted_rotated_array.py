"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

EPI: Pg 298
Only the unsorted half can contain the minumum element

"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        numElements = len(nums)
        if numElements == 0:
            return -1

        while lo <= hi:
            mid = lo + (hi-lo)/2
            next = (mid + 1 ) % numElements
            prev = (mid + numElements - 1 ) % numElements
            if nums[mid] <= nums[next] and nums[prev] >= nums[mid]:
                return nums[mid]
            elif nums[mid] > nums[hi]:
                # Right half is unsorted
                lo = mid + 1
            else:
                # Left half is unsorted
                hi = mid - 1

if __name__ == "__main__":
    x = Solution()
    print x.findMin([])
    print x.findMin([1])
    print x.findMin([1,2,3,4])
    print x.findMin([4,3,2,1])
    print x.findMin([4,1,2,3])
