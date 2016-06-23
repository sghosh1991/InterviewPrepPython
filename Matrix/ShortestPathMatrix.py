'''
Creation Date: 2016-06-21

@author : Santosh Ghosh, Engineer, Quantil Inc.

Problem Statement:

Input:

Output:

Logic Applied:

'''
import sys

#Will contain the minimum distance from 0,0 to i,j 
minDistanceFrom = [] 

def isValidPosition(matrix,x,y):
    
    
    valid_row_index = len(matrix) - 1
    valid_col_index = len(matrix[0]) - 1
    
    if (x <= valid_row_index and x >=0) and (y <= valid_col_index and y >=0):     
        return True
    
    return False

def shortestPathUtil(matrix,x,y):
    
    global minDistanceFrom
    print minDistanceFrom
           
    if minDistanceFrom[x][y] != -1:
        return minDistanceFrom[x][y]
    
    
    from_up = sys.maxint
    from_diag = sys.maxint
    from_left = sys.maxint
    
    
    #print "from left"
    if isValidPosition(matrix,x, y-1):
         
        from_left = shortestPathUtil(matrix, x, y-1)
    #print "from up"
    if isValidPosition(matrix,x-1, y):
         
        from_up = shortestPathUtil(matrix, x-1, y)

    #print "from diagonally up"
    if isValidPosition(matrix,x-1, y-1):
        from_diag = shortestPathUtil(matrix, x-1, y-1)
    #print "from right"
    
    
    min_dis_neighbours = list()
    min_dis_neighbours.append(from_up)
    min_dis_neighbours.append(from_left)
    min_dis_neighbours.append(from_diag)
    
    minimumDistance = min(min_dis_neighbours) + matrix[x][y]
    minDistanceFrom[x][y] = minimumDistance
    
    return minimumDistance


def shortestPath(matrix):
    
    global minDistanceFrom
    
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    for i in range(num_rows):
        cols = list()
        for j in range(num_cols):
            cols.append(-1)
        minDistanceFrom.append(cols)
    
    # This adds a base case where the distance from 0,0 to 0,0 is the distance 
    minDistanceFrom[0][0] = matrix[0][0]
    #print minDistanceFrom[2][2]
    return shortestPathUtil(matrix,2,2)
    
    
    
    
if __name__== "__main__":
    matrix = [ [1,2,3], [4,5,6], [7,8,9]]
    print shortestPath(matrix)
            
    