'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

'''
import heapq

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Find the two minimum elements
        (min1, min2) = self.findMinSecondMin(nums)

        # Find the three max elements
        (max1, max2, max3) = self.findTop3(nums)

        print " bottom two " + str(min1) + " : " + str(min2)
        print " top three " + str(max1) + " : " + str(max2) + " : " + str(max3)

        if(max3 < 0):
            return max3 * max2 * max1
        else:
            max_prod2 = min1 * min2 if min1 * min2 > max1 * max2 else max1 * max2
            return max3 * max_prod2


    def findMinSecondMin(self, nums):
        minimum = secondminimum = 0
        if nums[0] > nums[1]:
            minimum = nums[1]
            secondminimum = nums[0]
        else:
            minimum = nums[0]
            secondminimum = nums[1]
        for i in range(2, len(nums)):
            if nums[i] < minimum:
                secondminimum = minimum
                minimum = nums[i]
            elif nums[i] < secondminimum:
                secondminimum = nums[i]

        return minimum, secondminimum



    def findTop3(self, nums):
        d = []
        for num in nums:
            print str(d)
            if(len(d) < 3):
                heapq.heappush(d, num)
            elif(d[0] < num ):
                heapq.heapreplace(d, num)


        return ( heapq.heappop(d), heapq.heappop(d), heapq.heappop(d) )


if __name__ == "__main__":
    x = Solution()
    x.maximumProduct([-1, -4, -7, 3, 65, 12, 5, 7])
