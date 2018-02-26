'''

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.


Idea:
At a given node, the maximum diameter seen till now is:
max ( left subtree max diameter, right sub tree max diamater, diameter including the current root)
diameter including the current root = 1 + maxPathStartingAtLeftChild + 1 + maxPathStartingAtRightChild
We also compute what the current node can offer interms of the number of edges if thi is selected to be in the diameter.
We pass up the maxdiameter till now and what the current node can offer if it is selected to be part of the diameter.

Why we need what the current node can offer?
Because in the node that called this node, to compute the diameter through that ode it needs to know the max path available in the
left chi;ld and right child then add 2 to it because it is contributing two edges.


'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def diameterOfBinaryTreeHelper(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # Base case
        if not root:
            return (0,0)

        # Base case 2
        elif not root.left and not root.right:
            #print " At " + str(root.val)
            return (0,0)

        else:
            (leftDiameter, leftMaxPath) = self.diameterOfBinaryTreeHelper(root.left)
            (rightDiameter, rightMaxPath) = self.diameterOfBinaryTreeHelper(root.right)

            diameterthroughRoot = 0
            if(root.left):
                diameterthroughRoot += 1 + leftMaxPath
            if(root.right):
                diameterthroughRoot += 1 + rightMaxPath
            maxDiameterTillNow = max(leftDiameter, rightDiameter, diameterthroughRoot)
            maxPathStartingAtRoot = 1 + max(leftMaxPath, rightMaxPath)

            #print " At " + str(root.val)
            #print " Max dia till now " + str(maxDiameterTillNow) + " max path startig at root " + str(maxPathStartingAtRoot)

            return (maxDiameterTillNow, maxPathStartingAtRoot)

    def diameterOfBinaryTree(self, root):
        return self.diameterOfBinaryTreeHelper(root)[0]

