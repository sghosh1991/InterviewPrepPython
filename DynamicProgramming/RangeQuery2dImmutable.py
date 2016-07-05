'''
Creation Date: Jul 4, 2016
@author : Santosh Ghosh

Problem Statement: Given a 2d matrix which is immutable we want to do repeated queries of the form: return the sum of elements
between R1C1 and R2C2.

Input: A matrix. And many queries of the form (R1C1,R2C2)

Output: Sum of the elements of the matrix between R1C1 and R2C2

Logic Applied: Look at the video @ https://www.youtube.com/watch?v=PwDqpOMwg6U&index=41&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

'''

def createAuxArray(matrix):
    
    T = []
    for i in range(len(matrix)+1):
        T.append([0]*(len(matrix[0])+1))
    
    #fill up row 0 and col 0 with zeros. Already done during initialization.
 
    #fillup row 1
    for i in range(1,len(T[0])):
        T[1][i] = T[1][i-1] + matrix[0][i-1]
    
    #fill up col 1
    for i in range(1,len(T)):
        T[i][1] = T[i-1][1] + matrix[i-1][0]
        
    #fill up other cells
    for row in range(2,len(T)):
        for col in range(2,len(T[0])):
            T[row][col] = T[row-1][col] + T[row][col-1] + matrix[row-1][col-1] - T[row-1][col-1] 
    #printMatrix(T)
    return T




def query(r1,c1,r2,c2,T):
    
#     print T[r2+1][c2+1] #sum till r2,c2
#     print T[r1][c2+1] #sum till r1-1,c2
#     print T[r2][c1] #sum till r2,c1-1
#     print T[r1][c1] #sum till r1-1.c1-1
    
    #print when you move row wise change rows only. Keep in mind that the sum till cell r2,c2 is in cell r2+1,c2+1.
    #So need to adjust the sum calculation.
    #move one col left => keep col same
    #sum in that col => keep col + 1 value
    #sum in that row => row+1
    #move one row up => row
    
    sum = T[r2+1][c2+1] - T[r1][c2+1] - T[r2+1][c1] + T[r1][c1]
    return sum


def printMatrix(T):
    
    for row in range(len(T)):
        print T[row]
    print "\n"

if __name__=="__main__":
    
    matrix = [
              [2,0,-3,4],
              [6,3,2,-1],
              [5,4,7,3],
              [2,-6,8,1]
              ]
    
    (r1,c1) = (1,1)
    (r2,c2) = (3,2)
    printMatrix(matrix)
    T = createAuxArray(matrix)
    print(query(r1, c1, r2, c2,T))