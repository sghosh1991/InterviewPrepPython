'''
Creation Date: Jun 26, 2016
@author : Santosh Ghosh

Problem Statement: Merge N sorted list

Input: A list of lists each of which is sorted.

Output: A single list containing the union of all elements in sorted orders. 

Logic Applied: Use a min heap to combine the lists. Complexity: O(NlogK) where N = total elemets across all
lists, K = number of lists. It is efficient than O(NlogN) where you simply put all items in list and sort.
if K << N then this approach makes more sense. 
'''

import heapq
heap = []
#for each of the sublist contains the index of the element which have been processed.
processed_idx = [] 

def mergeNLists(sortedLists):
    
    global heap,processed_idx
    
    #initialize processed_idx list
    processed_idx = [0]*len(sortedLists)
    
    #put the first element off all lists in the heap
    for list_number,subList in enumerate(sortedLists):
        heapq.heappush(heap, (subList[0], list_number))
    

    while len(heap) != 0:
     
        #get the list from which the smallest element will be popped
        element_popped_from_list = heap[0][1]
         
        if(processed_idx[element_popped_from_list] != len(sortedLists[element_popped_from_list]) - 1):
             
            item_idx_to_push = processed_idx[element_popped_from_list]+1
            item_to_push = sortedLists[element_popped_from_list][item_idx_to_push]
            processed_idx[element_popped_from_list] += 1           
            print heapq.heappushpop(heap, (item_to_push,element_popped_from_list))[0]
        else:
            # A sub list has exhausted. So pop the next element
            print str(heapq.heappop(heap)[0])
    



if __name__ == "__main__":
    listOfLists = [[3,6,8,12],[4,6,7]]
    mergeNLists(listOfLists)
    
    #library function
    #print list(heapq.merge([3,6,8,12],[4,6,7]))
       
            
        
        

