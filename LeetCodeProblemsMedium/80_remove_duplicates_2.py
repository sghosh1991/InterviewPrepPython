"""

**INCOMPLETE**

"""




class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print "*"*20 + "\n"
        if len(nums) == 0 :
            return 0
        idxLastInserted = 0
        for i in range(1,len(nums)):
            if nums[idxLastInserted] != nums[i]:
                if i-1 - idxLastInserted+1 >= 2:
                    nums[idxLastInserted+2] = nums[i]
                    idxLastInserted += 2
                else:
                    nums[idxLastInserted+1] = nums[i]
                    idxLastInserted += 1
            print nums
        if len(nums) - 1 - idxLastInserted + 1 >= 2:
            idxLastInserted += 1
        print idxLastInserted+1
        return idxLastInserted + 1

if __name__ == "__main__":
    x = Solution()
    x.removeDuplicates([])
    x.removeDuplicates([2])
    x.removeDuplicates([2,3,4,5])
    x.removeDuplicates([2,2,2,2])
    x.removeDuplicates([2,2,2,3,3,4,5,5,5])
    x.removeDuplicates([1,1,1,2,2,3])