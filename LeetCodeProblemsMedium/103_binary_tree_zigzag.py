from collections import deque
class Solution(object):

    def r2lChildGeneration(self, root):
        res = []
        if root.right:
            res.append(root.right)
        if root.left:
            res.append(root.left)
        return res

    def l2rChildGeneration(self, root):
        res = []
        if root.left:
            res.append(root.left)
        if root.right:
            res.append(root.right)
        return res

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack_l2r = deque()
        stack_r2l = deque()
        stack_l2r.append(root)
        res = []

        while len(stack_l2r) or len(stack_r2l):
            if len(stack_l2r):
                (stack_under_process, direction) = (stack_l2r, 'l2r')
                other_stack = stack_r2l
            else:
                (stack_under_process, direction) = (stack_r2l, 'r2l')
                other_stack = stack_l2r
            level_nodes = []
            while len(stack_under_process):
                node = stack_under_process.pop()
                level_nodes.append(node.val)
                children = []
                # l2r means i have been processing from l2r queue.
                if direction == 'l2r':
                    print "Generating r 2 l children"
                    children = self.l2rChildGeneration(node)
                else:
                    print "Generating l 2 r children"
                    children = self.r2lChildGeneration(node)
                other_stack.extend(children)
            res.append(level_nodes)
            print "final res " + str(res)
        return res