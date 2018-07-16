# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

"""

Idea is to put the data on stack in reverse order.
Has next will always put integers on top and return True
If the stack top is not integer it will:
1) Remove that element
2) Push into stack in reverse order the elements of this new list
3) It will again loopback up and check to see if the top elem is a integer and so on..

Bottom line has next return true if there is an integer on top
or return false if there is nothing left.
In the mean time it explores the stack


"""


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]


    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()


    def hasNext(self):
        """
        :rtype: bool
        """
        while len(self.stack):
            if self.stack[-1].isInteger():
                return True
            else:
                nestedList = self.stack.pop()
                for elem in nestedList.getList()[::-1]:
                    self.stack.append(elem)
        return False





        # Your NestedIterator object will be instantiated and called as such:
        # i, v = NestedIterator(nestedList), []
        # while i.hasNext(): v.append(i.next())