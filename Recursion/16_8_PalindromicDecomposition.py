'''
Creation Date: Jul 2, 2016
@author : Santosh Ghosh

Problem Statement: 

Input: 

Output: 

Logic Applied:
'''
import copy
def isPalindrome(s,tab):
    
    #check for palindromicity of s
    if len(s)==1:
        return True
    i=0
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            #print " "*tab + s + " is a NOT palindrome"
            return False
        i+=1
        j-=1
    #print " "*tab + s + " is a palindrome"
    return True

def palindromicPartitions(s,final_result,partial_result,num_partial_res,tab):
    
    #print " "*tab + "Calling with " + s + " result : " + str(final_result)
    
    #base case
    if s=="":
        #print " "*tab + "Base case hit"
        #partial_result.append(s)
        final_result.append(copy.deepcopy(partial_result))
        #print " "*tab + "Global res till now: " + str(final_result)
    
    else:
        
        for idx,ch in enumerate(s):
            
#             print " "*tab + " s :" + s+ " idx:" + str(idx)
#             print " "*tab + "partial res in loop : " + str(partial_result)
            if( isPalindrome(s[:idx+1],tab)):
                num_partial_res += 1
                partial_result.append(s[:idx+1])
                #print " "*tab + "partial res before recurring : " + str(partial_result)
                palindromicPartitions(s[idx+1:], final_result, partial_result, num_partial_res,tab+1)
                num_partial_res-=1
               
            partial_result = partial_result[:num_partial_res]
            #print " "*tab + "partial res end loop for : " +s + " num res: " + str(num_partial_res) + " partial res= " + str(partial_result)


def printRes(res):
    
    for r in res:
        print r

if __name__ == "__main__":
    
    res = []
    palindromicPartitions("0204451881",res,[],0,0)
    printRes(res)
    
    