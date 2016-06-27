'''
Creation Date: Jun 26, 2016
@author : Santosh Ghosh

Problem Statement: Implement a Stack using a heap

Input: 

Output: 

Logic Applied:
'''

import heapq
import itertools

class Stack():
    
    heap  = []
    counter = itertools.count(-1,-1) #we need a max heap. So we count like -1,-2,-3 as the priorities
    '''
    O(logN) push operation
    '''
    def push(self,elem):
        
        timestamp = next(self.counter)
        heapq.heappush(self.heap, (timestamp,elem))
    
    
    '''
    O(logN) pop operartion
    '''
        
    def pop(self):
        
        if len(self.heap) == 0:
            raise Exception('Stack Empty')
        else:
            return heapq.heappop(self.heap)


if __name__ == "__main__":
    
    arr = [ 3,6,7,9]
    s = Stack()
    
    for i in arr:
        s.push(i)
    
    for i in range(4):
        print s.pop()
        