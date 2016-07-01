'''
Creation Date: 2016-06-30

@author : Santosh Ghosh

Problem Statement:

Input:

Output:

Logic Applied:

'''

import sys


visited = None

def max_connected_area(arr):
    
    global visited

    max_connected_area_size = 0
    
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col] == 1 and visited[row][col] == False:
                component_size = get_size_of_connected_area(arr,row,col)
                print "Component Size: " + str(component_size)
                max_connected_area_size = max_connected_area_size if max_connected_area_size > component_size else component_size
    
    print max_connected_area_size

def get_size_of_connected_area(arr,i,j):
    
    global visited
    print "Called with " + str(i) + " " + str(j)
   
    visited[i][j] = True
    
    connected_nodes = 1
    children = get_children(arr, i, j)
    for child in children:
        if visited[child[0]][child[1]] == False:
            connected_nodes += get_size_of_connected_area(arr,child[0],child[1])
            print "Connected nodes " + str(connected_nodes)
    return connected_nodes



def get_children(arr,i,j):
    
    children = []
    
    #up
    if isValid(arr,i-1,j) and arr[i-1][j] == 1:
        children.append((i-1,j))
    
    #down
    if isValid(arr,i+1,j) and arr[i+1][j] == 1:
        children.append((i+1,j))
    
    #left
    if isValid(arr,i,j-1) and arr[i][j-1] == 1:
        children.append((i,j-1))
    
    #right
    if isValid(arr,i,j+1) and arr[i][j+1] == 1:
        children.append((i,j+1))
    
    #top-left
    if isValid(arr,i-1,j-1) and arr[i-1][j-1] == 1:
        children.append((i-1,j-1))
    
    #top-right
    if isValid(arr,i-1,j+1) and arr[i-1][j+1] == 1:
        children.append((i-1,j+1))
    
    #bottom-left
    if isValid(arr,i+1,j-1) and arr[i+1][j-1] == 1:
        children.append((i+1,j-1))
    
    #bottom-right
    if isValid(arr,i+1,j+1) and arr[i+1][j+1] == 1:
        children.append((i+1,j+1))
    
    
    
    return children


def isValid(arr,i,j):
    
    max_row = len(arr) - 1
    max_col = len(arr[0]) - 1
    
    if (i> max_row or i<0) or (j>max_col or j<0):
        return False 
        
    return True

if __name__ == "__main__":
    
    #global visited
    ip_handle = open("/home/santosh/test123","r")#sys.stdin
    
    rows = int(ip_handle.readline().strip())
    cols = int(ip_handle.readline().strip())
    
    matrix = []
    
    for i in range(rows):
        
        arr = [ int(val) for val in ip_handle.readline().strip().split() ]
        matrix.append(arr)
    visited = []
    
    for i in range(rows):
        
        visited.append([False]*cols)
    
#     print matrix
#     print visited
    max_connected_area(matrix)
    
        
        