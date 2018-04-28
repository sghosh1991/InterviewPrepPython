'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
 the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
 it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.robHelper(nums, len(nums) - 1, 0)

    def robHelper(self, nums, pos, recLevel):
        # The maximum you can rob at a given position ( you are robbing houses left to right ) is:
        # max ( Dont include that position, Include that position )
        # max ( robHelper(i-1), nums[i] + robHelper(i-2) )
        print recLevel*"\t" + "Calling robhelper with pos = " + str(pos)

        if pos < 0:
            return 0
        elif pos == 0:
            return nums[0]
        else:
            includingPos = nums[pos] + self.robHelper(nums, pos-2, recLevel + 1)
            excludingPos = self.robHelper(nums, pos-1, recLevel + 1)
            ans =  max(includingPos, excludingPos)
            print recLevel*"\t" + "Includingpos=" + str(includingPos) + " ExcludingPos=" + str(excludingPos) + " Ans=" + str(ans)
            return ans

if __name__ == "__main__":
    x = Solution()
    print "Ans = " + str(x.rob([2]))

