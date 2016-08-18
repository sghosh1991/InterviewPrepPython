
class Node():

    def __init__(self, val):
        self.val = val
        self.next_node = None
        self.random = None


def clone(ll):

    mapping = {}
    runner = ll

    while runner is not None:
        mapping[runner] = Node(runner.val)
        runner = runner.next_node

    runner = ll

    while runner.next_node is not None:

        mapping[runner].next_node = mapping[runner.next_node]
        if runner.random is not None:
            mapping[runner].random = mapping[runner.random]
        runner = runner.next_node

    return mapping[ll]

def print_linkedlist(ll):

    runner = ll
    print " sequential nodes"
    while runner is not None:
        print "Next node: " + str(runner.val)
        if runner.random is not None:
            print "random node: " + str(runner.random.val)
        runner = runner.next_node


if __name__== "__main__":

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

    a.random = d
    c.random = f
    b.random = d

    cloned_ll = clone(a)
    print_linkedlist(cloned_ll)