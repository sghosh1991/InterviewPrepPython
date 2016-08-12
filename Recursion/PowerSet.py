'''
Creation Date: Jul 2, 2016
@author : Santosh Ghosh

Problem Statement: Generate the power set of a given set

Input: 
Output: 

Logic Applied:
'''
import copy
def power_set_recursion(arr,idx_to_process,tab):
    
    print " "*tab + "Calling for idx = " + str(idx_to_process)
    
    #base condition
    if idx_to_process == 1:
        return [[],[arr[0]],[arr[1]],[arr[0],arr[1]]]
    
    
    #recursive definition
    power_set_partial = power_set_recursion(arr, idx_to_process-1,tab+1)
    power_set_for_idx = copy.deepcopy(power_set_partial)
    #print " "*tab + "copy done ok? " + str(power_set_for_idx is power_set_partial)
    for subset in power_set_for_idx:
        subset.append(arr[idx_to_process])
    
    power_set_for_idx.extend(power_set_partial)
    
#     print " "*tab + "power_set_partial " + str(power_set_partial)
#     print " "*tab + "power set idx " + str(power_set_for_idx)
    return power_set_for_idx



'''
Second Method: Combinatorics
'''

def create_bitmap_to_subset_mapping(result,arr,bitmap):
    
    #modify the binary representation to be of length equal to length of the arr
    #000,010 ---> we want the numbers to be padded woth zero.
    bitmap = bitmap[2:]
    bitmap = bitmap.zfill(len(arr))
    
    subset = [arr[idx] for idx,i in enumerate(bitmap) if i=='1']
    result.append(subset)
    print " subset is :" + str(subset)
    return result


def power_set_combinatoris(arr):
    
    result = []
    arr_size = len(arr)
    subset_size = 2**arr_size
    
    for i in range(subset_size):
        create_bitmap_to_subset_mapping(result, arr, bin(i))
        print result
    



if __name__ == "__main__":
    arr = [1,2,3]
    #power_set_recursion(arr, len(arr)-1, 0)
    power_set_combinatoris(arr)
    