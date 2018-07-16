"""

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        level_nodes = []
        q = deque()
        q.append(root)

        curr_count = 0
        level_count = 1

        while len(q):
            processed_node = q.popleft()
            print "Processing node " + str(processed_node.val)
            level_nodes.append(processed_node.val)
            level_count -= 1
            if processed_node.left:
                print "Processing node left child present"
                q.append(processed_node.left)
                curr_count += 1
            if processed_node.right:
                print "Processing node right child present"
                q.append(processed_node.right)
                curr_count += 1
            if level_count == 0:
                print "Finished processing all nodes at a given level"
                res.append(level_nodes)
                level_count = curr_count
                curr_count = 0
                level_nodes = []
            print "Level nodes" + str(level_nodes)
            print "Result nodes" + str(res)

        print res
        return res

if __name__ == "__main__":
    x = Solution()
    x.levelOrder()

