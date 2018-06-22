"""
https://leetcode.com/problems/lfu-cache/description/

Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?


"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.lookupTable = {}
        self.freqList = {}
        self.numNodes = 0


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.lookupTable:
            return -1
        else:
            (freq, node) = self.lookupTable[key]
            self.__move_node__(node, freq, freq + 1)
            return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = Node(value)
        self.lookupTable[key] = node
        # delete a node if capacity is filled
        if self.capacity == self.numNodes:
            node = self.__least_frequently_used_node()
        self.__insert_node__(node, 0)
        self.numNodes += 1

    def __least_frequently_used_node(self):
        

    def __move_node__(self, node, f1, f2):
        self.__delete_node__(node, f1)
        self.__insert_node__(node, f2)


    def __delete_node__(self, node, freq):
        (head, tail) = self.freqList[freq]
        if head == tail:
            # only one node in this freq list
            del self.freqList[freq]
        else:
            if not node.prev:
                # deleting head
                head = node.next
                node.next.prev = None
            elif not node.next:
                # deleting tail
                tail = node.prev
                node.prev.next = None
            self.freqList[freq] = (head, tail)
        return node




    def __insert_node__(self, node, freq):
        # Insert a node to the end of the LL, Update head and tail pointers
        if freq not in self.freqList:
            self.freqList[freq] = (None, None)
        (head, tail) = self.freqList[freq]
        if not head:
            head = tail = node
        else:
            tail.next = node
            node.prev = tail
            tail = node
        self.freqList[freq] = (head, tail)
