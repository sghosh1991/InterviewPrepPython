'''
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.


Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
'''
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if(len(nums) == 1):
            return 0
        else:
            if(nums[0] > nums[1]):
                max = nums[0]
                max_idx = 0
                second_max = nums[1]
                pass
            elif(nums[1] > nums[0]):
                max = nums[1]
                max_idx = 1
                second_max = nums[0]
                pass
            else:
                max = second_max = nums[0]
                max_idx = 0

            i = 2
            nums_len = len(nums)

            while(i < nums_len):
                if(nums[i] > max):
                    second_max = max
                    max = nums[i]
                    max_idx = i
                elif(nums[i] > second_max):
                    second_max = nums[i]
                i += 1

            print " max " + str(max)
            print " smax " + str(second_max)

            if(max == second_max):
                return -1
            return max_idx if(max >= second_max*2) else -1

if __name__  == "__main__":
    x = Solution()
    print " dominant idx " + str(x.dominantIndex([2]))
    print " dominant idx " + str(x.dominantIndex([2,0]))
    print " dominant idx " + str(x.dominantIndex([3,0,0,2]))
    print " dominant idx " + str(x.dominantIndex([2,2,2]))
