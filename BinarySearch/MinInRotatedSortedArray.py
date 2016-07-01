'''
Creation Date: 2016-06-24

@author : Santosh Ghosh

Problem Statement:

Input:

Output:

Logic Applied:

'''

def find_min_rotated_sorted_array(arr):
    
    lo = 0
    hi = len(arr) - 1
    
    while ( arr[lo] > arr[hi]):
        
        mid = lo + (hi-lo)/2
        
        if arr[mid] > arr[hi]:
            
            lo = mid + 1
        else:
            hi = mid
    
    return arr[lo]

if __name__ == "__main__":
    arr = [4,5,6,7,3,2,1]
    print find_min_rotated_sorted_array(arr)
    
            