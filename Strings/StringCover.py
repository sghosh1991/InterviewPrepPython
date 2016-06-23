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
    
    print missing
    return missing


def remove_element(missing,ch):
    
    missing[ch] -= 1
    if missing[ch] == 0:
        del missing[ch]
    return missing

def find_smallest_substring_containing_missing_items(dna):
    
    min_substring_len = sys.maxint
    start_idx = 0
    end_idx = 0
    dna_len = len(dna)
    
    missing = create_chars_to_del_table(dna)
    missing_set_chars = set()
    for key in missing.keys():
        missing_set_chars.add(key)
    
    while end_idx < dna_len:
        
        
        if dna[end_idx] in missing:
            remove_element(missing,dna[end_idx])
        
            if len(missing) == 0:
                

                #start chopping elemnts from start
                while dna[start_idx] not in missing_set_chars:
                    start_idx += 1

                if (end_idx - start_idx + 1) < min_substring_len:
                    
                    min_substring_len = end_idx - start_idx + 1
                    
                #chop another element that foirms the critical set and start over again
                missing[dna[start_idx]] += 1
                start_idx += 1
         
        end_idx +=1
                        
    return min_substring_len
                        

if __name__ == "__main__":
#     dna_len = sys.stdin.readlines()
#     dna = sys.stdin.readlines()
    
#     print dna_len
#     print dna

    print find_smallest_substring_containing_missing_items("GAAATAAA")

        
        
        
        
            
            
    
    
    
    
        