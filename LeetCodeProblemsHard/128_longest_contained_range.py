"""

Idea: Start checking for range if the number is the leftmost one of the range

"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        unique_elements = set(nums)
        max_range_length = 0

        for num in nums:

            if num - 1 not in unique_elements:
                # Starting a sequence
                i = 1
                while num + i in unique_elements:
                    i += 1
                max_range_length = max_range_length if max_range_length > i else i
        return max_range_length

if __name__ == "__main__":
    x = Solution()
    print x.longestConsecutive([100, 4, 200, 1, 3, 2])
    print x.longestConsecutive([1])
    print x.longestConsecutive([])
    print x.longestConsecutive([1,1,1,1])

