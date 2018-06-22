"""

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"

https://leetcode.com/problems/largest-number/description/
"""
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        res = ""
        nums = sorted([str(num) for num in nums], reverse=True)
        print "Sorted nums " + str(nums)
        for i in range(len(nums)-1):
            print "Inspecting idx " + str(i) + " with number " + nums[i]
            if len(nums[i]) != len(nums[i+1]):
                print "Calling reorder nums with " + nums[i] + " and " + str(nums[i+1])
                res.append(self.reorderNums(nums[i], nums[i+1]))
            else:
                res.append(nums[i])

    def reorderNums(self, n1, n2):
        lenN1 = len(n1)
        lenN2 = len(n2)

        for i in range(min(lenN1, lenN2)):
            if n1[i] > n2[i]:
                return n1
            elif n1[i] < n2[i]:
                return n2
        if lenN1 < lenN2:
            if n1[i] > n2[i+1]:
                return n1
            else:
                return n2
        else:
            if n2[i] > n1[i+1]:
                return n2
            else:
                return n1

if __name__ == "__main__":
    x = Solution()
    x.largestNumber([10,2])



