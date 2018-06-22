"""
https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/
"""
# class Solution(object):
#
#     def isValidSplit(self, nums, start, end):
#         return nums[end] - nums[start] + 1 >= 3
#
#     def isPossible(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         print "Start " + str(nums)
#         if len(nums) < 3:
#             return False
#
#         start = curr = 0
#         end = 1
#
#         while end < len(nums):
#
#             #print "Start :" + str(start) + " End :" + str(end) + " Curr :" + str(curr)
#
#             if nums[end] <= nums[curr] + 1:
#                 end += 1
#                 curr += 1
#             else:
#                 # The jump is more than 1 so the current list under consideration must end here
#                 #print "Jump greater than 1 ==> " + str(start) + " : " + str(end-1)
#                 if not self.isValidSplit(nums, start, end-1):
#                     return False
#                 start = curr = end
#                 end += 1
#         # The list ended see if we can make a valid split
#         if start != 0:
#             return self.isValidSplit(nums, start, end - 1)
#         else:
#             return (nums[end-1] - nums[start])/3 >= 2

import collections

class Solution(object):
    def isPossible(self, nums):
        count = collections.Counter(nums)
        tails = collections.Counter()
        for i,x in enumerate(nums):
            print "*"*10
            print " Curr element => " + str(i) + ":" + str(x)
            print " Counters " + str(count)
            print " tails  " + str(tails)
            if count[x] == 0:
                print " Zero count continuing"
                continue
            elif tails[x] > 0:
                print "Adding to previous chain"
                tails[x] -= 1
                tails[x+1] += 1
            elif count[x+1] > 0 and count[x+2] > 0:
                print " New chain"
                count[x+1] -= 1
                count[x+2] -= 1
                tails[x+3] += 1
            else:
                print " Returning false "
                return False
            count[x] -= 1
        print " Returning true "
        return True


if __name__ == "__main__":
    x = Solution()
    nums = [1,2,3,4,5]
    print x.isPossible(nums)
    # nums = [1,2,3,3,4]
    # print x.isPossible(nums)
    # nums = [1,2,3,4,7,8,9]
    # print x.isPossible(nums)
    # nums = [1,2,3,3,3,4,5,6,6,6]
    # print x.isPossible(nums)
    # nums = [1,2,4,5,6]
    # print x.isPossible(nums)
    # nums = [1,2,3,3,4,5]
    # print x.isPossible(nums)
    # nums = [1,2,2,2,3,7,8,9,9,9,10]
    # print x.isPossible(nums)





