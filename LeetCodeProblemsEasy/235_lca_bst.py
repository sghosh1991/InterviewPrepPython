# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        print "Called LCA with " + str(root.val) + " p: " + str(p.val) + " q: " + str(q.val)
        if p.val >= q.val:
            return self.lowestCommonAncestor(root, q, p)

        if not root:
            return None

        if p.val <= root.val and q.val >= root.val:
            return root
        elif p.val >= root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)