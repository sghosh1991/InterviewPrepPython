'''
Creation Date: Jun 27, 2016
@author : Santosh Ghosh

Problem Statement: 

Input: 

Output: 

Logic Applied: This solution is not memory constrained. If N is very large then selection sort will also not work
as the space requirement also N for selection algorithm. This algorithm is space efficient. 

Selection: Time=> O(N) Space=> O(N)
Heap : Time=> O(NlogK) Space=> O(K)

If N very very large then the select algorithm will not work as it will not fit in RAM. So we maintain a candidate set of size K. This set contains
all the elements which can be the closest star. We need this set to support efficient maximum element extraction and
efficient insertion. A max heap come to mind as both the operations are O(logK).
Why max heap not a min heap? => First we insert the first k starts. In max heap the star with the max distance from earth is at the top.
Now for each incoming element we compare it with the star with the max distance so far. If the incoming star's distance is larger than
the one with at the top of the heap, then it cannot be a candidate as all other k-1 starts are already closer to earth than the max one.
So we keep on procesing elements k+1 to N. If the ith element is smaller than the max then we pop the max so far and insert the current element.
Finally we have a set of K closest stars. 
'''

import heapq,random
from scipy.io.matlab.miobase import arr_dtype_number
heap = []

def K_closest_starts(arr,k):
    
    global heap
    
    for i in range(k):
        heapq.heappush(heap, -arr[i])
    
    i += 1
    while i<len(arr):
        if abs(heap[0]) > arr[i]:
            #arr[i] has a chance of being one of the K closest.
            #Loop invariant: the heap contains the k closest elements
            #absolutely true: if arr[i] < heap[0] then heap[0] is not among the k closest
            heapq.heapreplace(heap, -arr[i])
        i +=1
    
    closest_stars = (-i for i in heap)
    print list(closest_stars)


if __name__=="__main__":
    
    k = 5
    arr = random.sample(range(78, 453),50)
    #print sorted(arr)
    K_closest_starts(arr,k)
        
    
