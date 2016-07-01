# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
Creation Date: 2016-06-30

@author : Santosh Ghosh

Problem Statement:
Input:
Output:


Module Description:

'''
import sys

def calculateMinimumCandies(student_ranks):
    
    aux = [1]*len(student_ranks)
    #print student_ranks
    
    #pass 1 L->R
    for i in range(1,len(student_ranks)):
        if student_ranks[i] > student_ranks[i-1]:
            aux[i] = aux[i-1]+1
    #print aux
    #pass 2 R->L
    for i in range(len(student_ranks)-2,-1,-1):
        if student_ranks[i] > student_ranks[i+1]:
            aux[i] = max(aux[i+1]+1,aux[i])
    #print aux
    print sum(aux)
        


if __name__ == "__main__":
    ip_handle = sys.stdin
    student_ranks = []
    n = int(ip_handle.readline().strip())
    for i in range(n):
        student_ranks.append(int(ip_handle.readline().strip()))
    calculateMinimumCandies(student_ranks)