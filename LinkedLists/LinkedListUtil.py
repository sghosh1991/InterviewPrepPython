"""
@created on: 8/18/16
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