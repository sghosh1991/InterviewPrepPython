Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def sortedArrayToBST(self, nums):
        return self.sortedArrayToBSTHelper(nums, 0, len(nums)-1)

    def sortedArrayToBSTHelper(self, nums, lo, hi):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if lo > hi:
            return None
        mid = lo + (hi - lo)/2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBSTHelper(nums, lo, mid - 1)
        root.right = self.sortedArrayToBSTHelper(nums, mid + 1, hi)
        return root