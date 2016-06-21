import collections

def create_freq_table(src):
    
    freq_table = collections.defaultdict(int)
    
    #Do processig here
    for ch in src:
        freq_table[ch] += 1
    
    return (freq_table, set(src))
    
def isMatchFound(freq_table):
    
    if len(freq_table) == 0:
        return True
    return False

def check_anagram_substring(src,target):
    
    freq_count,unique_chars = create_freq_table(src)
    start = 0
    end = 0
    length_src = len(src)
    
    print freq_count
    print unique_chars
    
    while( end < length_src):
        
        if isMatchFound(freq_count):
            return True
        if target[end] in freq_count:
            freq_count[target[end]] -=1
        
        end +=1
        
        print freq_count
    
    print "**********"      
    #start sliding. Only leaving and entering chars matter
    
    while( end < len(target)):
        
        print "start: " + str(start) + " end: " + str(end)
        
        if target[start] in unique_chars:
            freq_count[target[start]] += 1
            if freq_count[target[start]] == 0:
                del freq_count[target[start]]
        start +=1
        
        if target[end] in unique_chars:
            freq_count[target[end]] -=1
            if freq_count[target[end]] == 0:
                del freq_count[target[end]]
            
        
        if isMatchFound(freq_count):
            return True
        end +=1
        
        print "start: " + str(start) + " end: " + str(end)
        
        
        print freq_count
        
        
    return False

if __name__ == "__main__":
    
        src = "xyzzx"
        target = "afdgzyxxzksldfm"
        print check_anagram_substring(src,target)
        
        
        
    
    