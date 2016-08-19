"""
@created on: 16-08-2016
@author: Santosh Ghosh
@problem statement:
@input:
@output:
"""

class Node():

    def __init__(self, val):
        self.val = val
        self.next_node = None

def print_linked_list(ll):

    while ll is not None:
        print str(ll.val) + " "
        ll = ll.next_node

def reverse_linked_list(ll):


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
    return curr


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

    rev_ll = reverse_linked_list(a)
    print_linked_list(rev_ll)