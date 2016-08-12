'''
Creation Date: Jul 4, 2016
@author : Santosh Ghosh

Problem Statement: 

Input: S1,S2 <---- given component string. S3 <---- Test string. We need to test if S3 is an interleavibg
of S1 and S2

Output: 

Logic Applied: The logic is well explained in:
https://www.youtube.com/watch?v=ih2OZ9-M3OM&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=29
Wat does each element from T represent?
T[i][j] <---- is the s3[0,i+j-1] is an interleaving of s1[0,1] and s2[0,j]

'''

def create_aux_matrix(s1,s2,s3):
    
    T = []
    for i in range(len(s2)+1):
        T.append([-1]*(len(s1)+1))
    
    
    #fill up first row
    T[0][0] = True
    for i in range(1,len(T[0])):
        if s3[i-1] == s1[i-1]:
            T[0][i] = T[0][i-1]
        else:
            T[0][i] = False
    
    #fill up the 1st column
    for i in range(1,len(T)):
        if s3[i-1]==s2[i-1]:
            T[i][0] = T[i-1][0]
        else:
            T[i][0] = False
    
    #fill up the remaining of the columns
    for row in range(1,len(T)):
        for col in range(1,len(T[0])):
            char_in_str = s3[row+col-1]
        
            #the char_in_str has matched with s2 which is in the y axis or across all rows. So we are taking one char from S2 and
            #want to see if the remaining of S3 match with the with wat we have from s1 and s2 minus the one char matched.
            #How do we do that? We move up. Moving up one row implies we are consuming the char from s2
            if char_in_str == s2[row-1]:
                T[row][col] = T[row-1][col]
                
            #the char_in_str has matched with s1 which is along the x axis or across all columns. So we are taking one char from S1 and
            #want to see if the remaining of S3 match with the with wat we have from s2 and s1 minus the one char matched.
            #How do we do that? We move left. Moving left one col implies we are consuming the char from s1.
            elif char_in_str == s1[col-1]:
                T[row][col] = T[row][col-1]
            else:
                T[row][col] = False        
    
    
    return(T)
    
    
    
def printMatrix(T):
    for row in range(len(T)):
        print T[row]
    print "\n"
    
if __name__ =="__main__":
    
    s1 = "aab"
    s2 = "axy"
    s3 = "aaxaby"
    
    print "Is s3 an interleavibng of s1 and s2? " + str(create_aux_matrix(s1, s2, s3)[len(s2)][len(s1)])