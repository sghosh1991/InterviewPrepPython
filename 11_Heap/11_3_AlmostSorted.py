'''
Creation Date: Jun 27, 2016
@author : Santosh Ghosh

Problem Statement: Given a very long sequence of numbers such that the array is almost sorted. Each element in the array is atmost
k distance away from its correct position. Sort this array

Input: Almost sorted array and K.

Output: Print the elements in sorted order. Note only printing is needed. The array itself need not be modified.

Logic Applied: Since an element is almost k distance away from its original position, so we can say that if an element belongs at position i,
then in the array it can be at
'''
import heapq
heap = []

def sort_k_distance_away(arr,k):
    
    global heap
    for i in range(k+1):
        heapq.heappush(heap, arr[i])
    
    #k+1 elemets pushed. The samllest element must be one of this k+1 elemets as in the 
    #worst case the smallest element can be at k+1th position.
    # increase i to start processing the remaining elements
    i += 1
    while i<len(arr):
        print heapq.heappop(heap)
        heapq.heappush(heap, arr[i])
        i +=1
    
    #array elements exhausted. Now only pop
    while len(heap) != 0:
        print heapq.heappop(heap)
    
if __name__ == "__main__":
    
    arr = [3,-1,2,6,4,5,8]
    k = 2
    
    sort_k_distance_away(arr, k)
        
    