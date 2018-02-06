"""

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

    Input:
        Tree 1                     Tree 2
              1                         2
             / \                       / \
            3   2                     1   3
           /                           \   \
          5                             4   7
    Output:
    Merged tree:
             3
            / \
           4   5
          / \   \
         5   4   7


Solution: Symetrically move to merge the trees. Trick is the pass None in place of t1.left if t1 is None and so on for t1.right, t2.left, t2.right
         This solution is the one that is commented. Better approach. We donot need to traverse all the nodes once we see t1 == None and t2!= None and vice versa
         We can just return the non None node. If we need to maintain the original node structure we may need to copy. else we can just reuse the old ones.
         The initial solution gave me 17 pc the later 75 pc

         One interesting thing to note:
         If the block after else: was inside lese the performance dropped. If i put the block outside else i got better oerformance.
         Something to do with recursion stack. Compiler optimization.


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # Base case
        if not t1 and not t2:
            return None
        # Base case if one is None and the other is not
        elif not t1:
            return t2
            #processed_head = TreeNode(t2.val)
        elif not t2:
            return t1
            #processed_head = TreeNode(t1.val)
        else:
            processed_head = TreeNode(t1.val + t2.val)

        processed_head.left = self.mergeTrees(t1.left, t2.left)
        processed_head.right = self.mergeTrees(t1.right, t2.right)
        return processed_head

        # effective_t1_right = t1.right if t1 is not None else None
        # effective_t1_left = t1.left if t1 is not None else None
        # effective_t2_right = t2.right if t2 is not None else None
        # effective_t2_left = t2.left if t2 is not None else None
        #
        # processed_head.left = self.mergeTrees(effective_t1_left, effective_t2_left)
        # processed_head.right = self.mergeTrees(effective_t1_right, effective_t2_right)
        # return processed_head


