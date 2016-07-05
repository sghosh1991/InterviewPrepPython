'''
Creation Date: Jul 2, 2016
@author : Santosh Ghosh

Problem Statement: 

Input: 

Output: 

Logic Applied:
'''

'''
Check if the queen just placed at col_palcement[row] i.e at the (row)th row causes
problems with the other queens placed already
'''

def isValidplacement(col_placement,row_placed):
     
    for row in range(row_placed):
        
        #for each col till the one already placed check if
        #the other col_placements cause attacking position for this row
        
        diff = abs(col_placement[row] - col_placement[row_placed])
        
        #diff == 0 <--- there is a queen in the same col
        #diff == row_placed - row <--- there is already a queen in the same diagonal
        if diff==0 or diff == row_placed-row:
            return False
    
    return True

'''
@param row: 
@param col_placement:
@param all_palacements: 
@param N: the size of the board
@return: None 
'''
import copy

def NQueensHelper(row,col_placement,all_placements,tabs):
    
    #print " "*tabs + "Calling with row: " + str(row) + " Col placement till now: " + str(col_placement)
    #base case
    if row == len(col_placement):
        #print " "*tabs + "Base case hit"
        all_placements.append(copy.copy(col_placement))
    else:
        for col in range(len(col_placement)):
            col_placement[row] = col
            if isValidplacement(col_placement,row):
                NQueensHelper(row+1, col_placement, all_placements,tabs+1)
            
            #print " "*tabs + "The result so far : " + str(len(all_placements))
                

if __name__ == "__main__":
    
    all_placements = []
    col_placement = [-1]* 13
    NQueensHelper(0, col_placement, all_placements, 0)
    print (len(all_placements))
                