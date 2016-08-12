'''
Creation Date: Jun 28, 2016
@author : Santosh Ghosh

Problem Statement: 

Input: 

Output: 

Logic Applied: This problem is basially the NGE problem i.e the problem to find the next greater element. All the buildings
which have no NGE are not blocked by any building. So they can view the sunset. For each building from East to West
compute the NGE.
'''
from django.utils.translation import ngettext

def findBuildingsWithSunsetView(arr):
    
    nge = {}
    aux_stack = []
    
    aux_stack.append(arr[0])
    i = 1
    while i<len(arr):
        print aux_stack
        while len(aux_stack)!=0 and aux_stack[-1] < arr[i]:
            nge[aux_stack[-1]] = arr[i]
            aux_stack.pop(-1)
            print aux_stack
        aux_stack.append(arr[i])
        
        i +=1
        
    for elem in aux_stack:
        nge[elem] = -1
    print nge

if __name__ == "__main__":
    
    arr = [13,7,6,12]
    findBuildingsWithSunsetView(arr)
    
    arr = [13,12,11,10]
    findBuildingsWithSunsetView(arr)
     
    arr = [13,14,16,18]
    findBuildingsWithSunsetView(arr)
    
    
    