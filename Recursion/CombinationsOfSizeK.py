'''
Creation Date: 2016-06-24

@author : Santosh Ghosh

Problem Statement: Given a list of numbers print all combinations of size k

Input: List of numbers and K

Output: List of all possible combinations of size k

Logic Applied:

'''


def combinationsOfSizeK(arr,start_idx,arr_len,remaining_subset_size,partial_result,partial_res_idx,tabs):
    
    #print " "*tabs + "Called with: start_idx" + str(start_idx) + " remainning_len=" + str(remaining_subset_size) + " partial result=" + str(partial_result) 
    
    if remaining_subset_size == 0:
        print " "*tabs + str(partial_result)        #partial_result = partial_result[0:-1]
        return
    
    
    for idx in range(start_idx,arr_len-remaining_subset_size+1):
        
        
        #print " "*tabs + "idx range: "  + str(start_idx) + " to " + str(arr_len-remaining_subset_size) + " idx now: " + str(idx) 
        
        
        partial_result[partial_res_idx] = arr[idx]
        combinationsOfSizeK(arr, idx+1, arr_len, remaining_subset_size-1, partial_result,partial_res_idx+1,tabs+1)
    
    
if __name__=="__main__":
    
    combinationsOfSizeK([1,2,3,4], 0, 4, 3, [0,0,0],0,0) 
    
    