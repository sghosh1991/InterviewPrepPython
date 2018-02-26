'''

My solution:
There may be a tree where we lost the second minimum because we are propagating the
min vale. So we need to scan the entoire tree
propagate the min and second min up at each stage. It would be
a post order traversal. We would do the
min second min compute on the way up.
at a given node i will get the min,second min from both my sutrees.
Secode the min,second min from the 4 values.
and propagate up


# Better Solution:
No need to scan the entire tree ?
By te definition of the three, if one of the child node's value is not equal to the root value
then that, child node is a potential second min. No other node below the child node can be a
second min since all nodes are larger or euqal to that node.
if the root is same as one of the child we need to scan that subtree as thte second min might be lost under that tree

[2,2,5,3,2,5,7] This tree
the second min got lost under the left subtree. we need to scan the left sub tree


'''



'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, root_val):
            if not node:
                return 2 ** 32
            if node.val != root.val:
                return node.val
            return min(dfs(node.left, root.val), dfs(node.right, root.val))
        val = dfs(root, root.val)
        return val if val != 2 ** 32 else -1

'''

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findSecondMinimumHelper(root)[1]

    def findSecondMinimumHelper(self, root):
        if not root:
            #print " Returning -1"
            return (-1, -1)
        else:
            #print "Called with " + str(root.val)
            #print "Calling left"
            (lmin,lmax) = self.findSecondMinimumHelper(root.left)
            #print "Calling right"
            (rmin, rmax) = self.findSecondMinimumHelper(root.right)

            if(lmin == -1):
                return (root.val, -1)
            temp = [ x for x in [lmin, lmax, rmin, rmax] if x != -1]
            temp_unique = set(temp)
            temp = list(temp_unique)
            if(len(temp) == 1):
                return (temp[0], -1)
            temp.sort()
            print " returning " + str(temp)
            return (temp[0], temp[1])