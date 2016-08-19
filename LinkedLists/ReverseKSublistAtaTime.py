"""
@created on: 8/18/16
@author: Santosh Ghosh
@problem statement:
@input:
@output:
"""

from LinkedListUtil import *

def reverse_k_sublist_at_a_time(ll,k):

    front = ll
    dummy_head = Node(-1)
    dummy_head.next_node = ll
    sublist_pred = dummy_head
    sublist_sucessor = None

    while front is not None:

        #get the head and tail of the sublist to reverse. Keep track of the successor of the tail and
        #predecessor of the head of such a sublist

        i= 1
        while i<k:
            front = front.next_node
            i += 1
        sublist_sucessor = front.next_node
        front.next_node = None
        rev_ll_head, rev_ll_tail = reverse_linked_list(sublist_pred.next_node)
        sublist_pred.next_node = rev_ll_head
        rev_ll_tail.next_node  = sublist_sucessor

        # print "After reversing one segment"
        # print_linked_list(dummy_head)

        #update the pointers for the next round
        front = sublist_sucessor
        sublist_pred = rev_ll_tail

    return dummy_head.next_node


def reverse_linked_list(ll):

    tail = ll
    head = None
    if ll is None or ll.next_node is None:
        return ll

    back = None
    curr = ll
    forward = curr.next_node

    while forward is not None:

        curr.next_node = back
        back = curr
        curr = forward
        forward = forward.next_node

    curr.next_node = back
    head = curr

    return (head,tail)

if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)

    a.next_node = b
    b.next_node = c
    c.next_node = d
    d.next_node = e
    e.next_node = f

    reverse_k_sublist_at_a_time(a,2)



