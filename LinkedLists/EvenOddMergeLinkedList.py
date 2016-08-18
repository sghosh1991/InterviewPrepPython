class Node():
    def __init__(self, val):
        self.val = val
        self.next_node = None


def print_linked_list(ll):
    runner = ll
    while runner is not None:
        print "Next node: " + str(runner.val)
        runner = runner.next_node


def append(ll_tail, node):
    # append node to ll_tail and return ll_tail and current position of the node

    ll_tail.next_node = node
    ll_tail = ll_tail.next_node
    node = node.next_node
    ll_tail.next_node = None
    #print_linked_list(ll_tail)

    return (ll_tail, node)


def even_odd_list_split(ll):
    even_ll_dummy_head = Node(-1)
    odd_ll_dummy_head = Node(-1)

    even_ll_tail = even_ll_dummy_head
    odd_ll_tail = odd_ll_dummy_head

    runner = ll

    while runner is not None:

        #print "\n processing " + str(runner.val)

        if runner.val % 2 == 0:
            even_ll_tail, runner = append(even_ll_tail, runner)
        else:
            odd_ll_tail, runner = append(odd_ll_tail, runner)

    print "Printing Odd Nodes"
    print_linked_list(odd_ll_dummy_head.next_node)
    print "Printing Even Nodes"
    print_linked_list(even_ll_dummy_head.next_node)


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

    even_odd_list_split(a)

