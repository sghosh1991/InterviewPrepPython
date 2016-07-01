'''
Creation Date: 2016-06-24

@author : Santosh Ghosh

Problem Statement:

Input:

Output:

Logic Applied:

'''


def find_missing_positive_entry(arr):
    
    lo = 0
    hi = len(arr)-1
    
    while((hi-lo+1) < (arr[hi]-arr[lo] + 1)):
        
        mid = lo + (hi - lo)/2
        print "called with :",lo,mid,hi
        if( arr[mid] + 1 == arr[mid + 1] - 1 ):
            return arr[mid]+1
        
        if ((hi-mid+1) < (arr[hi]-arr[mid]+1)):
            lo = mid
        else:
            hi = mid
        
        
if __name__ == "__main__":
    arr= [1,2,3,4,5,6,8]
    print find_missing_positive_entry(arr)