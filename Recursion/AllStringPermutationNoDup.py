'''
Creation Date: Jul 2, 2016
@author : Santosh Ghosh

Problem Statement: Given a string s, generate all anagrams of the string. There are no duplicate characters in 
the string. 

Input: String S

Output: A set of all anagrams of the string.

Logic Applied: Permutation of 3 chars P(abc) = Insert a in all possible locations of P(bc). 
P(bc) = bc,cb
P(abc) = abc,bac,bca <--- put a in all possible locs of bc
         acb,cab,cba <--- put a in all possible locs of cb
'''

def insertInAllPoosibleLocs(char_to_insert,partial_res):
    
    res = []
    #do stuff
    for anagram in partial_res:
        for i in range(len(anagram)+1):
            res.append(anagram[0:i]+char_to_insert+anagram[i:])
    
    
    #print res
    return res


def findAnagrams(s, idx_to_process,tab):
    
    print " "*tab + "Called with " + str(idx_to_process)
    
    #base case
    if idx_to_process == len(s)-1:
        print " "*tab + " Base case hit"
        
        return [s[idx_to_process]]
        #return [s[idx_to_process]+s[idx_to_process+1],s[idx_to_process+1]+s[idx_to_process]]
    
    
    partial_res = findAnagrams(s, idx_to_process+1,tab+1)
    print " "*tab + "partial result: " + str(partial_res)
    partial_res_idx_to_process = insertInAllPoosibleLocs(s[idx_to_process], partial_res)
    print " "*tab + "partial result idx to process: " + str(partial_res_idx_to_process)
    
    return partial_res_idx_to_process


if __name__ == "__main__":
    
    #print str
    findAnagrams('abcd',0, 0)
    
    