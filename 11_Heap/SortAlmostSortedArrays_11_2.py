'''
Creation Date: Jun 26, 2016
@author : Santosh Ghosh

Problem Statement: Merge increasing decreasing array.

Input: 

Output: 

Logic Applied:
'''


import heapq
from MergeNSortedSequences_11_1 import mergeNLists
heap = []

def sortIncreasingDecreasingArray(arr,k):
    
    global heap
    sortedLists = []
    i = 0
    
    while i < len(arr):
        
        sub_list_ascending = []
        sub_list_descending = []
        
        while i < len(arr)-1 and arr[i] <= arr[i+1]: #Note the check for i
            #increasing seq
            sub_list_ascending.append(arr[i])
            i += 1
        #Add the last element of the increasing seq
        sub_list_ascending.append(arr[i])
        #add to the list of sorted lists
        sortedLists.append(sub_list_ascending)
        
        #Decreasing Sequence
        
        #Place i at the beginning of the desc seq
        i += 1
        while i < len(arr)-1 and arr[i] >= arr[i+1]: #Note the check for i
            
            sub_list_descending.append(arr[i])
            i +=1
        
        sub_list_descending.append(arr[i])
        sub_list_descending.reverse()
        
        #add to the list of sorted lists
        sortedLists.append(sub_list_descending)
        
        #Place i at the beginning of the next seq
        i += 1
        print sortedLists
        mergeNLists(sortedLists)
    
    
    
    
    
    
if __name__ == "__main__":
    arr = [57,131,493,294,221,339,418,452,442,190]
    sortIncreasingDecreasingArray(arr,3)
    