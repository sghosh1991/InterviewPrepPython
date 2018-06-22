# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        return self.lcaHelper(root, p, q)[1]

    def lcaHelper(self, root, p, q):

        if not root:
            #print "Called with None"
            return (0, None)
        else:
            #print str(root.val) + ": " + "Called with " + str(root.val)
            numNodesFound = 0
            if root.val == p.val or root.val == q.val:
                numNodesFound += 1
                #print str(root.val) + ": " + "Found at root numNodes: " + str(numNodesFound)


            (numNodesFound_left, left_lca) = self.lcaHelper(root.left, p, q)
            #print str(root.val) + ": " + "Left child result " + str(numNodesFound_left)
            if numNodesFound_left == 2:
                return (numNodesFound_left, left_lca)
            if numNodesFound_left + numNodesFound == 2:
                #print str(root.val) + ": " + "Both children found in left subtree "
                return (2, root)


            (numNodesFound_right, right_lca) = self.lcaHelper(root.right, p, q)
            #print str(root.val) + ": " + "Right child result " + str(numNodesFound_right)
            if numNodesFound_right == 2:
                return (numNodesFound_right, right_lca)
            if numNodesFound_right + numNodesFound == 2:
                #print str(root.val) + ": " + "Both children found in right subtree "
                return (2, root)

            numNodesFound = numNodesFound + numNodesFound_left + numNodesFound_right
            return (numNodesFound, root)



