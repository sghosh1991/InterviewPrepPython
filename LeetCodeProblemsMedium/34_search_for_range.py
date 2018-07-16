"""

"""
import bisect
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        leftmost = self.findLeftmostOccurance(nums, target)
        rightmost = self.findRightMostOccurance(nums, target)
        return [leftmost, rightmost]


    def findLeftmostOccurance(self, nums, target):
        i = bisect.bisect_left(nums, target)
        if i != len(nums) and nums[i] == target:
            return i
        return -1
    def findRightMostOccurance(self, nums, target):
        i = bisect.bisect_right(nums, target)
        if i != 0 and nums[i-1] == target:
            return i-1
        return -1
if __name__ == "__main__":
    x = Solution()
    print x.searchRange([5,7,7,8,8,10], 8)
    print x.searchRange([5,7,7,8,8,10], 6)
    print x.searchRange([5,7,7,8,8,10], 10)
    print x.searchRange([5,7,7,8,8,10], 5)