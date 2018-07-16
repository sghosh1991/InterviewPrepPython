"""

"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        numElements = len(nums)
        if hi < 0:
            return -1
        while lo <= hi:
            mid = lo + (hi - lo)/2
            next = (mid + 1)%numElements
            prev = (mid + numElements - 1)%numElements
            if nums[mid] >= nums[prev] and nums[next] <= nums[mid]:
                return nums[mid]
            elif nums[mid] < nums[next]:
                lo = mid + 1
            else:
                hi = mid  - 1

if __name__ == "__main__":
    x = Solution()
    print x.findPeakElement([])
    print x.findPeakElement([1])
    print x.findPeakElement([1,1])
    print x.findPeakElement([8,6,5,3])
    print x.findPeakElement([8,9,10,11])
    print x.findPeakElement([8,6,15,1])
