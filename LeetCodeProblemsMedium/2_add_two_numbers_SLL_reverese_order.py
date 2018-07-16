"""
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head_res = tail_res = ListNode(None)
        carry = 0
        while l1 and l2:
            sum = (carry + l1.val + l2.val) / 10
            carry = (carry + l1.val + l2.val) % 10
            tail_res.next = ListNode(sum)

        remaining_list = l1 if l1 else l2

        while remaining_list:
            sum = (carry + remaining_list.val) / 10
            carry = (carry + remaining_list.val) % 10
            tail_res.next = ListNode(sum)

        self.printLL(head_res)
        return head_res.next

    def printLL(self, head):
        while head:
            print head.val


if __name__ == "__main__":
    x = Solution()
    print x.addTwoNumbers()
