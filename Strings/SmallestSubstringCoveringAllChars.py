'''
Creation Date: Jun 23, 2016
@author : Santosh Ghosh

Problem Statement: 

Input: 

Output: 

Logic Applied:
'''

import sys
import collections

def create_chars_to_del_table(dna):
    
    missing = collections.defaultdict(int)
    
    freq_table = dict()
    freq_table['A'] = 0
    freq_table['T'] = 0
    freq_table['G'] = 0
    freq_table['C'] = 0
    
    #Do counting here
    for ch in dna:
        freq_table[ch] += 1
    
    for ch,count in freq_table.items():
        if(count > (len(dna)/4)):
            missing[ch] = count-len(dna)/4
    
    #print missing
    return missing


def remove_element(table,ch):
    
    #print "removing element"
    table[ch] -= 1
    if table[ch] == 0:
        del table[ch]
    #return missing


def isCovered(chars_covered,missing):
    
    print "In checker"
    print chars_covered
    print " missing"
    print missing
    
    for covered_key,missing_key in zip(chars_covered.keys(),missing.keys()):
        if chars_covered[covered_key] < missing[missing_key]:
            print "NOT Covered"
            return False
    print "Covered"
    return True


def find_smallest_substring_containing_missing_items(dna):
    
    min_substring_len = sys.maxint
    start_idx = 0
    end_idx = 0
    dna_len = len(dna)
    
    missing = create_chars_to_del_table(dna)
    missing_set_chars = set()
    for key in missing.keys():
        missing_set_chars.add(key)
        
    print missing
    print missing_set_chars
    
    chars_covered = collections.defaultdict(int)
    for key in missing.keys():
        chars_covered[key] = 0
    
    while end_idx < dna_len:
        
        print "Would process: " + str(end_idx) + " " + dna[end_idx]
        print "****chars_covered***"
        print chars_covered
        print "***missing***"
        print missing
        
        if dna[end_idx] in missing_set_chars:
            #remove_element(missing,dna[end_idx])
            chars_covered[dna[end_idx]] +=1
        
            if isCovered(chars_covered, missing):
                
                print "Start chopping"
                #start chopping elemnts from start
                while isCovered(chars_covered, missing):
                    if dna[start_idx] in missing_set_chars:
                        print "Removing element..." + dna[start_idx] + " at idx " + str(start_idx)
                        chars_covered[dna[start_idx]] -=1
                    print "after removing"
                    print chars_covered
                    start_idx += 1
                print "After chopping start is at" + str(start_idx) + " end is " + str(end_idx)
                if (end_idx - (start_idx-1) + 1) < min_substring_len:
                    
                    min_substring_len = end_idx - (start_idx -1) + 1
                    print "min updated " + str(min_substring_len)
                    
                #chop another element that foirms the critical set and start over again
                #chars_covered[dna[start_idx]] += 1
                #start_idx += 1
         
        end_idx +=1
        print "###Loop end####"
        print "###chars_covered###"
        print chars_covered
        print "###missing###"
        print missing
                        
    return min_substring_len
                        

if __name__ == "__main__":
    
    
    dna = "GAGTGTCG"
    print find_smallest_substring_containing_missing_items(dna)

    

        
        
        
        
            
            
    
    
    
    
        # Enter your code here. Read input from STDIN. Print output to STDOUT