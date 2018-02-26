"""

"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.level_count = {}

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.averageOfLevelsHelper(root, 0)
        #print self.level_count

        avg_sum_by_level = []

        for (level, (count,sum)) in self.level_count.iteritems():
            avg_sum_by_level.insert(level, float(sum)/count)

        #print avg_sum_by_level
        return avg_sum_by_level


    def averageOfLevelsHelper(self, root, level):

        if not root:
            return True
        #print "Called with " + str(root.val)
        #print self.level_count

        if(level not in self.level_count):
            self.level_count[level] = (1, root.val)
        else:
            (count, sum) = self.level_count[level]
            self.level_count[level] = (count + 1, sum + root.val)

        return self.averageOfLevelsHelper(root.left, level + 1) and self.averageOfLevelsHelper(root.right, level + 1)


