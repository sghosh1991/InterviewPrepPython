"""

"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_subarray_sum = max_ending_here = nums[0]
        max_subarray_start = max_subarray_end = start =  0
        print "*"*30 + "\n"
        for idx in range(1,len(nums)):
            num = nums[idx]
            print "Inspecting element at " + str(idx) + ":" + str(num)
            if num > max_ending_here + num:
                # Start a new subarray
                print "Starting a new subarray"
                start =  idx
                max_ending_here = num
            else:
                print "Extending"
                max_ending_here += num

            if max_subarray_sum < max_ending_here:
                print "Global max found updating indices and global max"
                max_subarray_sum = max_ending_here
                max_subarray_start = start
                max_subarray_end = idx
                print "Global max: " +  str(max_subarray_sum)
                print "Global max start idx: " +  str(max_subarray_start)
                print "Global max end idx: " +  str(max_subarray_end)

        print "="*20 + "\n"
        print "Final Global max: " +  str(max_subarray_sum)
        print "Final Global max start idx: " +  str(max_subarray_start)
        print "Final Global max end idx: " +  str(max_subarray_end)

if __name__ == "__main__":
    x = Solution()
    x.maxSubArray([1,3,6,2,9])
    x.maxSubArray([-5, -3, -5, -1])
    x.maxSubArray([-2, -5, -1, -9])
    x.maxSubArray([1,3,-2,2,4])
    x.maxSubArray([1,5,-8,12,20])




