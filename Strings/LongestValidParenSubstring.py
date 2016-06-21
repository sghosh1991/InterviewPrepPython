
(X,Y) = (0,1)
(CHAR,INDEX) = (0,1)

def contains(interval1,interval2):
    
    #checks if interval1 contains interval2
    
    if(interval1[X] <= interval2[X] and interval1[Y] >= interval2[Y]):
        
        return True
    else:
        return False
    
    
def adjacent(interval1,interval2):
    
    #checks to see if interval1 and interval2 are adjacent
    
    if(interval1[Y] + 1 == interval2[X]):
        return True
    
 
def longestValidParen(str):
    
    stack = []
    ranges = []
    
    for i,c in enumerate(str):
        
        if (c in "("):
            stack.insert(0, (c,i))
        else:
            if(len(stack) > 0):
                
                if(stack[0][CHAR] in '(' ):
                    
                    ranges.append((stack[0][INDEX],i))
                    stack.pop(0)
        print "Stack "
        print stack
        print "Ranges "
        print ranges
    findLongest(ranges)
        

def intervalLen(interval):
    return interval[Y]-interval[X]+1


def findLongest(ranges):
    
    
    currInterval = ranges[0]
    maxLen = intervalLen(currInterval)
    for interval in ranges[1:]:
        
        print currInterval
        print interval
        print "===="
        
        if(adjacent(currInterval,interval) == True):
            currInterval = (currInterval[X],interval[Y])
            print "mergerd"
            if intervalLen(currInterval) > maxLen:
                maxLen = intervalLen(currInterval)
            continue
        
        if(contains(interval,currInterval)):
            
            currInterval = interval
            if(intervalLen(currInterval) > maxLen):
                maxLen = intervalLen(currInterval)
            continue
            
        
        
        currInterval = interval
            
    print maxLen   
        
   

if __name__ == "__main__":
    
    longestValidParen(")()((()()())(")
    