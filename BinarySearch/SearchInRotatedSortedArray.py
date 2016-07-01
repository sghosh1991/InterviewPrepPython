'''
Creation Date: 2016-06-24

@author : Santosh Ghosh

Problem Statement:

Input:

Output:

Logic Applied: 

The main idea in any binary serach problem is to be able to figure out how can we conclusively eliminate each half of the problem in one iteration.
First try to figure out which part of the array is sorted. This is achieved by checking the arr[lo] with arr[mid]. Next we try to see if the sorted half may contain the
element to be looked up (E). The reason we have to first figure out the sorted half is this: The check to see if one subarray contains the element i.e if
arr[lo] <= E <= arr[hi]  is only possible if this subarray is sorted. So we need to know which one is sorted. Once we figure that out apply the
containment test i.e whether the element MAY lie in the given range. If yes search in that range else search in the other half

'''

def find_min_sorted_array(arr,elem):
    
    lo = 0
    hi = len(arr)-1
    mid = 0
    
     
    
    while(lo <= hi):
        
        
        mid = lo + (hi-lo)/2

        if arr[mid] == elem:
            return mid
        
        if arr[lo] <= arr[mid]:
            #The left part is sorted. 
            if elem >= arr[lo] and elem < arr[mid]:
                hi = mid-1 #because we already checked if the elem == arr[mid]. So for next iteration the hi can be mid-1
            else:
                lo = mid + 1
        else:
            #the right part is sorted
            if elem <= arr[hi] and elem > arr[mid]:
                lo = mid +1
            else:
                hi = mid -1
    


if __name__ == "__main__":
    
    #arr = [3,4,5,6,7,2,1]
    arr = [1,2,3,4,5,6,7,8]
    elem = 2
    print find_min_sorted_array(arr, elem)

            
            
                
        
        
    
    
    