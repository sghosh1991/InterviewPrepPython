"""

https://www.youtube.com/watch?v=elQcrJrfObg

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = deque()
        res = []
        stack.append(root)
        while len(stack):
            node = stack.popleft()
            res.append(node.val)
            if node.right:
                stack.appendleft(node.right)
            if node.left:
                stack.appendleft(node.left)
        return res

