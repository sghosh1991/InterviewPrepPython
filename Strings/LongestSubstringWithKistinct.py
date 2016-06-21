import collections
from __builtin__ import str
from _ast import Str


    
def reduce_count(ch,freq_table):
    
    freq_table[ch] -= 1
    if freq_table[ch] == 0:
        del freq_table[ch]
    
    return freq_table


def chop_trailing_chars(s,freq_table,start,k):
    
    print "###"
    while(len(freq_table) != k-1):
        #print str(len(freq_table)) + " : " + str(start)
        reduce_count(s[start], freq_table)
        start += 1
    
    return start

def longest_substring_with_K_distinct(s, k):
    
    max_len = 0
    start_max = 0
    end_max = 0
    curr_max = 0
    
    start = 0
    end =0
    len_str = len(s)
    
    freq_table = collections.defaultdict(int)
    #print freq_table
    
    while(end < len_str):
        
        print "Start: " + str(start) + " End: " + str(end)
        
        
        if (len(freq_table) == k) and (s[end] not in freq_table):
            start = chop_trailing_chars(s, freq_table, start,k)
     
        freq_table[s[end]] += 1
            
        if end - start + 1 > max_len:
            max_len  = end - start +1
            start_max = start
            end_max = end  
            
            print "Max changed: start_max: " + str(start_max) + " end_max: " + str(end_max)   
        
        end += 1
        print freq_table
        print "*****************\n"
        
        
    return s[start_max:start_max+max_len]


if __name__ == "__main__":
    print longest_substring_with_K_distinct("ecebaaabec" ,  2)
    