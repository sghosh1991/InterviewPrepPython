"""

"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        #print "*"*10 + "\n"
        #print nums
        numDigits = len(nums)
        if numDigits <= 1:
            return
        i = numDigits - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            #print "No next permutation"
            nums[:] = nums[-1::-1]
            return
        #print "Inflection point at " + str(i-1)
        # Find the element on the right that is just greater
        j = numDigits - 1
        while j >= i:
            if nums[j] > nums[i-1]:
                #print "Found rightmost digit just greater than digit at " + str(i-1)
                break
            j -= 1
        (nums[j], nums[i-1]) = (nums[i-1], nums[j])
        #print nums

        nums[i:] = nums[-1:i-1:-1]

        #print nums

if __name__ == "__main__":
    x = Solution()
    x.nextPermutation([6,2,1,5,4,3,0])
    x.nextPermutation([6,5,4,3,2])
    x.nextPermutation([1,2,3,4])
    x.nextPermutation([7,8])
    x.nextPermutation([8,5])


