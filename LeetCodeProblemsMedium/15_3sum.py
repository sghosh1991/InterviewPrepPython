"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Unique:
To gurantee uniqueness, whenever u find a two sum keep moving lo upwards and hi downwards
till we find that the last added two sum's lo is  equal to the current lo and last added
twosum's hi is equal to curent hi

Same goes for the third number..Skip over duplicates

the idea is for each outer loop number we have found all possible combinations of two sums in the
twoSum(). So we need to skip over the duplicate numbers in outer loop

"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lenNums = len(nums)
        if lenNums < 3:
            return []
        nums = sorted(nums)
        res = []
        print nums
        i = 0
        while i < len(nums)-2:
            print "Inspecting element " + str(nums[i]) + " at index " + str(i)
            if len(res) and res[-1][0] == nums[i]:
                i += 1
                continue
            twoSums = self.twoSum(i+1, lenNums-1, nums, -nums[i])
            for twoSum in twoSums:
                res.append([nums[i], twoSum[0], twoSum[1]])
            i += 1
        return res

    def twoSum(self, lo, hi, nums, k):
        res = []
        print "Inspecting twosum from " + str(lo) + ":" + str(hi) +" target: " + str(k)
        while lo < hi:
            print "Current two sum iteration " + str(lo) + ":" + str(hi)
            sum = nums[lo] + nums[hi]
            if sum < k:
                print "Less"
                lo += 1
            elif sum > k:
                print "More"
                hi -= 1
            else:
                print "Found"
                res.append((nums[lo], nums[hi]))
                lo += 1
                hi -= 1
                while res[-1][0] == nums[lo] and res[-1][1] == nums[hi]:
                    lo += 1
                    hi -= 1
        return res

if __name__ == "__main__":
    x = Solution()
    #print x.threeSum([-1, 0, 1, 2, -1, -4])
    #print x.threeSum([-1,0,-1,-1,0,0,1])
    print x.threeSum([-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0])