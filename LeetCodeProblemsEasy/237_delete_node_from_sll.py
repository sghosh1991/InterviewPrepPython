'''

'''

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        print " called with " + str(node.val)
        while node.next and node.next.next:
            print " Copy " + str(node.next.val) + " to " + str(node.val)
            node.val = node.next.val
            node = node.next

        node.val = node.next.val
        node.next = None

    def printLL(self):
        pass

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    x = Solution()
    x.deleteNode(a)
