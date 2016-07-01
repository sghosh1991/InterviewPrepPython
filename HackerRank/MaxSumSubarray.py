import sys

def maxSumSubarry(arr):
    
    currSum = 0
    maxSum = -sys.maxint -1
    start = 0
    end = 0
    i = 0
    
    while i < len(arr):
        
        currSum += arr[i]
        if currSum < 0:
            currSum = 0
            start = i + 1
            end = start
        
        else:
            
            if currSum > maxSum:
                
                end = i
                maxSum = currSum
        i +=1
        
    if maxSum < 0:
        #there is not a single +ve number. So return the min of the array.
        maxSum = max(arr)
    return maxSum




if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    maxSumSubarry(arr)
    