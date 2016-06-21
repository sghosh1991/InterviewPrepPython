def duplicateWithinKDistance(arr,k):

    unique_K_elements = set()
        
    start = 0
    end  = 0
    arr_size = len(arr)
    
    while(end < k):
        
        if arr[end] in unique_K_elements:
            return True
        else:
            unique_K_elements.add(arr[end])
        end +=1
    
        print unique_K_elements
    
    while(end < arr_size):
        
        unique_K_elements.remove(arr[start])
        
        if(arr[end] in unique_K_elements):
            return True
        else:
            unique_K_elements.add(arr[end])
        end +=1
        start +=1
    return False


if __name__ =="__main__":
    arr = [1,5,2,1,7,9,4,3]
    print duplicateWithinKDistance(arr,4)
        
        