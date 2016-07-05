'''
Creation Date: Jul 2, 2016
@author : Santosh Ghosh

Problem Statement: Given a input string s which may contain duplicate characters find the number of anagrams

Input: String s with duplicate chars

Output: All anagrams

Logic Applied: Look at Page 359 of Cracking the coding interview 6th ed. TC <--- O(n!)
'''
import collections

def prepend_to_anagrams(ch,partial_res):
    
    res = []
    for s in partial_res:
        res.append(ch+s)
    return res
    
'''
Main recursive function to compute anagrams. Results will be in res_to_ret
''' 
def findAnagrams(freq_table,tabs):
    
    print " "*tabs + "Calling with " + str(freq_table)
    #base case
    if len(freq_table) == 1:
        print " "*tabs + "Base case hit." 
        ch = freq_table.keys()[0]
        return [ch*freq_table[ch]]
    res_to_ret =[]
    for key in freq_table.keys():
        
        #update freq table
        freq_table[key] -=1
        #if key is 0 then delete it
        if freq_table[key]==0:
            del freq_table[key]
        partial_res = findAnagrams(freq_table, tabs+1)
        print " "*tabs + "partial res returned " + str(partial_res)
        res_to_ret.extend(prepend_to_anagrams(key, partial_res))
        print " "*tabs + "partial res after appending " + str(res_to_ret)
        freq_table[key] += 1
        
    return res_to_ret

if __name__=="__main__":
    
    s = "aabbbbc"
    freq_table = collections.defaultdict(int)
    for ch in s:
        freq_table[ch] +=1
    
    #print freq_table
    print len(findAnagrams(freq_table,0))
    

    
    