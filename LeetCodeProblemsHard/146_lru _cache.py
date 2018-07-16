"""

"""

class Node(object):

    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.val = val
        self.key = key


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.curr_cache_entries = 0
        self.head = self.tail = None
        self.capacity = capacity



    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.moveToEnd(self.cache[key])
            return self.cache[key].val
        return -1



    def evict(self):
        if self.head:
            del self.cache[self.head.key]
            self.curr_cache_entries -= 1
        return self.removeNode(self.head)


    def updateRecency(self, node):
        self.moveToEnd(node)

    def moveToEnd(self,node):
        self.insertNodeAtTail(self.removeNode(node))

    def removeNode(self, node):
        # if self.capacity == 1:
        #     self.head = self.tail = None
        # else:
        #     if self.head == node:
        #         self.head.next.prev = None
        #         next_head = self.head.next
        #         self.head.next = None
        #         self.head = next_head
        #     else:
        #         node.next.prev = node.prev
        #         node.prev.next = node.next
        #         node.next = node.prev = None

        next_node = node.next
        prev_node = node.prev

        if next_node:
            node.next.prev = node.prev
        if prev_node:
            node.prev.next = node.next
        if self.tail == node:
            self.tail = node.prev
        if self.head == node:
            self.head = node.next
        node.next = node.prev = None
        return node


    def insertNodeAtTail(self, node):
        if not self.tail:
            # First node to get inserted
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        return self.tail

    def printList(self):
        #print "Printing list Least recent to most recent"
        node = self.head
        res = []
        while node:
            res.append((node.key, node.val))
            node = node.next
        print res


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.updateRecency(node)
        else:
            if self.curr_cache_entries ==  self.capacity:
                self.evict()
                #print "Evicted " + str(self.evict().val)
            node = Node(key, value)
            self.cache[key] = node
            self.insertNodeAtTail(node)
            self.curr_cache_entries += 1
        print "Current cache entries " + str(self.curr_cache_entries)

if __name__ == "__main__":
    x = LRUCache(2)
    x.put(1,1)
    x.printList()
    x.put(1,2)
    x.printList()
    print "Getting: " + str(x.get(1))
    x.printList()
    x.put(3,3)
    x.printList()
    print "Getting: " + str(x.get(2))
    x.printList()
    x.put(4,4)
    x.printList()
    print "Getting: " + str(x.get(1))
    x.printList()
    print "Getting: " + str(x.get(3))
    x.printList()
    print "Getting: " + str(x.get(4))
    x.printList()

    # x.put(1,1)
    # x.printList()
    # x.put(1,2)
    # x.printList()
    # print "Getting: " + str(x.get(1))
    # x.printList()
    # x.put(3,3)
    # x.printList()
    # print "Getting: " + str(x.get(2))
    # x.printList()
    # x.put(4,4)
    # x.printList()
    # print "Getting: " + str(x.get(1))
    # x.printList()
    # print "Getting: " + str(x.get(3))
    # x.printList()
    # print "Getting: " + str(x.get(4))
    # x.printList()
