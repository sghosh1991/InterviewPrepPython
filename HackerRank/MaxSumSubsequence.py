import sys

def maxSumSubsequence(arr):
    # Simply sum up all +ve numbers. If no positive numbers simply output the least -ve number
    max_sum = 0
    for i in range(len(arr)):
        
        if arr[i] > 0:
            max_sum += arr[i]
        
    if max_sum <= 0:
        max_sum = max(arr)
    return max_sum