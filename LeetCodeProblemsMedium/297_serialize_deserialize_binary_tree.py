"""

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def __init__(self):
        self.serialized_tree = []
        self.idx = 0

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            self.serialized_tree.append(None)
            return

        self.serialized_tree.append(root.val)
        self.serialize(root.left)
        self.serialize(root.right)



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        print self.serialized_tree
        self.idx = 0
        return self.deserializeHelper()

    def deserializeHelper(self):

        print "Inspecting idx " + str(self.idx)
        if len(self.serialized_tree) == self.idx or self.serialized_tree[self.idx] == None:
            self.idx += 1
            return None

        root = TreeNode(self.serialized_tree[self.idx])
        self.idx += 1
        root.left = self.deserializeHelper()
        root.right = self.deserializeHelper()

        return root


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))